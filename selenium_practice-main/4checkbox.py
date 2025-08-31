from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Chrome()
url="https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php"
driver.get(url)
time.sleep(2)
hobbies=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,"hobbies"))
)
hobbies.click()
time.sleep(2)
driver.maximize_window()