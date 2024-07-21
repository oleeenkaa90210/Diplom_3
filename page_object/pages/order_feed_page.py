from selenium.webdriver.common.by import By
from page_object.data import Urls
from page_object.locators.main_page_locators import MainPageLocators
from page_object.locators.order_feed_locators import OrderFeedLocators
from page_object.pages.base_page import BasePage


class OrderFeedPage(BasePage):

    def click_to_order_feed(self):
        self.click_to_element(OrderFeedLocators.ORDER_FEED)
        self.wait_new_url(Urls.ORDER_FEED_PAGE)

    def click_on_any_order(self):
        self.click_to_element(OrderFeedLocators.ORDER_ITEM)

    def is_order_modal_open(self):
        element = self.find_element_with_wait(OrderFeedLocators.MODAL_OPENED)
        has_class = OrderFeedLocators.CLASS_MODAL_OPENED in element.get_attribute('class')
        return has_class

    def get_my_order(self):
        order_texts = self.extract_order_texts(OrderFeedLocators.ORDER_HISTORY, OrderFeedLocators.ORDER_ITEMS)
        return order_texts[-1]

    def get_order_feeds(self):
        return self.extract_order_texts(OrderFeedLocators.ORDER_FEEDS, OrderFeedLocators.ORDER_ITEMS)

    def extract_order_texts(self, container_selector, item_selector):
        order_texts = []
        container = self.find_element_with_wait(container_selector)
        items = container.find_elements(*OrderFeedLocators.ORDERS_NUMBERS)
        for item in items:
            text_element = item.find_element(*item_selector)
            order_texts.append(text_element.text)
        return order_texts

    def get_counter_completed_for_all_time(self):
        total_orders_count = self.get_text_from_element(OrderFeedLocators.COUNTER_COMPLETED)
        return int(total_orders_count)

    def go_to_main_page(self):
        self.click_to_element(OrderFeedLocators.CONSTRUCTION)
        self.wait_new_url(Urls.SERVER_URL)

    def get_counter_completed_for_day(self):
        counter = self.find_element_with_wait(OrderFeedLocators.TEXT_COUNTER_FOR_DAY)
        parent_counter = counter.find_element(*MainPageLocators.PARENT)
        order_feed_number_element = parent_counter.find_element(*OrderFeedLocators.COUNTER_COMPLETED)

        return order_feed_number_element.text

    def get_order_numbers_in_progress(self):
        order_numbers_in_progress = []
        elements = self.find_elements_with_wait(OrderFeedLocators.ORDER_IN_PROGRESS)
        for el in elements:
            if not "Все текущие заказы готовы!" in el.text:
                order_numbers_in_progress.append(el.text)

        return order_numbers_in_progress


