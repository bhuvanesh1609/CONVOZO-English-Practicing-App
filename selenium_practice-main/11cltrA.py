from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/")
time.sleep(2)
input_username = driver.find_element(By.ID, "user-name")
input_username.send_keys("standard_user is a testing purupose to malw ")
time.sleep(2)

actions= ActionChains(driver) 
time.sleep(2)
actions.click(input_username).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
time.sleep(3)
actions.send_keys(Keys.ESCAPE).perform()
time.sleep(2)

input_username = driver.find_element(By.ID, "user-name")
input_username.send_keys("standard write")
time.sleep(2)

driver.quit()