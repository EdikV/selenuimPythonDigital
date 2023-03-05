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
        driver.get("https://www.wikipedia.org/")
        yield driver
        driver.quit()

    def test_find_elements(self, setup_class):
        wikilogo = driver.find_element(By.CLASS_NAME, "central-featured-logo")
        language = driver.find_element(By.ID, "searchLanguage")
        seachbar = driver.find_element(By.ID, "searchInput")
        footer = driver.find_elements(By.CLASS_NAME, "footer-sidebar-content")

        webelements = list((wikilogo, language, seachbar, footer))
        print(webelements[::-1])




        














