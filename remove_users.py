from selenium import webdriver
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

#Firefox used
driver = webdriver.Firefox()
# base url
driver.get("http://github.com/login")

username = driver.find_element_by_id("login_field")
password = driver.find_element_by_id("password")

# password and username need to go into these values
username.send_keys("") # there you have to input your GitHub Login
time.sleep(1)
password.send_keys("") # there you have to input your GitHub password
time.sleep(1)


login_form = driver.find_element_by_xpath("//input[@value='Sign in']")
time.sleep(1)
login_form.click()
time.sleep(1)

prepend = [""] # there you have to input your GitHub username


for user in prepend:
    for i in range(0, 200):
        for t in range(1, 100):
            string = "https://github.com/{}/?page={}&tab=following".format(user, t)
            driver.get(string)
            time.sleep(3)

            follow_button = driver.find_elements_by_xpath("//input[@aria-label='Unfollow this person']")

            # time.sleep(1)
            # print len(follow_button)
            try:
                for i in follow_button:
                    i.submit()
            except:
                pass
            time.sleep(3)



driver.close()

time.sleep(3)

time.sleep(3)

driver.close()