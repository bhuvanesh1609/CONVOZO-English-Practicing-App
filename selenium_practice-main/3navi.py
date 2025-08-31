from selenium.webdriver.common.by import By
from selenium import webdriver
import time
browser=webdriver.Chrome()
url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
browser.get(url)
time.sleep(3)
browser.maximize_window
time.sleep(3)
conform=browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')
conform.click()
time.sleep(3)
browser.back()
time.sleep(3)
browser.forward()
time.sleep(3)
browser.refresh()
time.sleep(3)
browser.close()