from selenium import webdriver, common
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select, Select
import time
import re
import random
import string


def rantext():
    text = re.compile(r'[^a-zA-Z0-9]')
    text = string.ascii_lowercase
    result_text = ''.join(random.choice(string.ascii_lowercase) for i in range(6,45))
    return result_text


driver = webdriver.Firefox()
driver.get("https://www.abbeyresidential.com/apartments/al/hoover/riverchase/contact-us")
time.sleep(5)
poploc = driver.find_element(By.CSS_SELECTOR, ".close-btn")
ActionChains(driver).move_to_element(poploc).click(poploc).perform()
time.sleep(2)
fillna = driver.find_element(By.CSS_SELECTOR, "#contact-resident-name-lead-form-1953415")
ActionChains(driver).move_to_element(fillna).click(fillna).perform()
ActionChains(driver).send_keys(rantext()).perform()
poploc1 = driver.find_element(By.CSS_SELECTOR, "#contact-resident-p-g5-resident-2-lead-form-1953415")
ActionChains(driver).move_to_element(poploc1).click(poploc1).perform()
ActionChains(driver).send_keys(rantext()).perform()