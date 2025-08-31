from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
url="https://seleniumbase.io/demo_page/"
driver.get(url)
time.sleep(2)


element = driver.find_element(By.TAG_NAME, "h2")
element.screenshot("screenshot.png")

driver.get_screenshot_as_file(".\\test1.png")
driver.get_screenshot_as_file("\\test2.png")