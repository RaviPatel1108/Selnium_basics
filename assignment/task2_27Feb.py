from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://www.royalcaribbean.com/")

# driver.find_element(By.XPATH, "//div[contains(@class,'notification-banner__close')]").click()

driver.find_element(By.ID, "rciHeaderSignIn").click()

time.sleep(10)

driver.find_element(By.LINK_TEXT, "Create an account").click()

driver.find_element(By.ID, "mat-input-3").send_keys("Dennis")

driver.find_element(By.ID, "mat-input-4").send_keys("Rich")

driver.find_element(By.XPATH, "//span[normalize-space() ='Month']").click()

driver.find_element(By.XPATH, "//span[normalize-space()='April']").click()

driver.find_element(By.XPATH, "//span[contains(@text(),'Day')]").click()

driver.find_element(By.XPATH, "//span[contains(@text(),'4')]").click()

driver.find_element(By.XPATH, "//input[@data-placeholder='Year']").send_keys("1990")

driver.find_element(By.XPATH, "//span[contains(@text(),'India')]").click()

driver.find_element(By.XPATH, "//input[@data-placeholder='Email address']").send_keys("xyz@gmail.com")

driver.find_element(By.XPATH, "//input[@data-placeholder='Email address']").send_keys("xyz123")

driver.find_element(By.XPATH, "//span[contains(@text(),'What was your first car\'s make or model?')]").click()

driver.find_element(By.XPATH, "//input[@data-placeholder='Answer']").send_keys("Maruti")

driver.find_element(By.ID, 'mat-checkbox-1-input').click()

driver.find_element(By.XPATH, "//button[contains(@text(),'Done')]").click()

time.sleep(10)

driver.quit()