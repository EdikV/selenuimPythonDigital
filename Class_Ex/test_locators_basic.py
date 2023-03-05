import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest


class Test_ex10:
    @pytest.fixture()
    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://selenium.dev")
        yield driver
        driver.quit()

    def test_find_elements(self, setup_class):
        by_id = driver.find_element(By.ID, "Layer_1")
        by_name = driver.find_element(By.CLASS_NAME, "navbar-logo")
        by_tag = driver.find_element(By.TAG_NAME, "svg")
        links = driver.find_elements(By.TAG_NAME, "a")
        text = driver.find_elements(By.PARTIAL_LINK_TEXT, "Selenium")

        print("The Elements by Id =", by_id)
        print("The Elements by name =", by_name)
        print("The Elements by tag =", by_tag)
        print("The number of links on the webpage are : ", str(len(links)))
        print("The number of links having the name selenium are", str(len(text)))
















