import pytest
import random
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def new_user_data():
    new_email = "annalogunova11" + str(random.randint(100, 999)) + "@yandex.ru"
    new_user = ["Анна Логунова", new_email, 123456]
    return new_user


@pytest.fixture
def user_data():
    user = ["Анна Логунова", "annalogunova11@yandex.ru", 987654]
    return user
