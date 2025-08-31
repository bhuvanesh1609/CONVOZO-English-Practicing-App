from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
url="https://training.openspan.com/login"
driver.get(url)
element1=driver.find_element(By.ID, "login_button").is_enabled()
time.sleep(2)
driver.find_element(By.ID, "user_name").send_keys("abinesh")
driver.find_element(By.ID, "user_pass").send_keys("12334")
time.sleep(2)

element2=driver.find_element(By.ID, "login_button").is_enabled()
print(element2)
driver.quit()