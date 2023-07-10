from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


class TestsRegistration:

    def test_registration_new_login_successful_registration(self, new_user_data, driver):
        # тест регистрации по кнопке "Зарегистрироваться" на странице входа в личный кабинет
        # после ввода данных успешно регистрируемся и переходим на страницу входа

        driver.find_element(*TestLocators.Profile_Button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.New_Registration))
        driver.find_element(*TestLocators.New_Registration).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.Registration_Name))
        driver.find_element(*TestLocators.Registration_Name).send_keys(new_user_data[0])
        driver.find_element(*TestLocators.Registration_Email).send_keys(new_user_data[1])
        driver.find_element(*TestLocators.Registration_Password).send_keys(new_user_data[2])
        driver.find_element(*TestLocators.Confirm_Registration).click()

        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.Confirm_Login_Button)).text == "Войти"

    def test_registration_empty_password_show_error(self, new_user_data, driver):
        # негативный тест регистрации по кнопке "Зарегистрироваться" на странице входа в личный кабинет
        # после ввода некорректного пароля появляется сообщение об ошибке

        driver.find_element(*TestLocators.Profile_Button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.New_Registration))
        driver.find_element(*TestLocators.New_Registration).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.Registration_Name))
        driver.find_element(*TestLocators.Registration_Name).send_keys(new_user_data[0])
        driver.find_element(*TestLocators.Registration_Email).send_keys(new_user_data[1])
        driver.find_element(*TestLocators.Registration_Password).send_keys(" ")
        driver.find_element(*TestLocators.Confirm_Registration).click()

        assert driver.find_element(*TestLocators.Password_Error).text == 'Некорректный пароль'


class TestsLogin:
    def test_login_main_page_select_successful_login(self, user_data, driver):
        # тест входа в личный кабинет по кнопке "Войти в аккаунт" на главной странице
        # вводим данные. Переходим в личный кабинет по кнопке для проверки успешного входа

        driver.find_element(*TestLocators.Main_Login_Button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.Registration_Email))
        driver.find_element(*TestLocators.Registration_Email).send_keys(user_data[1])
        driver.find_element(*TestLocators.Registration_Password).send_keys(user_data[2])
        driver.find_element(*TestLocators.Confirm_Login_Button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.Profile_Button))
        driver.find_element(*TestLocators.Profile_Button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.Profile_Login))

        value_name = driver.find_element(*TestLocators.Profile_Login).get_attribute('value')
        assert user_data[1] in value_name

    def test_login_profile_button_successful_login(self, driver, user_data):
        # тест входа в личный кабинет по кнопке "Личный кабинет"
        # вводим данные. После успешного входа перенаправляемся на гравную страницу

        driver.find_element(*TestLocators.Profile_Button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.Registration_Email))
        driver.find_element(*TestLocators.Registration_Email).send_keys(user_data[1])
        driver.find_element(*TestLocators.Registration_Password).send_keys(user_data[2])
        driver.find_element(*TestLocators.Confirm_Login_Button).click()

        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(TestLocators.New_Order_Button))
        assert (driver.current_url == "https://stellarburgers.nomoreparties.site/") and ('Оформить заказ' in driver.find_element(*TestLocators.New_Order_Button).text)

    def test_login_registration_form_successful_login(self, driver, user_data):
        # тест входа в личный кабинет по кнопке "Войти" в форме регистарции
        # вводим данные. После успешного входа проверяем, что мы на гравной странице. Доступна кнопка "Оформить заказ"
        driver.find_element(*TestLocators.Profile_Button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.New_Registration))
        driver.find_element(*TestLocators.New_Registration).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.Registration_Login_Button))
        driver.find_element(*TestLocators.Registration_Login_Button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.Registration_Email))
        driver.find_element(*TestLocators.Registration_Email).send_keys(user_data[1])
        driver.find_element(*TestLocators.Registration_Password).send_keys(user_data[2])
        driver.find_element(*TestLocators.Confirm_Login_Button).click()

        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(TestLocators.New_Order_Button))
        assert 'Оформить заказ' in driver.find_element(*TestLocators.New_Order_Button).text

    def test_login_password_recovery_successful_login(self, driver, user_data):
        # тест входа в личный кабинет по кнопке "Войти" в форме восстановления пароля
        # вводим данные. После успешного входа проверяем, что мы на главной странице, есть 'бургер' в заголовке

        driver.find_element(*TestLocators.Profile_Button).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.Password_Recovery))
        driver.find_element(*TestLocators.Password_Recovery).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(TestLocators.Registration_Login_Button))
        driver.find_element(*TestLocators.Registration_Login_Button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.Registration_Email))
        driver.find_element(*TestLocators.Registration_Email).send_keys(user_data[1])
        driver.find_element(*TestLocators.Registration_Password).send_keys(user_data[2])
        driver.find_element(*TestLocators.Confirm_Login_Button).click()

        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(TestLocators.Burger_Constructor))
        assert 'бургер' in driver.find_element(*TestLocators.Burger_Constructor).text
