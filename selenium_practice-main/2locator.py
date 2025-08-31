# locator
#  1.ID
# 2.NameError
# 3.LINK TEXT
# 4.PARTIAL LINK TEXT
# 5.CLASS Name
# 6.TAG Name
# 7.css
# 8.XPATH


# ID

from selenium.webdriver.common.by import By
from selenium import webdriver
import time
browser=webdriver.Chrome()
browser.get("https://practicetestautomation.com/practice-test-login/")
print("open browser")
time.sleep(2)
browser.maximize_window()
title=browser.title
print(title)
time.sleep(2)

username=browser.find_element(By.ID,"username")
username.send_keys("student")
time.sleep(2)
password=browser.find_element(By.ID,"password")
password.send_keys("password123")
time.sleep(2)
