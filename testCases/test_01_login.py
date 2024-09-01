import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage


class TestLogin:
    """
    The Test001Login class is to perform login-related testcases
    """
    baseURL = "https://woocommerce-850415-2933260.cloudwaysapps.com/my-account"
    username = "test_customer"
    password = "password"

    def test_homepage_title(self, setup):
        """
         Test to verify the title of the homepage
        """

        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        self.driver.close()
        if actual_title == "My account – woocommerce-850415-2933260.cloudwaysapps.com":
            assert True
        else:
            assert False

    def test_login(self, setup):
        """
        Test to perform login functionality.
        """
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lpObj = LoginPage(self.driver)
        self.lpObj.set_username(self.username)
        time.sleep(2)
        self.lpObj.set_password(self.password)
        time.sleep(2)
        self.lpObj.click_login()
        time.sleep(2)

        log_title = self.driver.title
        self.driver.close()
        if log_title == "My account – woocommerce-850415-2933260.cloudwaysapps.com":
            assert True
        else:
            assert False








