import allure
from page_object.data import Urls
from page_object.pages.main_page import MainPage
from page_object.pages.personal_account_page import PersonalAccountPage


class TestMainPage:

    @allure.title('Переход по клику на «Конструктор»')
    def test_go_to_construction(self, driver, open_stellar_burgers):
        main_page = MainPage(driver)
        main_page.click_to_order_feed()
        main_page.click_on_construction()

        current_url = driver.current_url
        assert current_url == Urls.SERVER_URL

    @allure.title('Переход по клику на «Лента заказов»')
    def test_go_to_order_feed(self, driver, open_stellar_burgers):
        main_page = MainPage(driver)
        main_page.click_to_order_feed()

        current_url = driver.current_url
        assert current_url == Urls.ORDER_FEED_PAGE

    @allure.title('Всплывающее окно с деталями ингредиента')
    def test_modal_ingredient(self, driver, open_stellar_burgers):
        main_page = MainPage(driver)
        main_page.scroll_to_ingredient()
        main_page.click_to_ingredient()

        assert main_page.is_modal_opened()

    @allure.title('Закрытие всплывающего окна с деталями')
    def test_close_modal_ingredient(self, driver, open_stellar_burgers):
        main_page = MainPage(driver)
        main_page.scroll_to_ingredient()
        main_page.click_to_ingredient()
        main_page.click_to_close_modal()

        assert main_page.is_modal_closed()

    @allure.title('Увеличение каунтера ингредиента')
    def test_ingredient_counter_changes(self, driver, open_stellar_burgers):
        main_page = MainPage(driver)
        main_page.scroll_to_ingredient()
        initial_count = main_page.get_ingredient_count()
        assert initial_count == 0
        main_page.add_ingredient_to_order()
        new_count = main_page.get_ingredient_count()
        assert new_count == 1

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_logged_in_user_can_place_order(self, driver, open_stellar_burgers):
        personal_account_page = PersonalAccountPage(driver)
        main_page = MainPage(driver)
        personal_account_page.click_on_login_to_account()
        personal_account_page.add_email()
        personal_account_page.add_password()
        personal_account_page.click_to_login_button()
        main_page.scroll_to_ingredient()
        main_page.add_ingredient_to_order()
        main_page.add_bun_to_order()
        main_page.checkout()

        assert main_page.verify_order_modal()





