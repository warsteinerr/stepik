from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

link = 'https://suninjuly.github.io/explicit_wait2.html'
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    wait = (WebDriverWait(browser, 12).until
            (EC.text_to_be_present_in_element((By.ID, 'price'), '$100')))
    button = browser.find_element(By. ID, 'book')
    button.click()
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)
    but2 = browser.find_element(By.ID, 'solve')
    but2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(13)
    # закрываем браузер после всех манипуляций
    browser.quit()



