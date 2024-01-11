import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def test_button(browser):

    
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    time.sleep(4)
    assert button, 'the button is not founded'