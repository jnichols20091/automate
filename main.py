from playwright.sync_api import sync_playwright
import time


class PlayInstance:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False, slow_mo=50, timeout=100000000)
        self.page = self.browser.new_page()


    def start_browser(self):
        self.page.goto("https://www.abbeyresidential.com/apartments/al/hoover/riverchase/contact-us")
        self.page.click("span")
        self.page.fill("#contact-resident-name-lead-form-1953415", "playwright")
        time.sleep(1000)

start = PlayInstance()
start.start_browser()