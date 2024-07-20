import allure
from page_object.data import Urls
from page_object.pages.password_recovery_page import PasswordRecoveryPage


class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_switch_to_page_recovery(self, driver, open_stellar_burgers):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.click_on_login_to_account()
        password_recovery_page.click_on_restore_password()
        password_recovery_page.wait_for_forgot_page()

        current_url = driver.current_url
        assert current_url == Urls.FORGOT_PASSWORD_PAGE, f"Expected URL to be '{Urls.FORGOT_PASSWORD_PAGE}' but got {current_url}"

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_and_click_to_recover(self, driver, open_stellar_burgers):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.click_on_login_to_account()
        password_recovery_page.click_on_restore_password()
        password_recovery_page.wait_for_forgot_page()
        password_recovery_page.add_email()
        password_recovery_page.click_on_restore_button()
        password_recovery_page.wait_reset_password_page()

        current_url = driver.current_url
        assert current_url == Urls.RESET_PASSWORD_PAGE, f"Expected URL to be '{Urls.RESET_PASSWORD_PAGE}' but got {current_url}"

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным')
    def test_show_hide_password_field_activation(self, driver, open_stellar_burgers):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.click_on_login_to_account()
        password_recovery_page.click_on_restore_password()
        password_recovery_page.wait_for_forgot_page()
        password_recovery_page.add_email()
        password_recovery_page.click_on_restore_button()
        password_recovery_page.wait_reset_password_page()
        password_recovery_page.add_password_on_reset_page()
        password_recovery_page.click_to_show_hide_button()

        assert password_recovery_page.is_password_visible()


