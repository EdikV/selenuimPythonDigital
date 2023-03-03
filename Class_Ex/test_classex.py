import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture()
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()

def test_atid_store(browser):
    browser.get("https://atid.store")

    store_menu_link = browser.find_element_by_css_selector("li[id='menu-item-45'] a[class='menu-link']")
    store_menu_link.click()

    sort_by_dropdown = browser.find_element_by_xpath("//select[@name='orderby']")

    options = sort_by_dropdown.find_elements_by_tag_name("option")
    fifth_option = options[4]
    fifth_option.click()

    time.sleep(5)

    search_box = browser.find_element(By.ID, "wc-block-search__input-1").send_keys("Buddha Bracelet")
    search_box = browser.find_element(By.CLASS_NAME, "wc-block-product-search__button").click()

    time.sleep(15)

   











