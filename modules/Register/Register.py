from Main import Main
from page_objects.LoginPage import LoginPage
from page_objects.RegisterPage import RegisterPage
import os
import time


class Register:
    def __init__(self, driver):
        self.driver = driver

        self.login()
        self.steps()

    def login(self):
        Main.info("Performing Login")
        time.sleep(2)
        self.driver.get(os.getenv("APP_LOGIN"))
        # Opening Login Page
        try:
            time.sleep(1)
            # Assigning positional argument
            action = LoginPage(self.driver)

            action.username().send_keys(os.getenv("EMAIL"))
            time.sleep(1)
            action.password().send_keys(os.getenv("PASSWORD"))
            time.sleep(1)
            action.login_button().click()

        except Exception as e:
            Main.error(str(e))

    def steps(self):
        action = RegisterPage(self.driver)
        Main.info("Clicking on Start Button")
        action.start().click()



case = Register
