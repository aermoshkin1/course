import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    # Инициализация драйвера браузера
    browser = webdriver.Chrome()
    yield browser
    # Закрытие браузера после выполнения тестов
    browser.quit()

def test_add_to_cart_button_present(browser):
    # Переход на страницу товара
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(10)
    # Проверка наличия кнопки "Добавить в корзину"
    add_to_cart_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    assert add_to_cart_button.is_displayed(), "Кнопка 'Добавить в корзину' не отображается на странице"