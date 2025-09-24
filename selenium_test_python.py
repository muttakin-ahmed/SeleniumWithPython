from selenium import webdriver
from selenium.webdriver.common.by import By

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
    teardown()
    
basic_authentication_test("admin", "admin")