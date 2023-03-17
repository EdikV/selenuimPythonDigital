import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import xml.etree.ElementTree as ET


def get_data(node_name):
    root = ET.parse('./data.xml').getroot()
    browser_type = root.find('browser').text
    weight = root.find('Weight').text
    height = root.find('Height')
    return browser_type, weight, height

