import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")

driver.find_element(By.NAME, "UserFirstName").send_keys("John")

select_job_title = Select(driver.find_element(By.NAME, "UserTitle")).select_by_value("IT_Manager_AP")

select_employees = Select(driver.find_element(By.NAME, "CompanyEmployees")).select_by_value("250")

select_country = Select(driver.find_element(By.NAME, "CompanyCountry")).select_by_value("GB")

driver.find_element(By.CLASS_NAME, "checkbox-ui").click()

driver.find_element(By.NAME, "start my free trial").click()




time.sleep(10)
