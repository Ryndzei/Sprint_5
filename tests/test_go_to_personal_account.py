from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from urls import BASE_URL
from test_data import *
from locators import (
    LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT,
    LOGIN_BUTTON, LOGIN_ACCOUNT_BUTTON,
    PERSONAL_CABINET_LINK, LOGOUT_BUTTON
)


def test_successfully_went_to_personal_account(driver):
    driver.get(BASE_URL)

    driver.find_element(*LOGIN_ACCOUNT_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(VALID_LOGIN)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(VALID_PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PERSONAL_CABINET_LINK))

    driver.find_element(*PERSONAL_CABINET_LINK).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LOGOUT_BUTTON))

    assert "profile" in driver.current_url