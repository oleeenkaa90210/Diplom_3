import allure
from page_object.data import Urls
from page_object.pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:
    @allure.title('Переход по клику на «Личный кабинет»')
    def test_go_to_personal_account(self, driver, open_stellar_burgers):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_on_login_to_account()
        personal_account_page.add_email()
        personal_account_page.add_password()
        personal_account_page.click_to_login_button()
        personal_account_page.click_to_personal_account()
        personal_account_page.wait_personal_profile_page()

        current_url = driver.current_url
        assert current_url == Urls.PERSONAL_ACCOUNT_PROFILE_PAGE

    @allure.title('Переход в раздел «История заказов»')
    def test_go_to_order_history(self, driver, open_stellar_burgers):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_on_login_to_account()
        personal_account_page.add_email()
        personal_account_page.add_password()
        personal_account_page.click_to_login_button()
        personal_account_page.click_to_personal_account()
        personal_account_page.wait_personal_profile_page()
        personal_account_page.click_to_order_history_button()
        personal_account_page.wait_order_history_page()

        current_url = driver.current_url
        assert current_url == Urls.ORDER_HISTORY_PAGE

    @allure.title('Выход из аккаунта')
    def test_logout_from_personal_account(self, driver, open_stellar_burgers):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_on_login_to_account()
        personal_account_page.add_email()
        personal_account_page.add_password()
        personal_account_page.click_to_login_button()
        personal_account_page.click_to_personal_account()
        personal_account_page.wait_personal_profile_page()
        personal_account_page.click_to_logout_button()
        personal_account_page.wait_login_page()

        current_url = driver.current_url
        assert current_url == Urls.LOGIN_PAGE








