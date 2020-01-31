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

    # Print out all models and totals per model
    listOfRows = driver.find_elements(By.XPATH, '//table[@id="serverSideDataTable"]//tbody//tr//td[6]')
    row = 0
    models = {}
    for r in listOfRows:
        models[row] = r.text
        row += 1

    print("")
    count = Counter(models.values())
    print(count)

    # Print out a list of damages and totals per type of damage
    class Counters:
        rear = 0
        front = 0
        scratch = 0
        under = 0
        misc = 0

    listofDamages = driver.find_elements(By.XPATH, '//table[@id="serverSideDataTable"]//tbody//tr//td[12]')

    def rearend():
        Counters.rear += 1
        return

    def frontend():
        Counters.front += 1
        return

    def minor():
        Counters.scratch += 1
        return

    def undercarriage():
        Counters.under += 1
        return

    def default():
        Counters.misc += 1
        return

    switcher = {
        "REAR END": rearend,
        "FRONT END": frontend,
        "MINOR DENT/SCRATCHES": minor,
        "UNDERCARRIAGE": undercarriage
    }

    def switch(damage):
        return switcher.get(damage, default)()

    for d in listofDamages:
        switch(d.text)

    print("REAR END : " + str(Counters.rear))
    print("FRONT END : " + str(Counters.front))
    print("MINOR DENT/SCRATCHES : " + str(Counters.scratch))
    print("UNDERCARRIAGE : " + str(Counters.under))
    print("MISC : " + str(Counters.misc))