from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import NAME_INPUT, EMAIL_INPUT, PASSWORD_INPUT, REGISTER_BUTTON, PASSWORD_ERROR, LOGIN_BUTTON
from generators import random_login, random_password


def test_successful_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(*NAME_INPUT).send_keys("Anton")
    driver.find_element(*EMAIL_INPUT).send_keys(random_login())
    driver.find_element(*PASSWORD_INPUT).send_keys(random_password())
    driver.find_element(*REGISTER_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LOGIN_BUTTON))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    driver.quit()

def test_unsuccessful_registration_invalid_password(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(*NAME_INPUT).send_keys("Anton")
    driver.find_element(*EMAIL_INPUT).send_keys(random_login())
    driver.find_element(*PASSWORD_INPUT).send_keys("12345")
    driver.find_element(*REGISTER_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PASSWORD_ERROR))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/register"

    driver.quit()
