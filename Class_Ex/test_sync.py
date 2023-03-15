from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time




class Test_nav:
    @pytest.fixture()
    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/ex_synchronization.html")
        yield driver
        driver.quit()


        #implict wait
    def test_3rd_button(self, setup_class):
        driver.find_element(By.ID, "btn").click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//p[@id='message']").is_displayed()


    def test_2nd_button(self,setup_class):
        driver.find_element(By.ID, "hidden").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//div[@id='loading1']").is_displayed()


    def test_1st_button(self, setup_class):
        driver.find_element(By.ID, "rendered").click()
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "finish2"))).text
        assert element == "My Rendered Element After Fact!"





















