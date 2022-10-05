import pytest
from selenium import webdriver


@pytest.fixture(autouse=False, scope='function')
def selenium_driver():
    profile = webdriver.FirefoxProfile()
    profile.set_preference('media.navigator.permission.disabled', True)
    profile.update_preferences()
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.implicitly_wait(time_to_wait=10)
    yield driver
    driver.quit()
