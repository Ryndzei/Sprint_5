from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from urls import BASE_URL
from test_data import *
from locators import (
    LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT,
    LOGIN_BUTTON, LOGIN_ACCOUNT_BUTTON,
    PERSONAL_CABINET_LINK, LOGOUT_BUTTON,
    CONSTRUCTOR_LINK, LOGO_LINK
)


def test_successfully_went_to_main_page_by_clicking_constructor(driver):
    driver.get(BASE_URL)

    driver.find_element(*LOGIN_ACCOUNT_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(VALID_LOGIN)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(VALID_PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PERSONAL_CABINET_LINK))

    driver.find_element(*PERSONAL_CABINET_LINK).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LOGOUT_BUTTON))

    driver.find_element(*CONSTRUCTOR_LINK).click()

    assert driver.current_url == BASE_URL

def test_successfully_went_to_main_page_by_clicking_logo(driver):
    driver.get(BASE_URL)

    driver.find_element(*LOGIN_ACCOUNT_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(VALID_LOGIN)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(VALID_PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PERSONAL_CABINET_LINK))

    driver.find_element(*PERSONAL_CABINET_LINK).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LOGOUT_BUTTON))

    driver.find_element(*LOGO_LINK).click()

    assert driver.current_url == BASE_URL