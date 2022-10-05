import time
from source.bin.page.google_meet_page import meet_page
from source.bin.page.google_login_page import log_page

def test_first(selenium_driver):
    meet = meet_page(selenium_driver)
    log = log_page(selenium_driver)
    meet.open_google_meet()
    meet.auth()
    log.input_mail()
    log.input_pass()
    meet.go_to_meet()
    meet.confirm_meet()
    time.sleep(5600)