from page_object.data import Urls
from page_object.locators.personal_account_locators import PersonalAccountLocators
from page_object.pages.base_page import BasePage


class PersonalAccountPage(BasePage):

    def click_on_login_to_account(self):
        self.click_to_element(PersonalAccountLocators.LOGIN_TO_ACCOUNT)

    def add_email(self):
        self.add_text_to_element(PersonalAccountLocators.EMAIL_INPUT, 'zxcvbnm@ya.ru')

    def add_password(self):
        self.add_text_to_element(PersonalAccountLocators.PASSWORD_INPUT, 'zxcvbnm')

    def click_to_login_button(self):
        self.click_to_element(PersonalAccountLocators.LOGIN_BUTTON)

    def click_to_personal_account(self):
        self.click_to_element(PersonalAccountLocators.PERSONAL_ACCOUNT)

    def wait_personal_profile_page(self):
        self.wait_new_url(Urls.PERSONAL_ACCOUNT_PROFILE_PAGE)

    def click_to_order_history_button(self):
        self.click_to_element(PersonalAccountLocators.ORDER_HISTORY_BUTTON)

    def wait_order_history_page(self):
        self.wait_new_url(Urls.ORDER_HISTORY_PAGE)

    def click_to_logout_button(self):
        self.click_to_element(PersonalAccountLocators.LOGOUT_BUTTON)

    def wait_login_page(self):
        self.wait_new_url(Urls.LOGIN_PAGE)