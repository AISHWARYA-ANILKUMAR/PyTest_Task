from selenium.webdriver.common.by import By


class LoginPage:

    text_box_username_xpath = '//input[@id="username"]'
    text_box_password_xpath = '//input[@id="password"]'
    text_box_login_xpath = '//button[@type="submit" and text()="Log in"]'

    def __init__(self, driver):
        """
       initializes the driver for the class
        """
        self.driver = driver

    def set_username(self, username):
        """
        Enters the username into the username input field
        """
        self.driver.find_element(By.XPATH, self.text_box_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_box_username_xpath).send_keys(username)

    def set_password(self, password):
        """
        Enters the password into the password input field
        """
        self.driver.find_element(By.XPATH, self.text_box_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_box_password_xpath).send_keys(password)

    def click_login(self):
        """
        Clicks the login button on the login page
        """
        self.driver.find_element(By.XPATH, self.text_box_login_xpath).click()
