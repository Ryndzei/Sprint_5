from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import BUNS_SECTION, SAUCES_SECTION, FILLINGS_SECTION
from urls import BASE_URL


def test_successful_select_sauces_section(driver):
    driver.get(BASE_URL)

    element = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(SAUCES_SECTION))
    assert element is not None

def test_successful_select_fillings_section(driver):
    driver.get(BASE_URL)

    element = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(FILLINGS_SECTION))
    assert element is not None

def test_successful_select_buns_section(driver):
    driver.get(BASE_URL)

    driver.find_element(*FILLINGS_SECTION).click()

    element = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(BUNS_SECTION))
    assert element is not None
