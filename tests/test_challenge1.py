import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    # before each test
    _driver = webdriver.Chrome('../venv/chromedriver-Windows')
    _driver.get('https://google.com')
    yield _driver
    # after each test
    _driver.quit()


def test_google_title(driver):
    assert 'Google' in driver.title


def test_google_search(driver):
    driver.find_element(By.NAME, 'q').send_keys('puppies')
    driver.find_element(By.NAME, 'btnK').submit()
    assert 'puppies' in driver.title
