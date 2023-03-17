from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time
class Test_errorh:
    @pytest.fixture()
    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/ex_synchronization.html")
        yield driver
        driver.quit()
    def test_1(self, setup_class):
        driver.find_element(By.ID, "btn").click()
        time.sleep(5)
        try:
            driver.find_element(By.ID, "checkbox").is_displayed()
            print("Element found in the DOM")
        except NoSuchElementException:
            print("Element not found in the DOM")

    def test_2(self, setup_class):
        driver.find_element(By.ID, "btn").click()
        time.sleep(5)
        if len(driver.find_elements_by_id("checkbox")) > 0:
            print("Element exists on screen")
        else:
            print("Element does NOT exist on screen")