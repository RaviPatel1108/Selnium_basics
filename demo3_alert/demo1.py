from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(5)

driver.get("https://netbanking.hdfcbank.com/netbanking/IpinResetUsingOTP.htm")

driver.find_element(By.XPATH, "//img[@alt='Go']").click()

print(driver.switch_to.alert.text)

driver.switch_to.alert.accept()

time.sleep(10)

driver.quit()