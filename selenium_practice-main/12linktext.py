
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
url="https://demo.guru99.com/V4/"
driver.get(url)
time.sleep(2)
link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "Bank")
link_text.click()
time.sleep(2)
