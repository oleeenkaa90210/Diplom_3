import time
from page_object.data import Urls
from page_object.locators.main_page_locators import MainPageLocators
from page_object.locators.personal_account_locators import PersonalAccountLocators
from page_object.pages.base_page import BasePage
from selenium.webdriver import ActionChains


class MainPage(BasePage):

    def click_on_construction(self):
        self.click_to_element(MainPageLocators.CONSTRUCTION)
        self.wait_new_url(Urls.SERVER_URL)

    def click_to_order_feed(self):
        self.click_to_element(MainPageLocators.ORDER_FEED)
        self.wait_new_url(Urls.ORDER_FEED_PAGE)

    def click_to_ingredient(self):
        self.click_to_element(MainPageLocators.SPICY_X_SAUCE)
        self.find_element_with_wait(MainPageLocators.MODAL_CONTAINER)

    def scroll_to_ingredient(self):
        self.scroll_to_element(MainPageLocators.SPICY_X_SAUCE)

    def click_to_close_modal(self):
        self.click_to_element(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_new_url(Urls.MODAL_SPICY_X_SAUCE)

    def click_to_close_modal_checkout(self):
        self.click_to_element(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_new_url(Urls.SERVER_URL)

    def is_modal_opened(self):
        modal_opened = self.driver.find_element(*MainPageLocators.MODAL_OPENED)
        return modal_opened.is_displayed()

    def is_modal_closed(self):
        modal_closed = self.driver.find_elements(*MainPageLocators.MODAL_OPENED)
        return len(modal_closed) == 0

    def add_ingredient_to_order(self):
        ingredient = self.driver.find_element(*MainPageLocators.SPICY_X_SAUCE)
        target = self.driver.find_element(*MainPageLocators.TARGET_FIELD_TOP)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, target).perform()

    def add_bun_to_order(self):
        ingredient = self.driver.find_element(*MainPageLocators.BUN_UNGREDIENT)
        target = self.driver.find_element(*MainPageLocators.TARGET_FIELD_TOP)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, target).perform()

    def get_ingredient_count(self):
        spicy = self.driver.find_element(*MainPageLocators.SPICY_X_SAUCE)
        spicy_parent = spicy.find_element(*MainPageLocators.PARENT)
        count_element = spicy_parent.find_element(*MainPageLocators.COUNTER)
        return int(count_element.text)

    def get_order_number(self):
        order_number = self.get_text_from_element(MainPageLocators.ORDER_NUMBER)
        if order_number == "9999":
            time.sleep(5)
            order_number = self.get_text_from_element(
                MainPageLocators.ORDER_NUMBER)
        return order_number

    def checkout(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON)
        self.find_element_with_wait(MainPageLocators.MODAL_ORDER)

    def verify_order_modal(self):
        modal = self.driver.find_element(*MainPageLocators.MODAL_ORDER)
        order_id = modal.find_element(*MainPageLocators.ORDER_NUMBER)
        return order_id.is_displayed()
