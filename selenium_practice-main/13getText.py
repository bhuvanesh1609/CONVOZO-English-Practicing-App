from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
url="https://practicetestautomation.com/practice-test-login/"
driver.get(url)
time.sleep(2)

element = driver.find_element(By.TAG_NAME, "h2").text
print(element)
time.sleep(2)

expected_result="Testing login"

assert element == expected_result, f"text doesnot match Expected '{expected_result}', but got '{element}'"

driver.close()