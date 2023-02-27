from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(5)

driver.get("https://www.oracle.com/in/database/")

driver.find_element(By.ID, "acctBtnLabel").click()

driver.find_element(By.XPATH, "//a[contains(@data-lbl,'profile:sign-in-account')]").click()

print(driver.title)

print(driver.current_url)

print("Header: ", driver.find_element(By.XPATH, "//h2[contains(text(), 'Oracle account')]").text)

driver.find_element(By.ID, "sso_username").send_keys("john")

driver.find_element(By.ID, "ssopassword").send_keys("john123")

driver.find_element(By.ID, "signin_button").click()

time.sleep(5)

print("Error:", driver.find_element(By.XPATH, "//div[contains(text(),'Invalid')]").text)

driver.quit()

