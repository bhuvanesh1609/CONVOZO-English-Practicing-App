from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")

actions= ActionChains(driver)

deiver_click=driver.find_element(By.XPATH,"//*[@id='mousehover']")
actions.click(deiver_click).perform()
print("clicked")
time.sleep(2)
driver.close()