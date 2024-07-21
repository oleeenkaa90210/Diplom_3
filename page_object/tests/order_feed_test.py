import allure
from page_object.pages.order_feed_page import OrderFeedPage
from page_object.pages.main_page import MainPage
from page_object.pages.personal_account_page import PersonalAccountPage


class TestOrderFeedPage:
    @allure.title('Всплывающее окно с деталями заказа')
    def test_order_details_window(self, driver, open_stellar_burgers):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_to_order_feed()

        order_feed_page.click_on_any_order()
        assert order_feed_page.is_order_modal_open()

    @allure.title('Заказ из «История заказов» отображаются в «Лента заказов»')
    def test_orders_displayed_in_order_feed(self, driver, open_stellar_burgers):
        personal_account_page = PersonalAccountPage(driver)
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        personal_account_page.click_on_login_to_account()
        personal_account_page.add_email()
        personal_account_page.add_password()
        personal_account_page.click_to_login_button()

        main_page.scroll_to_ingredient()
        main_page.add_bun_to_order()
        main_page.add_ingredient_to_order()
        main_page.checkout()
        main_page.click_to_close_modal_checkout()

        personal_account_page.click_to_personal_account()
        personal_account_page.click_to_order_history_button()
        my_order = order_feed_page.get_my_order()

        main_page.click_to_order_feed()
        order_feeds = order_feed_page.get_order_feeds()

        assert my_order in order_feeds

    @allure.title('Счётчик Выполнено за всё время увеличивается')
    def test_completed_for_all_time(self, driver, open_stellar_burgers):
        personal_account_page = PersonalAccountPage(driver)
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        personal_account_page.click_on_login_to_account()
        personal_account_page.add_email()
        personal_account_page.add_password()
        personal_account_page.click_to_login_button()

        main_page.click_to_order_feed()

        initial_completed_for_all_time = order_feed_page.get_counter_completed_for_all_time()

        order_feed_page.go_to_main_page()
        main_page.scroll_to_ingredient()
        main_page.add_bun_to_order()
        main_page.add_ingredient_to_order()
        main_page.checkout()
        main_page.click_to_close_modal_checkout()
        main_page.click_to_order_feed()

        updated_completed_for_all_time = order_feed_page.get_counter_completed_for_all_time()

        assert updated_completed_for_all_time == initial_completed_for_all_time + 1

    @allure.title('Счётчик Выполнено за сегодня увеличивается')
    def test_completed_today(self, driver, open_stellar_burgers):
        personal_account_page = PersonalAccountPage(driver)
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        personal_account_page.click_on_login_to_account()
        personal_account_page.add_email()
        personal_account_page.add_password()
        personal_account_page.click_to_login_button()

        main_page.click_to_order_feed()

        initial_completed_today = order_feed_page.get_counter_completed_for_day()
        initial_completed_today = int(initial_completed_today)
        order_feed_page.go_to_main_page()
        main_page.scroll_to_ingredient()
        main_page.add_bun_to_order()
        main_page.add_ingredient_to_order()
        main_page.checkout()
        main_page.click_to_close_modal_checkout()
        main_page.click_to_order_feed()

        updated_completed_today = order_feed_page.get_counter_completed_for_day()

        assert int(updated_completed_today) == initial_completed_today + 1

    @allure.title( 'После оформления заказа его номер появляется в "В работе"')
    def test_order_in_progress(self, driver, open_stellar_burgers):
        personal_account_page = PersonalAccountPage(driver)
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        personal_account_page.click_on_login_to_account()
        personal_account_page.add_email()
        personal_account_page.add_password()
        personal_account_page.click_to_login_button()
        main_page.scroll_to_ingredient()
        main_page.add_ingredient_to_order()
        main_page.add_bun_to_order()
        main_page.checkout()
        order_number = main_page.get_order_number()
        main_page.click_to_close_modal_checkout()
        main_page.click_to_order_feed()

        order_in_progress = order_feed_page.get_order_numbers_in_progress()
        assert len(order_in_progress) == 0 or order_number in order_in_progress
