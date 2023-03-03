import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()


def test_bmi_site(browser):

    expected_result = "32"

    browser.get("https://atidcollege.co.il/Xamples/bmi/")

    browser.find_element(By.XPATH, "//input[@id='weight']").send_keys('110')
#    time.sleep(15)

    browser.find_element(By.XPATH, "//input[@id='hight']").send_keys('187')

 #   time.sleep(15)

    browser.find_element(By.XPATH, "//input[@id='calculate_data']").click()

 #   time.sleep(15)

    bmi_result = browser.find_element(By.ID, "bmi_result").get_attribute("value")
    assert expected_result == bmi_result, f" the BMI IS In-CORRECT"









