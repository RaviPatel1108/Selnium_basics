from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(5)

driver.get("https://netbanking.hdfcbank.com/netbanking/")

driver.switch_to.frame(driver.find_element(By.XPATH, "//frame[@name='login_page']"))

driver.find_element(By.XPATH, "//input[@name='fldLoginUserId']").send_keys("test123")

driver.find_element(By.XPATH, "//a[contains(@onclick,'return fLogon')]").click()

time.sleep(10)

driver.quit()