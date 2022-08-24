from Main import Main
from page_objects.LoginPage import LoginPage
import os
import time


class Login:
    def __init__(self, driver):
        self.driver = driver

        self.neg_case_1()
        self.neg_case_2()
        self.neg_case_3()
        self.neg_case_4()
        self.neg_case_5()
        self.pos_case_1()


    def neg_case_1(self):
        Main.info("Performing the Negative Test Case #1")
        Main.info("Login with Empty Fields")
        time.sleep(2)
        self.driver.get(os.getenv("APP_LOGIN"))
        # Opening Login Page
        try:
            time.sleep(1)
            # Assigning positional argument
            action = LoginPage(self.driver)
            time.sleep(1)
            action.login_button().click()

            # handling error message
            if action.error_message():
                for message in action.error_message():
                    Main.info(message.text)
            Main.info("Negative Test Case #1 Performed Successfully")

        except Exception as e:
            Main.error(str(e))

    def neg_case_2(self):
        Main.info("Performing the Negative Test Case #2")
        Main.info("Submitting form by providing only Username ")
        time.sleep(2)
        self.driver.get(os.getenv("APP_LOGIN"))
        # Opening Login Page
        try:
            time.sleep(1)
            # Assigning positional argument
            action = LoginPage(self.driver)

            action.username().send_keys(os.getenv("EMAIL"))
            time.sleep(1)
            action.login_button().click()

            # handling error message
            if action.error_message():
                for message in action.error_message():
                    Main.info(message.text)
            Main.info("NegativeTest Case #2 Performed Successfully")
        except Exception as e:
            Main.error(str(e))


    def neg_case_3(self):
        Main.info("Performing the Negative Test Case #3")
        Main.info("Submitting form by providing only Password")
        time.sleep(2)
        self.driver.get(os.getenv("APP_LOGIN"))
        # Opening Login Page
        try:
            time.sleep(1)
            # Assigning positional argument
            action = LoginPage(self.driver)

            action.password().send_keys(os.getenv("PASSWORD"))
            time.sleep(1)
            action.login_button().click()

            # Handling error message
            if action.error_message():
                for message in action.error_message():
                    Main.info(message.text)
            Main.info("Negative Test Case #3 Performed Successfully")
        except Exception as e:
            Main.error(str(e))

    def neg_case_4(self):
        Main.info("Performing the Negative Test Case #4")
        Main.info("Proving Password in Username & Password in Password Field")
        time.sleep(2)
        self.driver.get(os.getenv("APP_LOGIN"))
        # Opening Login Page
        try:
            time.sleep(1)
            # Assigning positional argument
            action = LoginPage(self.driver)

            action.username().send_keys(os.getenv("PASSWORD"))
            time.sleep(1)
            action.password().send_keys(os.getenv("PASSWORD"))
            time.sleep(1)
            action.login_button().click()

            # Handling error message
            if action.error_message():
                for message in action.error_message():
                    Main.info(message.text)
                Main.info("Negative Test Case #4 Performed Successfully")
        except Exception as e:
            Main.error(str(e))

    def neg_case_5(self):
        Main.info("Performing the Negative Test Case #5")
        Main.info("Proving Username in Username & Username in Password Field")
        time.sleep(2)
        self.driver.get(os.getenv("APP_LOGIN"))
        # Opening Login Page
        try:
            time.sleep(1)
            # Assigning positional argument
            action = LoginPage(self.driver)

            action.username().send_keys(os.getenv("EMAIL"))
            time.sleep(1)
            action.password().send_keys(os.getenv("EMAIL"))
            time.sleep(1)
            action.login_button().click()

            # Handling error message
            if action.error_message():
                for message in action.error_message():
                    Main.info(message.text)
                Main.info("Negative Test Case #5 Performed Successfully")
        except Exception as e:
            Main.error(str(e))

    def pos_case_1(self):
        Main.info("Performing the Positive Test Case #1")
        Main.info("Proving Username in Username & Password in Password Field")
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


case = Login
