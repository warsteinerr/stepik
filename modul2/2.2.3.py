from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects1.html'


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_el = browser.find_element(By.ID, 'num1')
    x =x_el.text
    y_el = browser.find_element(By.ID, 'num2')
    y = y_el.text
    z = int(x)+int(y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z))
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(13)
    # закрываем браузер после всех манипуляций
    browser.quit()

