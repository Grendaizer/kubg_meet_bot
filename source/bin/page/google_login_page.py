import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from source.bin.settings.config import EMAIL, PASS


class log_page:
    mail = '//*[@id="identifierId"]'
    pasword = '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input'

    def __init__(self, driver):
        self.driver = driver

    def input_mail(self):
        a = self.driver.find_element(By.XPATH, self.mail)
        a.send_keys(EMAIL)
        a.send_keys(Keys.ENTER)
        time.sleep(1)

    def input_pass(self):
        b = self.driver.find_element(By.XPATH, self.pasword)
        b.send_keys(PASS)
        b.send_keys(Keys.ENTER)
        time.sleep(3)