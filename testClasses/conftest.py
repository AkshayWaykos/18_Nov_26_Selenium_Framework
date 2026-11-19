import pytest

from selenium import webdriver

@pytest.fixture()
def openBrowser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://www.saucedemo.com/")
    return driver
