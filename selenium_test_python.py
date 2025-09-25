from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

baseUrl = "https://the-internet.herokuapp.com/"
driver = webdriver.Chrome()

def common():
    driver.get(baseUrl)

def teardown():
    driver.quit()

def basic_authentication_test(username, password):
    common()
    baseUrl_trimmed = baseUrl[8:]
    print(baseUrl_trimmed)
    path = "/basic_auth"
    driver.get(f"https://{username}:{password}@{baseUrl_trimmed}{path}")
    print(driver.title)

    driver.implicitly_wait(10)
    driver.get_screenshot_as_file("basic_auth.png")

    status = driver.save_screenshot("Users/user/OneDrive/Documents/python_workspace/SeleniumWithPython/selenium_screenshot.png")
    print("Screenshot saved?", status)
    teardown()
    
basic_authentication_test("admin", "admin")