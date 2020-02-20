import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_copart_skyline(driver, wait):
    driver.get('https://copart.com')
    model = "SKYLINE"
    element = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="Serverside Quickpicks"]//div')))
    srch = driver.find_element(By.ID, 'input-search')
    srch.send_keys('NISSAN')
    srchbutton = driver.find_element(By.XPATH, '//button[@type="submit"]')
    srchbutton.click()
    element = wait.until(
        EC.presence_of_element_located((By.XPATH, '//table[@id="serverSideDataTable"]//tbody//span[text()="NISSAN"]')))
    srch = driver.find_element(By.XPATH, '//div[@id="serverSideDataTable_filter"]//input')
    srch.send_keys(model)
    time.sleep(3)
    chkbox = driver.find_elements(By.XPATH, '//table[@id="serverSideDataTable"]//input')
    count = 1
    try:
        while True:
            chkbox[count].click()
            count += 1
    except BaseException as error:
        driver.save_screenshot("copart_listing_failure.png")
        print("")
        print("The number of " + model + " listings is : " + str(count-1))
        print("Picture was taken for trying to click checkbox " + str(count) + " which doesn't exist!")
        raise error
