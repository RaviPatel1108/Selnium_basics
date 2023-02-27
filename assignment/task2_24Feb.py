from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://www.medibuddy.in")

# Click on Login button
driver.find_element(By.XPATH, "//a[contains(text(),'Login')]").click()

# Click on corporate account
driver.find_element(By.XPATH, "//div[contains(text(),'I have a Corporate Account')]").click()

# Click on login and pswd link
driver.find_element(By.XPATH, "//div[contains(text(),'Login using Username & Password')]").click()

# Enter Username details
driver.find_element(By.NAME, "userName").send_keys("RaviPatel")

# Click Proceed button
driver.find_element(By.XPATH, "//button[contains(text(),'Proceed')]").click()

# Enter Password details
driver.find_element(By.NAME, "password").send_keys("RaviPatel@123")

# Click on Login button
driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()

# Check Error Message
print("Error Message : ", driver.find_element(By.XPATH, "//div[contains(text(),'valid')]").text)

time.sleep(10)

driver.quit()