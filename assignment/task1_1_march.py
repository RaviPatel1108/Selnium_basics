from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(10)

# Open Red bus Application
driver.get("https://www.redbus.in/")

# Click on sign in
driver.find_element(By.ID, 'i-icon-profile').click()

driver.find_element(By.ID, 'signInLink').click()

# Enter mobile number
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='modalIframe']"))

time.sleep(1)

driver.find_element(By.XPATH, "//input[@id='mobileNoInp']").send_keys(1234)

# Get the error message
error_msg = driver.find_element(By.XPATH, "//span[contains(text(),'Please enter valid mobile number')]").text

print(error_msg)

time.sleep(10)

driver.quit()