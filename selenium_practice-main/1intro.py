import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#step 1: Open the browser and navigate to the website
driver= webdriver.Chrome()

#step 2:element control
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(2)

singup_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(By.XPATH, "//*[@id='signBtn']"))
singup_button.click()
print("Sign in button clicked")

#step 3:
driver.find_element(By.ID,"username").send_keys("abi")
driver.find_element(By.ID,"email").send_keys("abi0389@gmail.com")
driver.find_element(By.ID,"psw").send_keys("abi")


#step 4:
singup_btn_submit=WebDriverWait(driver,10).untill(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='signup-form']/button"))
)
singup_btn_submit.click()
print("form submitted")

#step 5 verify navigation to home
WebDriverWait(driver,10).until(
    EC.url_changes(driver.current_url)
)

#step 6
WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located((By.ID,"search Box"))
)

search_box = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,"searchBox"))
)

