from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import requests

deriver= webdriver.Chrome()
url="https://jqueryui.com/"
deriver.get(url)

deriver.maximize_window()

links=deriver.find_elements(By.TAG_NAME, "a")
total_links=len(links)
print(total_links)
   
time.sleep(2)

for link in links:
    href = link.get_attribute("href")
    if href:
        try:
            response = requests.get(href, timeout=5)
            if response.status_code >= 400:
                print(f"Broken link: {href} (status code: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"Error checking link {href}: {e}")
    
deriver.quit()