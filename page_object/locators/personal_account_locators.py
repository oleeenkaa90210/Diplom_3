from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    LOGIN_TO_ACCOUNT = (By.CLASS_NAME, "button_button__33qZ0")
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".Auth_form__3qKeq.mb-20 .button_button__33qZ0")
    PERSONAL_ACCOUNT = (By.XPATH, "//nav[contains(@class, 'AppHeader_header__nav__g5hnF')]//p[contains(@class, "
                                  "'AppHeader_header__linkText__3q_va ml-2')][contains(text(), 'Личный Кабинет')]")
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[contains(@href, '/account/order-history')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']")
