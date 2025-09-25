import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

baseUrl = ""

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_google_title(driver):
    baseUrl = "https://www.google.com"
    driver.get(baseUrl)
    assert 'Google' in driver.title