import time

from appium import webdriver
from selenium.webdriver.common.by import By


class Test_API_app:
    global driver
    def setup_class(self):
        dc = {}
        dc['udid'] = 'R52T105JZ0E'
        dc['appPackage'] = 'com.example.android.apis'
        dc['appActivity'] = '.ApiDemos'
        dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', dc)

    def test_01_list(self):
        elements = self.driver.find_elements(By.XPATH, '//*[@id="text1"]')
        count = len(elements)

        assert count == 11

        for i in elements:
            print(i.text)

    def teardown_class(self):
        self.driver.quit()
