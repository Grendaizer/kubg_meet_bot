import time
from source.bin.page.google_meet_page import meet_page
from source.bin.page.google_login_page import log_page

def test_first(selenium_driver):
    meet = meet_page(selenium_driver)
    log = log_page(selenium_driver)
    meet.open_google_meet()
    time.sleep(1)
    meet.auth()
    time.sleep(1)
    log.input_mail()
    time.sleep(1)
    log.input_pass()
    time.sleep(1)
    meet.go_to_meet()
    time.sleep(10)
    meet.confirm_meet()
    time.sleep(1)
    meet.off_micro()
    time.sleep(10)