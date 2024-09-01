import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.ProductPage import ProductPage


class TestFieldValidationsProductPage:
    """
    The TestProductPage class is to perform product-related test cases.
    """
    baseURL = "https://woocommerce-850415-2933260.cloudwaysapps.com/product/rf-id-card"
    profile_description = "Buy Product"
    phone = "abcdefgh"
    path ="C:/Users/Aishwarya/Desktop/PyTest_Task/resources/logo.png"




    def test_validation(self, setup):
        """
        Test to perform Add to Cart Functionality
        """
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.pvObj = ProductPage(self.driver)
        self.pvObj.choose_red_color_variation()
        self.pvObj.choose_landscape_orientation()
        self.pvObj.enter_profile_description(self.profile_description)

        self.pvObj.check_phone_number_checkbox()

        self.pvObj.enter_phone_number(self.phone)
        self.pvObj.choose_premium_dropdown()
        self.pvObj.upload_logo_img(self.path)
        self.pvObj.choose_border()
        self.pvObj.click_add_to_cart_button()
        expected_error_message = "Phone Number (abcdefgh) is not a valid number."
        actual_error_message = self.pvObj.get_phone_error_message()
        assert actual_error_message == expected_error_message, f"Expected: {expected_error_message}, but got: {actual_error_message}"

        self.driver.close()
