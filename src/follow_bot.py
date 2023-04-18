import sys
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from bot_utils import login
import configparser
import argparse
from selenium.webdriver.firefox.options import Options


# Set up argparse
parser = argparse.ArgumentParser(description="GitHub follow bot")
parser.add_argument("-u", "--username", help="GitHub username", default=None)
parser.add_argument("-p", "--password", help="GitHub password", default=None)
parser.add_argument("-t", "--target", help="Target user to follow their followers", required=True)
parser.add_argument("-n", "--number", help="Number of pages to process (default: 100)", type=int, default=100)
parser.add_argument("-f", "--followers", help="Number of people to follow", type=int, required=True)
args = parser.parse_args()

config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config', 'config.ini')

if args.username is None or args.password is None:
    if os.path.exists(config_file_path):
        config = configparser.ConfigParser()
        config.read(config_file_path)
        username = config.get('GitHub', 'username')
        password = config.get('GitHub', 'password')
    else:
        parser.error("Username and password must be provided as arguments or in the config.ini file.")
else:
    username = args.username
    password = args.password

# Configure webdriver
firefox_options = Options()
firefox_options.binary_location = "/usr/bin/firefox"
driver = webdriver.Firefox(options=firefox_options)
login(driver, username, password)

# Set up target user and number of pages to process
target_user = args.target
num_pages = args.number
max_followers = args.followers
followers_count = 0

for t in range(1, num_pages + 1):
    url = f"https://github.com/{target_user}/?page={t}&tab=followers"
    driver.get(url)
    time.sleep(3000)

    follow_button = driver.find_elements(By.XPATH, "//input[@class='btn btn-sm ' and starts-with(@aria-label, 'Follow')]")

    for i in follow_button:
        i.submit()
        followers_count += 1
        if followers_count >= max_followers:
            break
        time.sleep(120)

    if followers_count >= max_followers:
        break

driver.close()
print("Following finished")