import scrape_x 

driver = scrape_x.driver

#update username and password for login
username = ""
password=""

if(scrape_x.login(scrape_x.driver,username,password)==True):
    print("Login successful")

# user_profile = scrape_x.collect_user_info(driver, "BillGates")
# print(user_profile)

# user_posts = scrape_x.collect_tweets_of_user(driver,"BillGates",20)
# print(user_posts)

# user_followings = scrape_x.collect_following(scrape_x.driver,"BillGates",5)
# print(user_followings)

# followers = scrape_x.collect_followers(scrape_x.driver,"BillGates",5)
# print(followers)

driver.quit()
