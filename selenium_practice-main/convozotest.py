from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
import time

#start
driver = webdriver.Chrome()
url = "https://convo-zo.vercel.app/login"
driver.get(url)
time.sleep(2)
driver.maximize_window()

#function
def Wait_and_click(driver,locator,timeout=10):
    element= WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
    element.click()


#login 

driver.find_element(By.ID,"email").send_keys("abinesh0309@gmail.com")
driver.find_element(By.ID,"password").send_keys("123456")

singup_btn_submit=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='root']/div/form/button"))
)
singup_btn_submit.click()
print("form submitted")
time.sleep(3)

#click on alert button
alerts=driver.switch_to.alert
print("step 1:logged in successfully")
alerts.accept()
time.sleep(5)

#check for broken links 
links=driver.find_elements(By.TAG_NAME, "a")
total_links=len(links)
print(total_links)
time.sleep(2)

has_broken_links = False
print("Checking for broken links...")

for link in links:
    href = link.get_attribute("href")
    if href:
        try:
            response = requests.get(href, timeout=5)
            if response.status_code >= 400:
                print(f"Broken link: {href} (status code: {response.status_code})")
                has_broken_links = True
        except requests.exceptions.RequestException as e:
            print(f"Error checking link {href}: {e}")
            has_broken_links = True
if not has_broken_links:
    print("No broken links found.")

#scroll down

driver.find_element(By.XPATH,"//*[@id='root']/nav/a[1]").click()
driver.execute_script("window.scrollTo(0, 2000);")
time.sleep(2)
print("step 2 : scrolled down successfully in home page")

#roleplay
driver.find_element(By.XPATH,"//*[@id='root']/nav/a[2]").click()
time.sleep(4)

#rolebox hover
element_hover=driver.find_element(By.XPATH,"//*[@id='root']/div[3]/div/div[1]")
action=ActionChains(driver)
action.move_to_element(element_hover).perform()
print("step 3: hovered on rolebox successfully")
time.sleep(2)



#start roleplay
Wait_and_click(driver, (By.XPATH, "//*[@id='root']/div[3]/div/div[1]/a"))
time.sleep(2)
print("entered into roleplay successfully")

driver.find_element(By.XPATH,"//*[@id='root']/section/div[2]/button[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='root']/section/div[2]/button[3]").click()
time.sleep(4)
driver.find_element(By.XPATH,"//*[@id='root']/nav/a[2]").click()
time.sleep(2)
#loop
# for i in range(1,14):
#     locater= f"//*[@id='root']/div[3]/div[{i}]"
#     locate ='//*[@id="root"]/div[3]/div/div[7]/a'
#     Wait_and_click(driver, (By.XPATH, locater))
#     Wait_and_click(driver, (By.XPATH, locate))
#     time.sleep(2)


#pratice
driver.find_element(By.XPATH,"//*[@id='root']/nav/a[3]").click()
time.sleep(2)

#ai
driver.find_element(By.XPATH,"//*[@id='root']/section/div/div[1]/a").click()
time.sleep(2)

driver.back()
time.sleep(2)

#human
driver.find_element(By.XPATH,"//*[@id='root']/section/div/div[2]/a").click()
time.sleep(2)

#leaderboard
driver.find_element(By.XPATH,"//*[@id='root']/nav/a[4]").click()
time.sleep(2)
first_cell = driver.find_element(By.XPATH, "//*[@id='root']/section/table/tbody/tr[1]").text
print("First cell value:", first_cell)
