import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage


class LoginPage:
    text_box_username_xpath = '//input[@id="username"]'
    text_box_password_xpath = '//input[@id="password"]'
    text_box_login_xpath = '//button[@type="submit" and text()="Log in"]'

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.XPATH, self.text_box_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_box_username_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.text_box_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_box_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.text_box_login_xpath).click()
