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

    def test_gestures(self):
        self.driver.find_element_by_xpath("//*[@text='Views']").click()
        self.driver.find_element_by_xpath("//*[@contentDescription='Date Widgets']").click()
        self.driver.find_element_by_xpath("//*[@text='2. Inline']").click()
        startHours =self.driver.find_element_by_xpath("//*[@contentDescription='12']")
        newHours=self.driver.find_element_by_xpath("//*[@contentDescription='9']")
        self.driver.swipe(startHours.rect["x"],startHours.rect["y"],newHours.rect["x"],newHours.rect["y"])
        time.sleep(2)


    def teardown_class(self):
        self.driver.quit()
