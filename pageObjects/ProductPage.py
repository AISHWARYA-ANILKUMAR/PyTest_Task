from selenium.webdriver.common.by import By


class ProductPage:
    color_variation_red_xpath = '//ul[@class="thwvs-wrapper-ul "]/li/span[text()="Red"]'
    orientation_variation_landscape_xpath = '//ul[@class="thwvs-wrapper-ul "]/li/span[text()="Landscape"]'
    profile_description_xpath = '//textarea[@id="profile_desc"]'
    checkbox_phone_number_xpath = '//input[@id="phone_number_checkbox"]'
    phone_number_xpath = '//input[@id="phone_number_field"]'
    id_type_dropdown_premium_xpath = '//option[text()="Premium ($50.00)"]'
    img_logo_upload_xpath = '//input[@type="file"]'
    border_dashed_xpath = '//img[@title="dashed"]'
    border_dashed_dotted_xpath = '//img[@title="dashed-dotted"]'
    add_to_cart_button_xpath = '//button[text()="Add to cart"]'
    add_to_cart_success_message_xpath = '//div[@class="woocommerce-message"]'
    phone_error_message_xpath = "//ul[@class='woocommerce-error']/li"
    border_error_message_xpath = "//ul[@class='woocommerce-error']/li"

    def __init__(self, driver):
        """
        Initializes the driver for the class
        """
        self.driver = driver

    def choose_red_color_variation(self):
        """
        Choose the color variation 'red' from the list of variations
        """
        self.driver.find_element(By.XPATH, self.color_variation_red_xpath).click()

    def choose_landscape_orientation(self):
        self.driver.find_element(By.XPATH, self.orientation_variation_landscape_xpath).click()

    def enter_profile_description(self, profile_description):
        self.driver.find_element(By.XPATH, self.profile_description_xpath).clear()
        self.driver.find_element(By.XPATH, self.profile_description_xpath).send_keys(profile_description)

    def check_phone_number_checkbox(self):
        self.driver.find_element(By.XPATH, self.checkbox_phone_number_xpath).click()

    def enter_phone_number(self, phone):
        self.driver.find_element(By.XPATH, self.phone_number_xpath).clear()
        self.driver.find_element(By.XPATH, self.phone_number_xpath).send_keys(phone)

    def choose_premium_dropdown(self):
        drop_ele = self.driver.find_element(By.XPATH, self.id_type_dropdown_premium_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", drop_ele)
        self.driver.find_element(By.XPATH, self.id_type_dropdown_premium_xpath).click()

    def upload_logo_img(self, path):
        ele = self.driver.find_element(By.XPATH, self.img_logo_upload_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ele)
        self.driver.find_element(By.XPATH, self.img_logo_upload_xpath).send_keys(path)

    def choose_border(self):
        self.driver.find_element(By.XPATH, self.border_dashed_xpath).click()
        self.driver.find_element(By.XPATH, self.border_dashed_dotted_xpath).click()

    def select_single_border(self):
        self.driver.find_element(By.XPATH, self.border_dashed_dotted_xpath).click()

    def click_add_to_cart_button(self):
        cart_ele = self.driver.find_element(By.XPATH, self.add_to_cart_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", cart_ele)
        self.driver.find_element(By.XPATH, self.add_to_cart_button_xpath).click()

    def get_add_to_cart_success_message(self):
        return self.driver.find_element(By.XPATH, self.add_to_cart_success_message_xpath).text

    def get_phone_error_message(self):
        return self.driver.find_element(By.XPATH, self.phone_error_message_xpath).text

    def get_border_error_message(self):
        return self.driver.find_element(By.XPATH, self.border_error_message_xpath).text


