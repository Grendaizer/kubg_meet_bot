import time
import pyautogui
from source.bin.settings.config import URL
from selenium.webdriver.common.by import By
from source.bin.settings.config import CODE


class meet_page:
    button = '/html/body/header/div[1]/div/div[3]/div[1]/div/span[1]/a'
    code_meet = '//*[@id="i6"]'
    confirm_button = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[2]/div[2]/button/span'
    microphone = '//*[@id="ow3"]/div[1]/div/div[10]/div[3]/div[10]/div[2]/div/div[1]/div/div/span/button/div[3]/div[1]/span[2]/svg'
    video = '/html/body/div[1]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div[1]'
    connect = 'span.VfPpkd-vQzf8d:nth-child(4)'

    def __init__(self, driver):
        self.driver = driver

    def open_google_meet(self):
        self.driver.get(URL)

    def auth(self):
        button = self.driver.find_element(By.XPATH, self.button)
        button.click()

    def go_to_meet(self):
        code_input = self.driver.find_element(By.XPATH, self.code_meet)
        code_input.send_keys(CODE)
        confirm = self.driver.find_element(By.XPATH, self.confirm_button)
        confirm.click()
        time.sleep(5)

    def confirm_meet(self):
        con = self.driver.find_element(By.CSS_SELECTOR, self.connect)
        con.click()

    def write_plus_in_chat(self):
        pass

    def off_micro(self):
        pyautogui.hotkey('ctrl', 'd')
        pyautogui.hotkey('ctrl', 'e')