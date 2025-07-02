import pytest
from Base.login_page import LoginPage


@pytest.mark.usefixtures("init_driver")
class TestLogin:
    @pytest.mark.order(1)
    def test_valid_login(self, credentials):
        login_page = LoginPage(self.driver)
        login_page.login(credentials["username"], credentials["password"])
        assert login_page.is_dashboard_visible(), "Dashboard is not visible after valid login"

    @pytest.mark.order(3)
    def test_invalid_login(self, credentials):
        login_page = LoginPage(self.driver)
        login_page.invalid_login(credentials["invalid_username"], credentials["invalid_password"])
        assert login_page.is_invalid_login_error_displayed(), "valid login credentials"

    @pytest.mark.order(4)
    def test_hide_show_password(self, credentials):
        login_page = LoginPage(self.driver)
        login_page.show_hide_password_button(credentials["invalid_password"])
        assert login_page.is_password_visible(), "password not shown"

    @pytest.mark.order(2)
    def test_login_random_password(self, credentials):
        login_page = LoginPage(self.driver)
        login_page.login_with_random_password(credentials["username"], credentials["invalid_password"])
        assert login_page.is_invalid_login_error_displayed(), "random password working LogedIn"

    @pytest.mark.order(5)
    def test_forgot_password(self):
        login_page = LoginPage(self.driver)
        login_page.navigate_forget_password_page()
        assert login_page.is_forget_password_page_visible(), "Did not navigate to forget-password page"

    @pytest.mark.order(6)
    def test_login_button_disabled(self):
        login_page = LoginPage(self.driver)
        login_page.login_button_disabled()
        assert login_page.is_login_button_disabled(), "login button not disabled"
