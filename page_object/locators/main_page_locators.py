from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTION = (By.XPATH,
                    "//nav[contains(@class, 'AppHeader_header__nav__g5hnF')]//p[contains(@class, "
                    "'AppHeader_header__linkText__3q_va ml-2')][contains(text(), 'Конструктор')]")
    ORDER_FEED = (By.XPATH, "//a[contains(@href, '/feed')]")
    SPICY_X_SAUCE = (By.XPATH, "//p[text()='Соус Spicy-X']/ancestor::a")
    BUN_UNGREDIENT = (By.CSS_SELECTOR, '.BurgerIngredient_ingredient__text__yp3dH')
    MODAL_CLOSE_BUTTON = (By.CLASS_NAME, "Modal_modal__close_modified__3V5XS")
    MODAL_OPENED = (By.CLASS_NAME, "Modal_modal_opened__3ISw4")
    MODAL_CONTAINER = (By.CLASS_NAME, "Modal_modal__container__Wo2l_")
    TARGET_FIELD_TOP = (By.CSS_SELECTOR, ".BurgerConstructor_basket__list__l9dp_")
    COUNTER = (By.CSS_SELECTOR, ".counter_default__28sqi")
    PARENT = (By.XPATH, '..')
    ORDER_BUTTON = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx"
                                     ".button_button_size_large__G21Vg")
    MODAL_ORDER = (By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4")
    ORDER_NUMBER = (By.CLASS_NAME, 'Modal_modal__title__2L34m')



