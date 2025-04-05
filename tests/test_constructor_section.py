from locators import BUNS_SECTION, SAUCES_SECTION, FILLINGS_SECTION
from urls import BASE_URL


def test_successful_select_sauces_section(driver):
    driver.get(BASE_URL)

    driver.find_element(*SAUCES_SECTION).click()

    assert "tab_tab_type_current__2BEPc" in driver.find_element(*SAUCES_SECTION).get_attribute("class")

def test_successful_select_fillings_section(driver):
    driver.get(BASE_URL)

    driver.find_element(*FILLINGS_SECTION).click()

    assert "tab_tab_type_current__2BEPc" in driver.find_element(*FILLINGS_SECTION).get_attribute("class")

def test_successful_select_buns_section(driver):
    driver.get(BASE_URL)

    driver.find_element(*FILLINGS_SECTION).click()
    driver.find_element(*BUNS_SECTION).click()

    assert "tab_tab_type_current__2BEPc" in driver.find_element(*BUNS_SECTION).get_attribute("class")