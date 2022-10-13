import time
from base.data_page import BasePage

def test(driver):
    page = BasePage(driver, "https://www.youtube.com/")
    page.open()
    time.sleep(15)