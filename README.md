# x_scraper

## Description
A python project for scraping X

## Installation

Before using the functions provided in this project, you need to install the required packages listed in the `requirements.txt` file. You can do this by running the following command:

```sh
pip install -r requirements.txt
```

## Functions

### `login(driver: webdriver.Chrome, username: str, password: str) -> bool`

This function logs into the web application using the provided username and password.

**Parameters:**
- `driver` (webdriver.Chrome): The Chrome WebDriver instance used to interact with the browser.
- `username` (str): The username for logging into the web application.
- `password` (str): The password for logging into the web application.

**Returns:**
- `bool`: Returns `True` if the login was successful, `False` otherwise.

### `collect_user_info(driver: webdriver.Chrome, username: str) -> dict`

This function collects user information from the web application for the specified username.

**Parameters:**
- `driver` (webdriver.Chrome): The Chrome WebDriver instance used to interact with the browser.
- `username` (str): The username for which to collect information.

**Returns:**
- `dict`: A dictionary containing the user's information with the following keys:
  - `given_name` (str): The user's given name.
  - `user_bio` (str): The user's biography.
  - `user_location` (str): The user's location.
  - `number_of_followers` (int): The number of followers the user has.
  - `number_of_following` (int): The number of users the user is following.
  - `number_of_posts` (int): The number of posts the user has made.
  - `user_website` (str): The user's website URL.
  - `username` (str): The username.
  - `user_join_date` (str): The date the user joined -> 'dd/mm/yyyy'

### `collect_posts_of_user(driver: webdriver.Chrome, username: str, n: int) -> list[str]`

This function collects the latest n posts from the specified user.

**Parameters:**
- `driver` (*webdriver.Chrome*): The Chrome WebDriver instance used to interact with the browser.
- `username` (*str*): The username for which to collect posts.
- `n` (*int*): The number of posts to collect.

**Returns:**
- `list[str]`: A list of strings, each representing the text of the post from the user.

### `collect_following(driver: webdriver.Chrome, username: str, n: int) -> list[dict]`

This function collects the information of the users followed by the specified user.

**Parameters:**
- `driver` (*webdriver.Chrome*): The Chrome WebDriver instance used to interact with the browser.
- `username` (*str*): The username for which to collect the following list.
- `n` (*int*): The number of users to collect from the following list.

**Returns:**
- `list[dict]`: A list of dictionaries, each containing the information of a followed user with the following keys:
  - `given_name` (*str*): The user's given name.
  - `user_bio` (*str*): The user's biography.
  - `user_location` (*str*): The user's location.
  - `number_of_followers` (*int*): The number of followers the user has.
  - `number_of_following` (*int*): The number of users the user is following.
  - `number_of_posts` (*int*): The number of posts the user has made.
  - `user_website` (*str or None*): The user's website URL.
  - `username` (*str*): The username.
  - `user_join_date` (*str*): The date the user joined.

### `collect_followers(driver: webdriver.Chrome, username: str, n: int) -> list[dict]`

This function collects the information of the followers of the specified user.

**Parameters:**
- `driver` (*webdriver.Chrome*): The Chrome WebDriver instance used to interact with the browser.
- `username` (*str*): The username for which to collect the followers list.
- `n` (*int*): The number of followers to collect.

**Returns:**
- `list[dict]`: A list of dictionaries, each containing the information of a follower with the following keys:
  - `given_name` (*str*): The user's given name.
  - `user_bio` (*str*): The user's biography.
  - `user_location` (*str*): The user's location.
  - `number_of_followers` (*int*): The number of followers the user has.
  - `number_of_following` (*int*): The number of users the user is following.
  - `number_of_posts` (*int*): The number of posts the user has made.
  - `user_website` (*str or None*): The user's website URL.
  - `username` (*str*): The username.
  - `user_join_date` (*str*): The date the user joined.


## Example Usage

```python
import scrape_x 

driver = scrape_x.driver

#update username and password for login
username = ""
password=""

if(scrape_x.login(scrape_x.driver,username,password)==True):
    print("Login successful")

user_info = scrape_x.collect_user_info(driver, "BillGates")
print(user_info)

# Example output:
# {
#   'given_name': 'Bill Gates',
#   'user_bio': "Sharing things I'm learning through my foundation work and other interests.",
#   'user_location': 'Seattle, WA',
#   'number_of_followers': 64656966,
#   'number_of_following': 588,
#   'number_of_posts': 4469,
#   'user_website': 'https://t.co/UkvHzxDwkH',
#   'username': 'BillGates',
#   'user_join_date': '24.06.2009'
# }

user_posts = scrape_x.collect_posts_of_user(driver,"BillGates",5)
print(user_posts)

# Example output:
# [
#   "Post 1 content",
#   "Post 2 content",
#   "Post 3 content",
#   "Post 4 content",
#   "Post 5 content"
# ]

user_followings = scrape_x.collect_following(scrape_x.driver,"BillGates",2)
print(user_followings)

# Example output:
# [
#   {
#     'given_name': 'Ratan N. Tata',
#     'user_bio': 'Chairman Emeritus, Tata Sons. Chairman, Tata Trusts',
#     'user_location': 'Mumbai',
#     'number_of_followers': 12962010,
#     'number_of_following': 7,
#     'number_of_posts': 188,
#     'user_website': None,
#     'username': 'RNTata2000',
#     'user_join_date': '05.04.2011'
#   },
#   {
#     'given_name': 'Mark Suzman',
#     'user_bio': 'CEO of @GatesFoundation. Working to ensure everyone can live a healthy life & reach their full potential. Father, husband, optimist.',
#     'user_location': 'Seattle, WA',
#     'number_of_followers': 39304,
#     'number_of_following': 1038,
#     'number_of_posts': 3220,
#     'user_website': 'https://t.co/yCyjUie0do',
#     'username': 'MSuzman',
#     'user_join_date': '19.04.2010'
#   }
# ]

followers = scrape_x.collect_followers(scrape_x.driver,"BillGates",2)
print(followers)

# Example output:
# [
#   {
#     'given_name': 'Ratan N. Tata',
#     'user_bio': 'Chairman Emeritus, Tata Sons. Chairman, Tata Trusts',
#     'user_location': 'Mumbai',
#     'number_of_followers': 12962010,
#     'number_of_following': 7,
#     'number_of_posts': 188,
#     'user_website': None,
#     'username': 'RNTata2000',
#     'user_join_date': '05.04.2011'
#   },
#   {
#     'given_name': 'Mark Suzman',
#     'user_bio': 'CEO of @GatesFoundation. Working to ensure everyone can live a healthy life & reach their full potential. Father, husband, optimist.',
#     'user_location': 'Seattle, WA',
#     'number_of_followers': 39304,
#     'number_of_following': 1038,
#     'number_of_posts': 3220,
#     'user_website': 'https://t.co/yCyjUie0do',
#     'username': 'MSuzman',
#     'user_join_date': '19.04.2010'
#   }
# ]

driver.quit()

```