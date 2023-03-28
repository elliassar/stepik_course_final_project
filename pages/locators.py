from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD_1_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_2_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#register_form .btn-primary")