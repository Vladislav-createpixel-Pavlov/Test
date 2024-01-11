from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//div[@class='container']/form/div[@class='first_block']/div[@class='form-group first_class']/input[@class='form-control first']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//div[@class='container']/form/div[@class='first_block']/div[@class='form-group second_class']/input[@class='form-control second']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//div[@class='container']/form/div[@class='first_block']/div[@class='form-group third_class']/input[@class='form-control third']")
    input3.send_keys("smolensk@bk.uk")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()