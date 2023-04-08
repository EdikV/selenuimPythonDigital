from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time


class Test_sauce_demo:

    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/ex_synchronization.html")


    def teardown_class(self):
        driver.quit()
