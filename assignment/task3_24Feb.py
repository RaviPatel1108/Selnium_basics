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

driver.find_element(By.LINK_TEXT, 'select your product type').click()

driver.find_element(By.LINK_TEXT, 'Credit Card').click()

driver.find_element(By.CSS_SELECTOR, "#citiCard1").send_keys("7897")
driver.find_element(By.CSS_SELECTOR, "input[name='citiCard2']").send_keys("7897")
driver.find_element(By.CSS_SELECTOR, "[name='citiCard3']").send_keys("7897")
driver.find_element(By.ID, "citiCard4").send_keys("7897")

driver.find_element(By.ID, "cvvnumber").send_keys("889")

#approach 1 - not working
# d.find_element(By.ID,"bill-date-long").send_keys("14/04/2022")

#approach 2
# d.find_element(By.ID,"bill-date-long").click()
#
# select_year=Select(d.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
# select_year.select_by_visible_text("2000")
#
# select_month=Select(d.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
# select_month.select_by_visible_text("Apr")
#
# d.find_element(By.LINK_TEXT,"14").click()

#approach 3 - javascript
driver.execute_script("document.querySelector('#bill-date-long').value='11/09/2000'")

# Click on Proceed button using CSS selector

driver.find_element(By.CSS_SELECTOR, 'input[type="button"]').click()

print(driver.find_element(By.XPATH, "//li[Contains(text(),'Terms')]").text)


time.sleep(5)
driver.quit()

