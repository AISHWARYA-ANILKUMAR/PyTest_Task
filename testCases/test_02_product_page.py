import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.ProductPage import ProductPage


class TestProductPage:
    """
    The TestProductPage class is to perform product-related test cases.
    """
    baseURL = "https://woocommerce-850415-2933260.cloudwaysapps.com/product/rf-id-card"
    profile_description = "Buy Product"
    phone = "9876543210"
    path ="C:/Users/Aishwarya/Desktop/PyTest_Task/resources/logo.png"

    def test_product_page_title(self, setup):
        """
        Test to verify the title of the product page
        """
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        self.driver.close()
        assert actual_title == "RF ID Card – woocommerce-850415-2933260.cloudwaysapps.com"

    def test_add_to_cart(self, setup):
        """
        Test to perform Add to Cart Functionality
        """
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.ppObj = ProductPage(self.driver)
        self.ppObj.choose_red_color_variation()
        self.ppObj.choose_landscape_orientation()
        self.ppObj.enter_profile_description(self.profile_description)
        self.ppObj.check_phone_number_checkbox()
        self.ppObj.enter_phone_number(self.phone)
        self.ppObj.choose_premium_dropdown()
        self.ppObj.upload_logo_img(self.path)
        self.ppObj.choose_border()
        self.ppObj.click_add_to_cart_button()

        expected_message = '“RF ID Card” has been added to your cart.'
        actual_message = self.ppObj.get_add_to_cart_success_message()
        assert expected_message in actual_message, f"Expected: {expected_message}, but got: {actual_message}"
        self.driver.close()

