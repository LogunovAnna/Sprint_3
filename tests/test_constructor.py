
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


class TestLoginRegistration:

    def test_constructor_bun_scroll_to_bun(self):
        # тест раздела конструктор переход к разделу Булки
        # чтобы заметить изменения переходим к последнему элементу конструктора. Сравниваем координату 'y' до и после нажатия кнопки
        driver = webdriver.Chrome()
        driver.set_window_size(691, 990)
        driver.get("https://stellarburgers.nomoreparties.site/")

        last_element = driver.find_element(*TestLocators.Last_Element)
        driver.execute_script("arguments[0].scrollIntoView();", last_element)
        position_before = driver.find_element(*TestLocators.Buns).rect

        driver.find_element(*TestLocators.Bun_Button).click()
        WebDriverWait(driver, 5)
        position_later = driver.find_element(*TestLocators.Buns).rect
        assert position_later['y'] > position_before['y']

        driver.quit()

    def test_constructor_sauce_scroll_to_sauce(self):
        # тест раздела конструктор переход к разделу Соусы
        # сравниваем координату 'y' до и после нажатия кнопки
        driver = webdriver.Chrome()
        driver.set_window_size(691, 990)
        driver.get("https://stellarburgers.nomoreparties.site/")

        position_before = driver.find_element(*TestLocators.Sauces).rect
        driver.find_element(*TestLocators.Sauce_Button).click()

        WebDriverWait(driver, 5)
        position_later = driver.find_element(*TestLocators.Sauces).rect
        assert position_later['y'] < position_before['y']

        driver.quit()

    def test_constructor_filling_scroll_to_filling(self):
        # тест раздела конструктор переход к разделу Начинки
        # сравниваем координату 'y' до и после нажатия кнопки
        driver = webdriver.Chrome()
        driver.set_window_size(691, 990)
        driver.get("https://stellarburgers.nomoreparties.site/")

        position_before = driver.find_element(*TestLocators.Fillings).rect
        driver.find_element(*TestLocators.Filling_Button).click()

        WebDriverWait(driver, 5)
        position_later = driver.find_element(*TestLocators.Fillings).rect
        assert position_later['y'] < position_before['y']

        driver.quit()
