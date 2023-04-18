import time
from selenium.webdriver.common.by import By


def login(driver, username, password):
    driver.get("http://github.com/login")
    username_element = driver.find_element(By.ID, "login_field")
    password_element = driver.find_element(By.ID, "password")

    username_element.send_keys(username)
    time.sleep(1)
    password_element.send_keys(password)
    time.sleep(1)

    login_form = driver.find_element(By.XPATH, "//input[@value='Sign in']")
    time.sleep(1)
    login_form.click()
    time.sleep(1)
