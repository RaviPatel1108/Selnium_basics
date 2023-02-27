from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://www.online.citibank.co.in/")

# Close Pop up window
driver.find_element(By.XPATH, "//a[@title='Close']").click()

# Click on Sign on
driver.find_element(By.XPATH, "//span[contains(text(),'Login')]").click()

# Switch to new window
driver._switch_to.window(driver.window_handles[1])

# Click on forgot user ID
driver.find_element(By.XPATH, "//div[contains(@onclick,'ForgotUserID')]").click()

Select(driver.find_element(By.XPATH, "//a[contains(text(),'select your product type']")).select_by_value("Credit Card")

time.sleep(10)

driver.quit()