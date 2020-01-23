# File to hold global pytest fixtures
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver():
    # before each test
    web_driver = webdriver.Chrome('../chromedriver.exe')
    yield web_driver
    # after each test
    web_driver.quit()


@pytest.fixture
def wait(driver):
    yield WebDriverWait(driver, timeout=10)
