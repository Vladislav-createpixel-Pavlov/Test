from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time 

link ="http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    browser.execute_script("window.scrollBy(0, 100);")

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    option1.click()
    option2 = browser.find_element(By.ID, "robotCheckbox")
    option2.click()


    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
    
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла