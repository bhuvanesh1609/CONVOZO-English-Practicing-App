from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Chrome()
url="https://dev.automationtesting.in/alerts"
driver.get(url)
time.sleep(2)
driver.maximize_window()

wait=WebDriverWait(driver, 10)
simple_alert=wait.until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='vertical-tabpanel-0']/div/p/button"))
)
simple_alert.click()

alerts=driver.switch_to.alert
print("step 1:ok")
alerts.accept()
time.sleep(2)


#canlcel and confirm alert
driver.find_element(By.XPATH, "//*[@id='vertical-tab-1']").click()
confirm_alert=wait.until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='vertical-tabpanel-1']/div/p/button"))
)
confirm_alert.click()
time.sleep(2)
confirm_alert=driver.switch_to.alert
time.sleep(2)
confirm_alert.accept()
time.sleep(2)
confirm_alert.click()
confirm_alert=driver.switch_to.alert
confirm_alert.dismiss()
time.sleep(2)

driver.quit()