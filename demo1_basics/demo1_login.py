import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://facebook.com")

print(driver.title)

driver.find_element(By.ID, "email").send_keys("123@gmail.com")
driver.find_element(By.ID, "pass").send_keys("1234")

driver.find_element(By.NAME, "login").click()
time.sleep(10)

driver.quit()