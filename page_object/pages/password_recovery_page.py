from page_object.data import Urls
from page_object.locators.password_recovery_locators import PasswordRecoveryLocators
from page_object.pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):

    def click_on_login_to_account(self):
        self.click_to_element(PasswordRecoveryLocators.LOGIN_TO_ACCOUNT)

    def click_on_restore_password(self):
        self.click_to_element(PasswordRecoveryLocators.PASSWORD_RECOVERY_FORM)

    def wait_for_forgot_page(self):
        self.wait_new_url(Urls.FORGOT_PASSWORD_PAGE)

    def wait_reset_password_page(self):
        self.wait_new_url(Urls.RESET_PASSWORD_PAGE)

    def add_email(self):
        self.add_text_to_element(PasswordRecoveryLocators.EMAIL_IN_RECOVERY_FORM, 'zxcvbnm@ya.ru')

    def click_on_restore_button(self):
        self.click_to_element(PasswordRecoveryLocators.RESTORE_BUTTON)

    def add_password_on_reset_page(self):
        self.add_text_to_element(PasswordRecoveryLocators.PASSWORD_FIELD, 'example_password')

    def click_to_show_hide_button(self):
        self.click_to_element(PasswordRecoveryLocators.SHOW_HIDE_PASSWORD_BUTTON)

    def is_password_visible(self):
        password_field = self.driver.find_element(*PasswordRecoveryLocators.PASSWORD_FIELD)
        return password_field.get_attribute("type") == "text"






