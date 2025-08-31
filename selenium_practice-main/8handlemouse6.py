from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

import time

driver=webdriver.Chrome()
url="https://practice.expandtesting.com/hovers"
driver.get(url)
time.sleep(2)
driver.maximize_window()
actions=ActionChains(driver)

hover_element=driver.find_element(By.XPATH, "//*[@id='core']/div/div/div[1]/img")
actions.move_to_element(hover_element).perform()
print("step1 btn hover")
time.sleep(2)

hover_element=driver.find_element(By.XPATH, "//*[@id='core']/div/div/div[2]/img")
actions.move_to_element(hover_element).perform()
print("step2 btn hover")
time.sleep(2)

hover_element=driver.find_element(By.XPATH, "//*[@id='core']/div/div/div[3]/img")
actions.move_to_element(hover_element).perform()
print("step3 btn hover")
time.sleep(2)

driver.quit()