from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time 

link ="http://suninjuly.github.io/selects1.html"

def calc(x,y):
  return str(int(x)+int(y))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text

    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text
    z = calc(x,y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(z) # ищем элемент с текстом "Python"
    
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла