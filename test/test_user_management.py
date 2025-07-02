import logging

import pytest
from Base.user_management import UserManagement
from Base.login_page import LoginPage


@pytest.mark.usefixtures("init_driver")
class TestUsermanagement:
    @pytest.mark.order(4)
    def test_create_user_type(self, credentials):
        login_page = LoginPage(self.driver)
        login_page.login(credentials["username"], credentials["password"])
        user_management = UserManagement(self.driver)
        user_management.navigate_user_page()
        user_management.create_user_type(credentials["user_type"])
        assert user_management.is_user_type_created(), "User type not created"

    @pytest.mark.order(3)
    def test_create_user(self, credentials):
        login_page = LoginPage(self.driver)
        login_page.login(credentials["username"], credentials["password"])
        user_management = UserManagement(self.driver)
        user_management.navigate_user_page()
        user_management.add_user(credentials["first_name"], credentials["last_name"], credentials["user_username"],
                                 credentials["user_contact"],
                                 credentials["user_email"], credentials["user_pass"],
                                 credentials["user_confirm_pass"])
        assert user_management.is_user_saved(), "User not created"

    @pytest.mark.order(2)
    def test_refresh_button(self, credentials):
        login_page = LoginPage(self.driver)
        login_page.login(credentials["username"], credentials["password"])
        user_management = UserManagement(self.driver)
        user_management.navigate_user_page()
        user_management.refresh_user_type_list()
        assert user_management.is_refresh_button_clicked(), "Refresh button not working"

    @pytest.mark.order(1)
    def test_search_button(self, credentials):
        login_page = LoginPage(self.driver)
        login_page.login(credentials["username"], credentials["password"])
        user_management = UserManagement(self.driver)
        user_management.navigate_user_page()
        user_management.search_user_type(credentials["user_type"])
        assert user_management.is_search_result_visible, "Search button not working"
