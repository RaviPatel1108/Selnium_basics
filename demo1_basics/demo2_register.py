import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://facebook.com")

driver.find_element(By.LINK_TEXT, "Create new account").click()
driver.find_element(By.NAME, "firstname").send_keys("john")
driver.find_element(By.NAME, "lastname").send_keys("cena")
driver.find_element(By.ID, "password_step_input").send_keys("welcome@123")
driver.find_element(By.XPATH, "//input[@value = '-1']").click()
driver.find_element(By.NAME, "websubmit").click()

select_day = Select(driver.find_element(By.ID, "day")).select_by_value('11')

select_month = Select(driver.find_element(By.ID, "month")).select_by_value('8')

select_year = Select(driver.find_element(By.ID, "year")).select_by_value('1991')


time.sleep(10)



