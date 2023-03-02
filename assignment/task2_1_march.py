from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(10)

# Open PHP travels application
driver.get("https://www.phptravels.net/home")

# Go to flights
driver.find_element(By.XPATH, "//a[text()='flights']").click()


# select flight from and to destination
driver.find_element(By.XPATH, "//input[contains(@placeholder,'Flying From')]").send_keys("los angles")

actions = webdriver.ActionChains(driver)

actions.send_keys(webdriver.Keys.ARROW_DOWN).send_keys(webdriver.Keys.ENTER).perform()

driver.find_element(By.XPATH, "//input[contains(@placeholder,'To Destination')]").send_keys("Dallas")

actions.send_keys(webdriver.Keys.ARROW_DOWN).send_keys(webdriver.Keys.ENTER).perform()

driver.find_element(By.XPATH, "//input[@id='departure']").click()

for i in range(10):
    actions.send_keys(webdriver.Keys.BACKSPACE).pause(1).perform()

time.sleep(10)

driver.find_element(By.XPATH, "//input[@id='departure']").send_keys("30-05-2023")

time.sleep(10)

driver.find_element(By.XPATH, "//a[@data-toggle='dropdown']").click()

driver.find_element(By.XPATH, "//i[contains(@class,'la la-plus')]").click()

time.sleep(10)

driver.find_element(By.ID, "flights-search").click()

time.sleep(10)

driver.quit()