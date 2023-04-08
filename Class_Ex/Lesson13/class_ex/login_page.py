from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def get_username_field(self):
        return self.driver.find_element(By.XPATH, '//input[@name="username2"]')

    def get_password_field(self):
        return self.driver.find_element(By.XPATH, '//input[@name="password2"]')

    def get_button(self):
        return self.driver.find_element(By.ID, "submit")

