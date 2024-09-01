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
    phone = "9876543210"
    path = "C:/Users/Aishwarya/Desktop/PyTest_Task/resources/logo.png"

    def test_min_border_requirement(self, setup):
        """
        Test to perform Add to Cart Functionality
        """
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.pbObj = ProductPage(self.driver)
        self.pbObj.choose_red_color_variation()
        self.pbObj.choose_landscape_orientation()
        self.pbObj.enter_profile_description(self.profile_description)

        self.pbObj.check_phone_number_checkbox()

        self.pbObj.enter_phone_number(self.phone)
        self.pbObj.choose_premium_dropdown()
        self.pbObj.upload_logo_img(self.path)
        self.pbObj.select_single_border()
        self.pbObj.click_add_to_cart_button()
        expected_error_message = "Border: Make at least 2 selections."
        actual_error_message = self.pbObj.get_border_error_message()
        assert actual_error_message == expected_error_message, f"Expected: {expected_error_message}, but got: {actual_error_message}"

        self.driver.close()
