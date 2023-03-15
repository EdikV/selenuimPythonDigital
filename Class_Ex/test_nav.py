from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest


class Test_nav:
    @pytest.fixture()
    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/ex_switch_navigation.html")
        yield driver
        driver.quit()
    def test_verify_alert(self, setup_class):
        driver.find_element(By.ID, "btnAlert").click()
        alert = driver.switch_to.alert
        alert.accept()
        output = "Alert is gone."
        assert output == driver.find_element_by_id("output").text



    def test_show_prompt(self, setup_class):
        driver.find_element(By.ID, "btnPrompt").click()
        prompt = driver.switch_to.alert
        text = prompt.text
        print("This is the original text", text)
        prompt.send_keys("Edward")
        print("The new prompt is:", prompt.text)
        prompt.accept()
        output = "Edward"
        assert output == driver.find_element_by_id("output").text