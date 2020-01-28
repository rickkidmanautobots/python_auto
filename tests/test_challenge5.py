import pytest
import time
from collections import Counter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_copart_makes_categories(driver, wait):
    driver.get('https://copart.com')

    element = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="Serverside Quickpicks"]//div')))
    srch = driver.find_element(By.ID, 'input-search')
    srch.send_keys('PORSCHE')
    srchbutton = driver.find_element(By.XPATH, '//button[@type="submit"]')
    srchbutton.click()
    element = wait.until(
        EC.presence_of_element_located((By.XPATH, '//table[@id="serverSideDataTable"]//tbody//span[text()="PORSCHE"]')))

    entries = driver.find_element(By.XPATH, '//select[@name="serverSideDataTable_length"]')
    entries.find_element(By.XPATH, '//option[@value="100"]').click()

    time.sleep(5)

    listOfRows = driver.find_elements(By.XPATH, '//table[@id="serverSideDataTable"]//tbody//tr//td[6]')
    row = 0
    models = {}
    for r in listOfRows:
        models[row] = r.text
        row += 1

    print("")
    count = Counter(models.values())
    print(count)
