import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

urls = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1',
]

@pytest.mark.parametrize("url", urls)
def test_entrance(browser,url):
    browser.get(url)
    otvet = math.log(int(time.time()))
    button = browser.find_element(By.ID, 'ember33')
    button.click()
    milo = browser.find_element(By.CSS_SELECTOR, 'input[name="login"]')
    milo.send_keys('')
    passw = browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')
    passw.send_keys('')
    button1 = browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn.button_with-loader' )
    button1.click()
    time.sleep(5)
    answer = browser.find_element(By.TAG_NAME, 'textarea')
    answer.send_keys(otvet)
    button2 = browser.find_element(By. CSS_SELECTOR, 'button.submit-submission')
    button2.click()
    equality = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')
    assert "Correct!" == equality.text, f"получили {equality.text}"




