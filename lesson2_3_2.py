from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary")
    button.click()

    browser.switch_to.window(browser.window_handles[1])

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    x_value = calc(x)

    input_b = browser.find_element(By.ID, "answer")
    input_b.send_keys(x_value)

    button2 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button2.click()

    print(browser.switch_to.alert.text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()