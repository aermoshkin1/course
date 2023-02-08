from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button1 = browser.find_element(By.CSS_SELECTOR, '#book')
    button1.click()

    chislo1 = browser.find_element(By.ID, 'input_value') #input_value
    x = chislo1.text
    x = calc(x)
    element = browser.find_element(By.CSS_SELECTOR, '#answer')
    element.send_keys(x)
    button3 = browser.find_element(By.CSS_SELECTOR, "#solve")
    button3.click()


finally:
    time.sleep(5)
    browser.quit()