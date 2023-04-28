from appium import webdriver
from selenium.webdriver.common.by import By
import pytest


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        username_field = self.driver.find_element(By.XPATH, "//*[@id='usernameTextField']")
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.XPATH, "//*[@id='passwordTextField']")
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(By.XPATH, "//*[@text='Login']")
        login_button.click()


class back_to_HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_logout_button(self):
        logout_button = self.driver.find_element(By.XPATH, "//*[@text='Logout']")
        logout_button.click()


class Test_EriBank:
    username = "company"
    password = "company"

    def setup_class(self):
        dc = {}
        dc['udid'] = 'R52T105JZ0E'
        dc['appPackage'] = 'com.experitest.ExperiBank'
        dc['appActivity'] = '.LoginActivity'
        dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', dc)

    def test_eri_login(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username(self.username)
        login_page.enter_password(self.password)
        login_page.click_login_button()

        home_page = back_to_HomePage(self.driver)
        home_page.click_logout_button()

    def teardown_class(self):
        self.driver.quit()
