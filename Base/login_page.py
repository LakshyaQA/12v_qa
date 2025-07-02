import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

logging.basicConfig(level=logging.INFO)


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username = (By.ID, "mat-input-0")
        self.password = (By.ID, "mat-input-1")
        self.login_button = (By.XPATH, "//button[@aria-label='LOGIN']")
        self.hide_password_button = (By.XPATH, "//button[@aria-label='Hide password']")
        self.forget_password = (By.XPATH, "//a[contains(text(), 'forget password')]")
        self.dashboard_header = (By.XPATH, "//a[text()='i2V ITMS System']")
        self.invalid_error_message = (By.XPATH, "//div[text()='Invalid Username/ Password']")
        self.show_hide_password = (By.XPATH, "//button[@aria-label='Hide password']")
        self.show_password_button = (By.XPATH, "//button[contains(@class,'cdk-mouse-focused')]")
        self.disabled_login_button = (By.XPATH, "//button[@disabled='true']")

    def login(self, username, password):
        logging.info("Filling in login form")
        self.driver.find_element(*self.username).send_keys(username)
        time.sleep(1)
        self.driver.find_element(*self.password).send_keys(password)
        time.sleep(2)
        self.driver.find_element(*self.login_button).click()
        time.sleep(2)

    def invalid_login(self, invalid_username, invalid_password):
        logging.info("Filling in login form with invalid credentials")
        self.driver.find_element(*self.username).send_keys(invalid_username)
        time.sleep(1)
        self.driver.find_element(*self.password).send_keys(invalid_password)
        time.sleep(1)
        self.driver.find_element(*self.login_button).click()
        time.sleep(2)

    def show_hide_password_button(self, invalid_password):
        self.driver.find_element(*self.password).send_keys(invalid_password)
        time.sleep(2)
        # self.driver.find_element(*self.show_hide_password).send_keys(Keys.SPACE)
        button = self.driver.find_element(*self.show_hide_password)
        actions = ActionChains(self.driver)
        actions.click_and_hold(button).perform()
        time.sleep(2)
        actions.release().perform()
        time.sleep(2)

    def login_with_random_password(self, username, invalid_password):
        logging.info("Filling in login form with random password and admin as username")
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(invalid_password)
        self.driver.find_element(*self.login_button).click()
        time.sleep(2)

    def navigate_forget_password_page(self):
        self.driver.find_element(*self.forget_password).click()
        time.sleep(2)

    def login_button_disabled(self):
        logging.info("opening login page")
        time.sleep(1)
        self.driver.find_element(*self.disabled_login_button)

    def is_login_button_disabled(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.disabled_login_button))
            return True
        except:
            return False

    # assertions
    # def is_forget_password_page_visible(self, expected_url="http://localhost:4777/forget-password"):
    #     try:
    #         self.wait.until(EC.url_to_be(expected_url))
    #         return True
    #     except:
    #         return False

    def is_forget_password_page_visible(self, expected_url="http://localhost:4777/forget-password"):
        try:
            self.wait.until(EC.url_to_be(expected_url))
            current_url = self.driver.current_url
            return current_url == expected_url
        except Exception as e:
            print(f"[ERROR] Navigation failed. Current URL: {self.driver.current_url}, Expected: {expected_url}")
            return False

    def is_password_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.show_password_button))
            return True
        except:
            return False

    def is_invalid_login_error_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.invalid_error_message))
            return True
        except:
            return False

    def is_dashboard_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.dashboard_header))
            return True
        except:
            return False
