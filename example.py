import scrape_x 

# #update username and password for login
# username = ""
# password=""

# if(scrape_x.login(scrape_x.driver,username,password)==True):
#     print("Login successful")

user_profile = scrape_x.collect_user_info(scrape_x.driver, "BillGates")
print(user_profile)

user_posts = scrape_x.collect_tweets_of_user(scrape_x.driver,"elonmusk",20)
print(user_posts)