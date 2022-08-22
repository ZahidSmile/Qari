from Main import Main
import time
import os
from page_objects.SignupPage import SignupPage

class SignUp:
    def __init__(self, driver):
        self.driver = driver
        self.Register()

    def Register(self):

        # Assigning positional argument
        action = SignupPage(self.driver)

        # performing click on Username Field

        action.username().click()

        Main.info("Clicked Username Field")

        action.username().send_keys(os.getenv("USER"))

        time.sleep(2)
        # performing click on Email field

        action.email().click()

        Main.info("Clicked on Email Field")

        time.sleep(2)
        action.email().send_keys(os.getenv("EMAIL"))

        time.sleep(2)
        # performing click on password field

        action.password().click()

        Main.info("Clicked on Password Field")

        action.password().send_keys(os.getenv("PASSWORD"))

        time.sleep(2)
        # performing click on Sign Up Button

        action.signup_button().click()

        Main.info("Clicked on Sign Up button")


signup = SignUp
