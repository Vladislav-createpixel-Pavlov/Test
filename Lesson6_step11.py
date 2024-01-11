from selenium import webdriver
from selenium.webdriver.common.by import By

import time 

link = "http://suninjuly.github.io/registration2.html"
#link ="http://suninjuly.github.io/registration1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CLASS_NAME, "form-control.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.third")
    input3.send_keys("alexander@mail.ru")
    input4 = browser.find_element(By.XPATH,"//input[@placeholder='Input your phone:']")
    input4.send_keys("+123")
    input5 = browser.find_element(By.XPATH,"//input[@placeholder='Input your address:']")
    input5.send_keys("volga")
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла