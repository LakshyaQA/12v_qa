import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserManagement:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.settings_page = (By.XPATH, "//li[@title='Settings']")
        self.user_page = (By.XPATH, "(//div[contains(@class, 'mat-tab-labels')])//div[4]")
        self.refresh_button = (By.XPATH, "(//button[contains(@class,'mat-focus-indicator')])[1]")
        self.create_user_type_button = (By.XPATH, "(//button[contains(@class,'mat-focus-indicator')])[2]")
        self.search_icon = (By.XPATH, "(//button[contains(@class,'mat-focus-indicator')])[3]")
        self.search_box = (By.XPATH, "(//input[@id='search'])")
        self.search_result = (By.XPATH, "//span[contains(text(),'Test_user_admin')]")
        self.create_user_button = (By.XPATH, "//button[contains(@class,'mat-focus-indicator')])[4]")
        self.user_type_name = (By.XPATH, "//*[@id='typeName']")
        self.rights_dropdown = (By.XPATH, "(//span[@style='transform: rotate(0deg);'])[1]")
        self.select_deselect = (
            By.XPATH, "(//label[@class='mat-checkbox-layout']//span[@class='mat-checkbox-inner-container'])[1]")
        self.add_user_type = (By.XPATH, "(//span//mat-icon[contains(text(), 'add')])[3]")
        self.user_type_created_alert = (By.XPATH, "//div[text()='User Type Saved Successfully!!']")
        self.add_user_to_user_type = (By.XPATH, "(//span//mat-icon[contains(text(), 'add')])[2]")
        self.first_name = (By.XPATH, "//input[@id='user_first_name']")
        self.last_name = (By.XPATH, "//input[@id='user_last_name']")
        self.user_name = (By.XPATH, "//input[@id='user_name']")
        self.user_contact = (By.XPATH, "//input[@id='contact']")
        self.user_email = (By.XPATH, "//input[@id='user_email_address']")
        self.user_type_dropdown = (By.XPATH, "//mat-label[text()='User Type']/ancestor::mat-form-field")
        self.admin_select = (By.XPATH, "(//div[@id='Resource-panel']//mat-option)[3]")
        self.input_password = (By.XPATH, "(//input[@type='password'])[1]")
        self.input_confirm_password = (By.XPATH, "(//input[@type='password'])[2]")
        self.show_hide_user_password = (By.XPATH, "//button[@aria-label='Hide password']")
        self.assign_to_user = (By.XPATH, "//button//span[contains(text(),'Assign to User')]")
        self.select_devices_user = (By.XPATH, "(//span[@class='mat-checkbox-inner-container'])[1]")
        self.save_devices_button = (By.XPATH, "(//span[contains(@class, 'mat-button-wrapper')])[10]")
        self.save_user_details = (By.XPATH, "//span//mat-icon[contains(text(), 'save')]")
        self.user_saved_alert = (By.XPATH, "//div[contains(text(), 'User saved successfully')]")

    def navigate_user_page(self):
        self.driver.find_element(*self.settings_page).click()
        time.sleep(1)
        self.driver.find_element(*self.user_page).click()
        time.sleep(3)

    def create_user_type(self, user_type):
        self.driver.find_element(*self.create_user_type_button).click()
        time.sleep(4)
        self.driver.find_element(*self.user_type_name).click()
        time.sleep(2)
        self.driver.find_element(*self.user_type_name).send_keys(user_type)
        time.sleep(2)
        self.driver.find_element(*self.rights_dropdown).click()
        time.sleep(2)
        self.driver.find_element(*self.select_deselect).click()
        time.sleep(2)
        self.driver.find_element(*self.add_user_type).click()
        time.sleep(2)

    def add_user(self, first_name, last_name, user_username, user_email, user_contact, user_pass, user_confirm_pass):
        self.driver.find_element(*self.add_user_to_user_type).click()
        time.sleep(1)
        self.driver.find_element(*self.first_name).send_keys(first_name)
        time.sleep(1)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        time.sleep(1)
        self.driver.find_element(*self.user_name).send_keys(user_username)
        time.sleep(2)
        self.driver.find_element(*self.user_email).send_keys(user_email)
        time.sleep(1)
        self.driver.find_element(*self.user_contact).send_keys(user_contact)
        time.sleep(3)
        self.driver.find_element(*self.user_type_dropdown).click()
        time.sleep(1)
        self.driver.find_element(*self.admin_select).click()
        time.sleep(1)
        self.driver.find_element(*self.input_password).send_keys(user_pass)
        time.sleep(1)
        self.driver.find_element(*self.input_confirm_password).send_keys(user_confirm_pass)
        time.sleep(1)
        self.driver.find_element(*self.show_hide_user_password).click()
        time.sleep(1)
        self.driver.find_element(*self.assign_to_user).click()
        time.sleep(1)
        self.driver.find_element(*self.select_devices_user).click()
        time.sleep(1)
        self.driver.find_element(*self.save_devices_button).click()
        time.sleep(2)
        self.driver.find_element(*self.save_user_details).click()
        time.sleep(2)

    def refresh_user_type_list(self):
        self.driver.find_element(*self.refresh_button).click()
        time.sleep(4)

    def search_user_type(self, user_type):
        self.driver.find_element(*self.search_icon).click()
        time.sleep(2)
        self.driver.find_element(*self.search_box).send_keys(user_type)
        time.sleep(2)

    def is_search_result_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.search_result))
            return True
        except:
            return False

    def is_refresh_button_clicked(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.refresh_button))
            return True
        except:
            return False

    def is_user_saved(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.user_saved_alert))
            return True
        except:
            return False

    def is_user_type_created(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.user_type_created_alert))
            return True
        except:
            return False
