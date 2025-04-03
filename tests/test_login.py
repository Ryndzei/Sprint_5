from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from urls import BASE_URL, REGISTER_URL, PASS_FORGOT_URL
from locators import *


def test_successful_login_from_main_page(driver):
    driver.get(BASE_URL)

    driver.find_element(*LOGIN_ACCOUNT_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("antonrineyskiy1939@yandex.ru")
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PERSONAL_CABINET_LINK))

    driver.find_element(*PERSONAL_CABINET_LINK).click()

    assert "account" in driver.current_url

def test_successful_login_from_personal_cabinet(driver):
    driver.get(BASE_URL)

    driver.find_element(*PERSONAL_CABINET_LINK).click()
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("antonrineyskiy1939@yandex.ru")
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PERSONAL_CABINET_LINK))

    driver.find_element(*PERSONAL_CABINET_LINK).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LOGOUT_BUTTON))

    assert "account" in driver.current_url

def test_successful_login_from_registration_form(driver):
    driver.get(REGISTER_URL)

    driver.find_element(*LOGIN_FROM_REGISTER).click()
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("antonrineyskiy1939@yandex.ru")
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PERSONAL_CABINET_LINK))

    driver.find_element(*PERSONAL_CABINET_LINK).click()

    assert "account" in driver.current_url

def test_successful_login_from_password_recovery_form(driver):
    driver.get(PASS_FORGOT_URL)

    driver.find_element(*LOGIN_FROM_RECOVERY).click()
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("antonrineyskiy1939@yandex.ru")
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PERSONAL_CABINET_LINK))

    driver.find_element(*PERSONAL_CABINET_LINK).click()

    assert "account" in driver.current_url