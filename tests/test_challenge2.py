# import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_copart_porche(driver, wait):
    # time.sleep(10)
    driver.get('https://copart.com')
    element = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="Serverside Quickpicks"]//div')))
    srch = driver.find_element(By.ID, 'input-search')
    srch.send_keys('Exotics')
    srchbutton = driver.find_element(By.XPATH, '//button[@type="submit"]')
    srchbutton.click()
    element = wait.until(
        EC.presence_of_element_located((By.XPATH, '//table[@id="serverSideDataTable"]//tbody//span[text()="PORSCHE"]')))

    assert 'PORSCHE' in driver.find_element(By.XPATH, '//span[text()="PORSCHE"]').text
