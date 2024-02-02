from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'https://suninjuly.github.io/cats.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, 'button')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(13)
    # закрываем браузер после всех манипуляций
    browser.quit()