import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from bot_utils import login
import configparser

config = configparser.ConfigParser()
config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config', 'config.ini')
config.read(config_file_path)

driver = webdriver.Firefox()
login(driver, config.get('GitHub', 'username'), config.get('GitHub', 'password'))

prepend = [config.get('GitHub', 'username')]

for user in prepend:
    for t in range(1, 100):
        string = "https://github.com/{}/?page={}&tab=following".format(user, t)
        driver.get(string)
        time.sleep(3)

        follow_button = driver.find_elements(By.XPATH, "//input[@aria-label='Unfollow this person']")

        try:
            for i in follow_button:
                i.submit()
        except:
            pass
        time.sleep(3)

driver.close()
