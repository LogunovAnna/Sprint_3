
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


class TestsProfile:

    def test_constructor_from_profile_successful_redirect(self, driver, user_data):
        # тест переход из личного кабинета в конструктор по клику на "Конструктор"
        # входим в личный кабинет. После клика на "Конструктор" успешно переходим на страницу, есть 'бургер' в заголовке

        driver.find_element(*TestLocators.Main_Login_Button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.Registration_Email))
        driver.find_element(*TestLocators.Registration_Email).send_keys(user_data[1])
        driver.find_element(*TestLocators.Registration_Password).send_keys(user_data[2])
        driver.find_element(*TestLocators.Confirm_Login_Button).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.Profile_Button))
        driver.find_element(*TestLocators.Profile_Button).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.Constructor_Button))
        driver.find_element(*TestLocators.Constructor_Button).click()

        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(TestLocators.Burger_Constructor))
        assert 'бургер' in driver.find_element(*TestLocators.Burger_Constructor).text

    def test_stellar_from_profile_successful_redirect(self,driver ,user_data):
        # тест перехода из личного кабинета в конструктор по клику на логотип Stellar Burgers
        # входим в личный кабинет. После клика на "Stellar Burgers" успешно переходим на страницу конструктора

        driver.find_element(*TestLocators.Profile_Button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.Registration_Email))
        driver.find_element(*TestLocators.Registration_Email).send_keys(user_data[1])
        driver.find_element(*TestLocators.Registration_Password).send_keys(user_data[2])
        driver.find_element(*TestLocators.Confirm_Login_Button).click()

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.Profile_Button))
        driver.find_element(*TestLocators.Profile_Button).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.Stellar_Logo))
        driver.find_element(*TestLocators.Stellar_Logo).click()

        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(TestLocators.New_Order_Button))
        assert 'Оформить заказ' in driver.find_element(*TestLocators.New_Order_Button).text

    def test_logout_profile_exit(self, driver, user_data):
        # тест выхода из личного кабинета
        # входим в личный кабинет. После нажатия кнопки "Выход" выполняется перенаправление на страницу входа

        driver.find_element(*TestLocators.Profile_Button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.Registration_Email))
        driver.find_element(*TestLocators.Registration_Email).send_keys(user_data[1])
        driver.find_element(*TestLocators.Registration_Password).send_keys(user_data[2])
        driver.find_element(*TestLocators.Confirm_Login_Button).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.Profile_Button))
        driver.find_element(*TestLocators.Profile_Button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.Profile_Exit))
        driver.find_element(*TestLocators.Profile_Exit).click()

        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.Confirm_Login_Button)).text == "Войти"
