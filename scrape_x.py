from selenium import webdriver
import logging
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import chromedriver_autoinstaller
import json
from dateutil import parser
chromedriver_autoinstaller.install()

basePath = 'https://www.twitter.com/'
logger = logging.getLogger("scrape_x")
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)


def login(driver:webdriver.Chrome, username: str, password: str):
    url = basePath + 'login'
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    try:
        next_button_path = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]'
        login_button_path = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div'
        password_input_path = '[autocomplete="current-password"]'

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[autocomplete="username"]'))).send_keys(username)
        next_button = wait.until(EC.presence_of_element_located((By.XPATH, next_button_path)))
        next_button.click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, password_input_path)),timeout=3).send_keys(password)
        login_button = wait.until(EC.presence_of_element_located((By.XPATH, login_button_path)))
        login_button.click()
        
        wait.until(EC.url_to_be("https://twitter.com/home"),timeout=3)
        
        if driver.current_url == "https://twitter.com/home":
            return True
        else:
            logger.error("Unexpected URL after login")
            return False
    
    except TimeoutException:
        logger.error("Timed out waiting for login process")
        return False
        
    except Exception as e:
        logger.error(f"Failed to login: {str(e)}")
        return False


def collect_user_info(driver:webdriver.Chrome, username: str):
    user_profile = {}
    
    url = basePath + username
    driver.get(url)
    xpath_expression = '//*[@data-testid="UserProfileSchema-test"]'

    try:
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_expression)))

        json_str = element.get_attribute("innerText")
        profile = json.loads(json_str)
        driver.close()
        
        author = profile.get('author', {})
        interaction_statistic = author.get('interactionStatistic', [])
        
        user_profile["given_name"] = author.get('givenName', None)
        user_profile["user_bio"] = author.get('description', None) if author.get('description') else None
        user_profile["user_location"] = author.get('homeLocation', {}).get('name', None) if author.get('homeLocation', {}).get('name') else None
        user_profile["number_of_followers"] = next((interaction['userInteractionCount'] for interaction in interaction_statistic if interaction['interactionType'] == 'https://schema.org/FollowAction'), None)
        user_profile["number_of_following"] = next((interaction['userInteractionCount'] for interaction in interaction_statistic if interaction['interactionType'] == 'https://schema.org/SubscribeAction'), None)
        user_profile["number_of_posts"] = next((interaction['userInteractionCount'] for interaction in interaction_statistic if interaction['interactionType'] == 'https://schema.org/WriteAction'), None)
        user_profile["user_website"] = profile.get("relatedLink", [])[0] if profile.get("relatedLink", []) else None
        user_profile["username"] = author.get('additionalName', None)
        user_join_date_str = profile.get('dateCreated', None)
        if user_join_date_str:
            user_join_date = parser.parse(user_join_date_str)
            user_profile["user_join_date"] = user_join_date.strftime('%d.%m.%Y')
        else:
            user_profile["user_join_date"] = None

        return user_profile

    except:
        print("Timed out waiting for elements to appear")
        driver.close()
        return {}

    
def collect_tweets_of_user(driver:webdriver.Chrome, username: str, n:int):
    
    url = basePath + username
    driver.get(url)
    collected_elements = []
    collected_text = []

    xpath_expression = '//*[@data-testid="tweetText"]'

    while True:
        try:
            elements = WebDriverWait(driver, 1000).until(EC.presence_of_all_elements_located((By.XPATH, xpath_expression)))

            initial_scroll_position = driver.execute_script("return window.scrollY;")

            
            for element in elements:
                if len(collected_text) >= n:
                    break 
                if element not in collected_elements:
                    text = element.text.strip()
                    collected_elements.append(element)
                if text:
                    if text not in collected_text:
                        collected_text.append(text)
                       
            # Scroll back to the initial scroll position
            driver.execute_script("window.scrollTo(0, arguments[0]);", initial_scroll_position)
            # Scroll down to load more elements
            driver.execute_script("window.scrollBy(0, window.innerHeight);")

            if len(collected_text) >= n:
                break 
        except:
            break 
    driver.close()
    return collected_text