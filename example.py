import scrape_x 

driver = scrape_x.driver

#update username and password for login
username = ""
password=""

if(scrape_x.login(scrape_x.driver,username,password)==True):
    print("Login successful")

user_info = scrape_x.collect_user_info(driver, "BillGates")
print(user_info)

user_posts = scrape_x.collect_posts_of_user(driver,"BillGates",5)
print(user_posts)

user_followings = scrape_x.collect_following(scrape_x.driver,"BillGates",5)
print(user_followings)

followers = scrape_x.collect_followers(scrape_x.driver,"BillGates",5)
print(followers)

driver.quit()
