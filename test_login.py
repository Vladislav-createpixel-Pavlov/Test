import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1"])

def test_guest_should_see_login_link(browser, links):
    string = str(math.log(int(time.time())))
    link = links
    #browser.implicitly_wait(30)
    
    browser.get(link)
    time.sleep(20)
    #WebDriverWait(browser, 20).until(
    #EC.visibility_of_element_located((By.CLASS_NAME,"ember-view navbar__auth navbar__auth_login st-link st-link_style_button")))
    
    #a = browser.find_element(By.,"ember-view navbar__auth navbar__auth_login st-link st-link_style_button")
    a = browser.find_element(By.ID,"ember33")
    a.click

    input1 = browser.find_element(By.ID, "id_login_email")
    input1.send_keys("alexander_0897@mail.ru")
    input2 = browser.find_element(By.ID, "id_login_password")
    input2.send_keys("Vlad06052001")
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
    
