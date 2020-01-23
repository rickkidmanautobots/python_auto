import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_copart_makes_categories(driver, wait):
    driver.get('https://copart.com')

    element = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="Serverside Quickpicks"]//div')))

    listOfMakes = driver.find_elements(By.XPATH, '//div[@ng-if="popularSearches"]//li')

    print("")
    print("List of Makes")
    for e in listOfMakes:
        print(e.text)

    listOfLinks = driver.find_elements(By.XPATH, '//div[@id="tabTrending"]/div[3]//li/a')
    count = 0
    print("")
    print("List of URLs")
    while count < len(listOfLinks):
        print(listOfLinks[count].text + " : " + listOfLinks[count].get_attribute("href"))
        count += 1
