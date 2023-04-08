class TestTeardown:
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
