from selenium.webdriver.common.by import By


class TestLocators:

    Profile_Button = By.XPATH, ".//p[text()='Личный Кабинет']"      # кнопка "Личный кабинет"
    New_Registration = By.XPATH, ".//a[text()='Зарегистрироваться']"        # переход "Зарегистрироваться" на старнице входа
    Registration_Name = By.XPATH, ".//input[@name='name']"      # поле "Имя" на странице регестраци и в личном кабинете
    Registration_Email = By.XPATH, ".//label[text()='Email']/following-sibling::input"      # поле "Email" на странице регистрации и входа
    Registration_Password = By.XPATH, ".//input[@name='Пароль']"        # поле "Пароль" на странице регистрации и входа
    Confirm_Registration = By.XPATH, ".//button[text()='Зарегистрироваться']"       #кнопка "Зарегистрироваться" на странице регистрации
    Confirm_Login_Button = By.XPATH, ".//button[text()='Войти']"    # кнопка "Войти" на странице входа
    Password_Error = By.XPATH, ".//p[text()='Некорректный пароль']"     # сообщение об ошибке на странице регистрации
    Main_Login_Button = By.XPATH, ".//button[text()='Войти в аккаунт']"     # кнопка "Войти в аккаунт" на главной странице
    Registration_Login_Button = By.XPATH, ".//a[text()='Войти']"        # кнопка "Войти" на странице регистрации и на странице восстановления пароля
    New_Order_Button = By.XPATH, ".//button[text()='Оформить заказ']"   # кнопка "Оформить заказ" на главной странице
    Profile_Exit = By.XPATH, ".//button[text()='Выход']"        # кнопка "Выход" в личном кабинете
    Profile_Login = By.XPATH, ".//label[text()='Логин']/following-sibling::input"       # поле "Логин" в личном кабинете
    Password_Recovery = By.XPATH, ".//a[text()='Восстановить пароль']"      # переход "Восстановить пароль" на странице входа
    Burger_Constructor = By.CLASS_NAME, "text_type_main-large"      # заголовок "Соберите бургер" на главной странице
    Constructor_Button = By.XPATH, ".//p[text()='Конструктор']"        # кнопка "Конструктор"
    Stellar_Logo = By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']/a"     # логотип "Stellar burgers"
    Filling_Button = By.XPATH, ".//span[text()='Начинки']"       # кнопка "Начинки" в шапке конструктора
    Fillings = By.XPATH, ".//h2[text()='Начинки']"      # раздел "Начинки" в поле с ингридиентами
    Last_Element = By.XPATH, ".//p[text()='Сыр с астероидной плесенью']"         # последний элемент в разделе конструктора
    Bun_Button = By.XPATH, ".//span[text()='Булки']"        # кнопка "Булки" в шапке конструктора
    Buns = By.XPATH, ".//h2[text()='Булки']"        # раздел "Булки" в поле с ингридиентами
    Sauce_Button = By.XPATH, ".//span[text()='Соусы']"      # кнопка "Соусы" в шапке конструктора
    Sauces = By.XPATH, ".//h2[text()='Соусы']"      # раздел "Соусы" в поле с ингридиентами
