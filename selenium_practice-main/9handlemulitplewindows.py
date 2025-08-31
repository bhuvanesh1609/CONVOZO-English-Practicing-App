from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

import time

driver=webdriver.Chrome()
url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)
time.sleep(2)
driver.switch_to.new_window()
time.sleep(2)
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)
total_tabs= len(driver.window_handles)
print(total_tabs)
value=driver.window_handles
print(value)
current_tab=driver.current_window_handle
print(current_tab)
time.sleep(2)
first_tab=driver.window_handles[0]
driver.switch_to.window(first_tab)
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p")
time.sleep(2)