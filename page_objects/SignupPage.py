from selenium.webdriver.common.by import By


class SignupPage:
    def __init__(self, driver):
        self.driver = driver

    def username(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#name')

    def email(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#email")

    def password(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#password")

    def signup_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'form button.btn-primary')

    def error_message(self):
        return self.driver.find_elements(By.CSS_SELECTOR, 'div.invalid-feedback.ng-star-inserted')


