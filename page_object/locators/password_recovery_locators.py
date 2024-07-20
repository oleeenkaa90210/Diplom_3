from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:

    LOGIN_TO_ACCOUNT = (By.CLASS_NAME, "button_button__33qZ0")
    PASSWORD_RECOVERY_FORM = (By.XPATH,"//div[contains(@class, 'Auth_login__3hAey')]//a[contains(@class, "
                                       "'Auth_link__1fOlj')][contains(text(), 'Восстановить пароль')]")
    EMAIL_IN_RECOVERY_FORM = (By.CSS_SELECTOR, ".Auth_login__3hAey .input_type_text input[name='name']")
    RESTORE_IN_RECOVERY_FORM = (By.CLASS_NAME, 'Auth_link__1fOlj')
    RESTORE_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    SHOW_HIDE_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".Auth_login__3hAey .input__container div div")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='Введите новый пароль']")



