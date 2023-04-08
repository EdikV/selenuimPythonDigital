import allure
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def get_username_field(self):
        return self.driver.find_element(By.ID, "user-name")

    def get_passworld_field(self):
        return self.driver.find_element(By.ID, "password")


    def get_button(self):
        return self.driver.find_element(By.ID, "login-button")

    @allure.step("Sign in using provided username and password")

    def sign_in(self, username, password):
        self.get_username_field().send_keys(username)
        self.get_passworld_field().send_keys(password)
        self.get_button().click()



