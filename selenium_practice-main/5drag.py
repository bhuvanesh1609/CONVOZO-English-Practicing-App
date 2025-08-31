from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

import time

driver=webdriver.Chrome()
url="https://testpages.eviltester.com/styled/drag-drop-javascript.html"
driver.get(url)
time.sleep(2)
source=driver.find_element(By.ID,"draggable1")
dest=driver.find_element(By.ID,"droppable1")
actions=ActionChains(driver)
actions.drag_and_drop(source, dest).perform()
time.sleep(2)