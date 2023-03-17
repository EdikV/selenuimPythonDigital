import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import xml.etree.ElementTree as ET

XML_DATA_PATH = './data.xml'


class Test_bmi:
    def get_data(self, datapath):
        root = ET.parse(XML_DATA_PATH).getroot()
        return root.find(".//"+datapath).text

browser_type = ge('browser').text
weight = root.find('Weight').text
height = root.find('Height').text
url = root.find('URL').text
return browser_type, weight, height, url


browser_type, weight, height, url = Test_bmi.get_data(XML_DATA_PATH)


@pytest.fixture
def init_driver(browser_type):
    if browser_type == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_type == 'firefox':
        driver = webdriver.Chrome(ChromeDriverManager().install())
