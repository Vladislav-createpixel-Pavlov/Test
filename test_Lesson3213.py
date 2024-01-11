from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestForm(unittest.TestCase):
    def test_Form1(self):
        link ="http://suninjuly.github.io/registration1.html"
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
        congratulation = browser.find_element(By.TAG_NAME,"h1")
        self.assertEqual(congratulation.text, 'Congratulations! You have successfully registered!',
                         "button_click_error")
    def test_Form2(self):
        link ="http://suninjuly.github.io/registration2.html"
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
        congratulation = browser.find_element(By.TAG_NAME,"h1")
        self.assertEqual(congratulation.text, 'Congratulations! You have successfully registered!',
                         "button_click_error")
if __name__ == "__main__":
    unittest.main()