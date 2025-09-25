from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.find_element(By.NAME, "q").send_keys("Selenium_python\n")
print(driver.title)
driver.quit()