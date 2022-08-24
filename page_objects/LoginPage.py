from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def username(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#email")

    def password(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#Password")

    def login_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'body app-template button.btn-primary')

    def error_message(self):
        return self.driver.find_elements(By.CSS_SELECTOR, 'body .invalid-feedback.ng-star-inserted')





