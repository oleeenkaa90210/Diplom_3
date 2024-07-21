from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_FEED = (By.XPATH, "//a[contains(@href, '/feed')]")
    ORDER_ITEM = (By.CSS_SELECTOR, '.OrderHistory_listItem__2x95r')
    MODAL_OPENED = (By.CSS_SELECTOR, '.Modal_modal_opened__3ISw4.Modal_modal__P3_V5')
    ORDER_ITEMS = (By.CSS_SELECTOR, '.OrderHistory_textBox__3lgbs .text_type_digits-default')
    ORDER_HISTORY = (By.CSS_SELECTOR, '.OrderHistory_orderHistory__qy1VB')
    ORDER_FEEDS = (By.CSS_SELECTOR, '.OrderFeed_contentBox__3-tWb')
    COUNTER_COMPLETED = (By.CSS_SELECTOR, '.OrderFeed_number__2MbrQ')
    CONSTRUCTION = (By.XPATH,
                    "//nav[contains(@class, 'AppHeader_header__nav__g5hnF')]//p[contains(@class, "
                    "'AppHeader_header__linkText__3q_va ml-2')][contains(text(), 'Конструктор')]")
    TEXT_COUNTER_FOR_DAY = (By.XPATH, "//p[contains(@class, 'text_type_main-medium') and text()='Выполнено за "
                                      "сегодня:']")
    ORDER_IN_PROGRESS = (By.CSS_SELECTOR, '.OrderFeed_orderListReady__1YFem.OrderFeed_orderList__cBvyi li')
    CLASS_MODAL_OPENED = 'Modal_modal_opened__3ISw4'
    ORDERS_NUMBERS = (By.CSS_SELECTOR, 'li.OrderHistory_listItem__2x95r')



