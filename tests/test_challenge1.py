

def test_google_title(driver):
    driver.get('https://google.com')
    assert 'Google' in driver.title
