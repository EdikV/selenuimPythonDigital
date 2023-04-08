import allure
import pytest
from Class_Ex.Lesson13.class_ex.login_page import LoginPage
from Class_Ex.Lesson13.class_ex.driver import get_driver

@allure.feature('Login')
class TestLoginPage:
    def setup_method(self):
        self.driver = get_driver()
        self.driver.get('https://atidcollege.co.il/Xamples/webdriveradvance.html')
        self.login_page = LoginPage(self.driver)

    @allure.story('Successful login')
    def test_successful_login(self):
        self.login_page.get_username_field().send_keys('selenium')
        self.login_page.get_password_field().send_keys('webdriver')
        self.login_page.get_button().click()
        assert self.driver.current_url == 'https://atidcollege.co.il/Xamples/webdriveradvance2.html'

@pytest.fixture(scope='class')
def test_teardown():
    yield
    from teardown import TestTeardown
    TestTeardown.driver = get_driver()

class TestLoginPageTeardown:
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
