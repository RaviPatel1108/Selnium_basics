import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Opening the Chrome browser
driver = webdriver.Chrome()
driver.implicitly_wait(10)
# Maximize the window
driver.maximize_window()
# Open URL
driver.get("https://github.com/login")

driver.find_element(By.ID, "login_field").send_keys("hello")

driver.find_element(By.ID, "password").send_keys("89hello")

driver.find_element(By.NAME, "commit").click()

time.sleep(10)