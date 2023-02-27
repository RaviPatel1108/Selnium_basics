from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://www.automationworld.com/")

# Click on Subscribe
driver.find_element(By.LINK_TEXT, "Subscribe").click()

driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.XPATH, "//input[@value='344']").click()

driver.find_element(By.NAME, "demo59703").send_keys("Ravi")

driver.find_element(By.NAME, "demo59704").send_keys("Patel")

driver.find_element(By.NAME, "demo59705").send_keys("Automation Engineer")

driver.find_element(By.NAME, "demo59707").send_keys("Einfochips.com")

driver.find_element(By.NAME, "demo59708").send_keys("Einfochips")

driver.find_element(By.NAME, "demo59709").send_keys("1234567890")

select_country = Select(driver.find_element(By.NAME, "demo59710")).select_by_value('189')

driver.find_element(By.NAME, "demo59713").send_keys("Chennai")

driver.find_element(By.NAME, "demo59693").click()

driver.find_element(By.XPATH, "//input[@value='Submit']").click()

print(driver.find_element(By.XPATH, "//li[contains(text(),'Email Address is required.')]").text)

time.sleep(10)

driver.quit()