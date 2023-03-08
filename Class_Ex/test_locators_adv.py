import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest


class Test_adv:
    @pytest.fixture()
    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/ex_locators.html")
        yield driver
        driver.quit()

    def test_find_elements(self, setup_class):
        loc_1 = driver.find_element(By.ID, "locator_id")
        loc_2 = driver.find_element(By.NAME, "locator_name")
        loc_3 = driver.find_element(By.XPATH, "//p")
        loc_4 = driver.find_element(By.CSS_SELECTOR,"div.locator_class")
        loc_5 = driver.find_element(By.LINK_TEXT, "myLocator(5)")
        loc_6 = driver.find_element(By.PARTIAL_LINK_TEXT, "(6)")
        loc_7 = driver.find_element(By.TAG_NAME, "input")
        loc_8 = driver.find_element(By.XPATH, "//button[@class='btn btn-2']")

        print(loc_1.text)
        print(loc_2.text)
        print(loc_3.text)
        print(loc_4.text)
        print(loc_5.text)
        print(loc_6.text)
        print(loc_7.text)
        print(loc_8.text)









        














