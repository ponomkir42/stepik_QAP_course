from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    browser.find_element(By.ID, 'book').click()
    x = int(browser.find_element(By.ID, 'input_value').text)
    result = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(result)
    browser.find_element(By.ID, 'solve').click()
    alert = browser.switch_to.alert
    print(alert.text)
finally:
    time.sleep(5)
    browser.quit()
