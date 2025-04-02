from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import BUNS_SECTION, SAUCES_SECTION, FILLINGS_SECTION


def test_successful_select_sauces_section(driver):
    driver.get("https://stellarburgers.nomoreparties.site")

    element = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(SAUCES_SECTION))
    assert element is not None

    driver.quit()

def test_successful_select_fillings_section(driver):
    driver.get("https://stellarburgers.nomoreparties.site")

    element = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(FILLINGS_SECTION))
    assert element is not None

    driver.quit()

def test_successful_select_buns_section(driver):
    driver.get("https://stellarburgers.nomoreparties.site")

    driver.find_element(*FILLINGS_SECTION).click()

    element = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(BUNS_SECTION))
    assert element is not None

    driver.quit()


