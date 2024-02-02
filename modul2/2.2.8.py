from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    name.send_keys('yo')
    surname = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    surname.send_keys('yo')
    input1 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input1.send_keys('yo')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test1.txt')  # добавляем к этому пути имя файла
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(13)
    # закрываем браузер после всех манипуляций
    browser.quit()