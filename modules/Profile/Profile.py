from Main import Main
from page_objects.LoginPage import LoginPage
from page_objects.ProfilePage import ProfilePage
from selenium.webdriver.common.keys import Keys
import os
import time


class Profile:
    def __init__(self, driver):
        self.driver = driver

        self.login()
        self.profile()

    def login(self):
        Main.info("Performing Login")
        time.sleep(2)
        self.driver.get(os.getenv("APP_LOGIN"))
        # Opening Login Page
        try:
            time.sleep(1)
            # Assigning positional argument
            action = LoginPage(self.driver)

            action.username().send_keys(os.getenv("USR_EMAIL"))
            time.sleep(1)
            action.password().send_keys(os.getenv("USR_PASS"))
            time.sleep(1)
            action.login_button().click()
            time.sleep(3)

        except Exception as e:
            Main.error(str(e))

    def profile(self):
        self.driver.implicitly_wait(10)
        action = ProfilePage(self.driver)
        time.sleep(5)
        Main.info("Clicking on Complete Profile Button")
        action.get_hired().click()

        time.sleep(2)
        Main.info("Selecting Radio Button I want to Teach")
        action.teach().click()
        action.charges_pm().click()

        time.sleep(2)
        scroll = action.add_timing()
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", scroll)

        time.sleep(2)
        Main.info("Selecting Class Per Week = 2")
        action.class_pw().click()

        time.sleep(2)
        Main.info("Selecting Class Charges/Month = 30")
        action.charges_pm().click()
        time.sleep(1)
        action.charges_pm().click()
        time.sleep(1)
        action.charges_pm().click()
        time.sleep(1)
        action.charges_pm().click()
        time.sleep(1)

        time.sleep(2)
        Main.info("Selecting Class Duration/Minute = 45")
        action.class_duration().click()
        time.sleep(1)
        action.class_duration().click()

        time.sleep(2)
        Main.info("Selecting Class Covered/Subjects = 45")
        action.subjects().click()
        time.sleep(1)
        action.subjects().send_keys("hifz")
        time.sleep(1)
        action.subjects().send_keys(Keys.RETURN)


        time.sleep(2)
        Main.info("Adding New Package")
        action.add_package().click()

        time.sleep(2)
        Main.info("Removing New Package")
        action.remove_package().click()

        time.sleep(2)
        scroll = action.day_7()
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", scroll)

        time.sleep(2)
        Main.info("Adding Time Slot")
        action.add_timing().click()

        time.sleep(2)
        Main.info("Removing Time Slot")
        action.remove_timing().click()

        time.sleep(2)
        Main.info("Adding Day 2 as Monday")
        action.day_2().click()


        time.sleep(2)
        scroll = action.submit()
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", scroll)

        time.sleep(2)
        Main.info("Selecting Class Duration = 45 Mins")
        time.sleep(1)
        action.cls_duration().click()
        time.sleep(1)
        action.cls_duration().click()

        time.sleep(2)
        Main.info("Providing Value for IBAN Number")
        action.iban().click()
        action.iban().send_keys("0000864890")

        time.sleep(2)
        Main.info("Providing Value for Account Number")
        action.account().click()
        action.account().send_keys("Qari Tester")

        time.sleep(2)
        Main.info("Providing Value for Billing Address")
        action.billing().click()
        action.billing().send_keys("PECHS Block 2 Karachi")


case = Profile
