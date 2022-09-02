from Main import Main
from page_objects.LoginPage import LoginPage
from page_objects.RegisterPage import RegisterPage
from selenium.webdriver.common.keys import Keys
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
            time.sleep(3)

        except Exception as e:
            Main.error(str(e))

    def steps(self):
        self.driver.implicitly_wait(10)
        action = RegisterPage(self.driver)

        step_1 = action.step_1()
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", step_1)
        time.sleep(2)
        action.step_1().click()
        time.sleep(3)

        Main.info("Clicking on Start Button")
        action.start().click()

        time.sleep(2)
        Main.info("Clicking on Upload Profile Field")
        try:
            if action.profile_exist():
                action.profile_exist().click()
        except Exception as e:
            Main.error(str(e))
        time.sleep(3)
        action.profile().send_keys(os.getcwd() + '\image.jpg')

        time.sleep(2)
        Main.info("Clicking on Country Field")
        action.country().click()
        time.sleep(1)
        action.country().send_keys('Pakistan')
        action.country().send_keys(Keys.RETURN)

        time.sleep(2)
        Main.info("Clicking on State Field")
        action.state().click()
        time.sleep(1)
        action.state().send_keys('Sindh')
        action.state().send_keys(Keys.RETURN)

        time.sleep(2)
        Main.info("Clicking on City Field")
        action.city().click()
        time.sleep(1)
        action.city().send_keys('Karachi')
        action.city().send_keys(Keys.RETURN)

        time.sleep(2)
        Main.info("Clicking on Address Field")
        action.address().clear()
        time.sleep(2)
        action.address().click()
        action.address().send_keys('PECHS')

        section = action.step_3()
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", section)

        time.sleep(2)
        Main.info("Clicking on Gender Field")
        action.gender().click()

        time.sleep(2)
        Main.info("Clicking on Language Field")
        try:
            if action.ex_lang():
                action.ex_lang().click()
        except Exception as e:
            Main.error(str(e))
        time.sleep(2)
        action.language().click()
        action.language().send_keys('Urdu')
        action.language().send_keys(Keys.RETURN)

        time.sleep(2)
        Main.info("Clicking on About Me Field")
        action.about().clear()
        time.sleep(2)
        action.about().click()
        action.about().send_keys("There is no one who loves pain itself, who seeks after it and wants to have it, simply because it is pain...")

        time.sleep(2)
        Main.info("Clicking on Save & Proceed to Step 3")
        action.step_2().click()

        self.driver.implicitly_wait(10)
        Main.info("Clicking on Qualification Field")
        try:
            if action.ex_qualf():
                action.ex_qualf().click()
        except Exception as e:
            Main.error(str(e))
        time.sleep(2)
        action.qualifications().click()
        action.qualifications().send_keys('Other')
        action.qualifications().send_keys(Keys.RETURN)

        time.sleep(3)
        Main.info("Clicking on Add Photo Field")
        try:
            if action.certificate_exist():
                action.certificate_exist().click()
        except Exception as e:
            Main.error(str(e))
        time.sleep(2)
        action.certificate().send_keys(os.getcwd() + '\certificate.jpg')

        time.sleep(3)
        Main.info("Clicking on Experience Title")
        action.ex_title().clear()
        time.sleep(2)
        action.ex_title().click()
        action.ex_title().send_keys('Senior Qari')

        time.sleep(3)
        Main.info("Clicking on Start Date")
        action.from_date().click()
        action.from_date().send_keys(Keys.ARROW_LEFT)
        action.from_date().send_keys(Keys.ARROW_LEFT)
        action.from_date().send_keys('10')
        action.from_date().send_keys('09')
        action.from_date().send_keys('10092006')

        time.sleep(3)
        Main.info("Clicking on End Date")
        action.to_date().click()
        action.from_date().send_keys(Keys.ARROW_LEFT)
        action.from_date().send_keys(Keys.ARROW_LEFT)
        action.to_date().send_keys('10')
        action.to_date().send_keys('09')
        action.to_date().send_keys('2010')

        time.sleep(3)
        Main.info("Clicking on End Date")
        action.exp_details().clear()
        time.sleep(2)
        action.exp_details().click()
        action.exp_details().send_keys('Share some more details about your roles and responsibilities in this job')

        time.sleep(3)
        Main.info("Clicking on Save & Proceed Step 4")
        action.step_3().click()

        step_4 = action.step_4()
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", step_4)

        self.driver.implicitly_wait(10)
        Main.info("Clicking on Video Link 1")
        action.video_1().clear()
        time.sleep(2)
        action.video_1().click()
        action.video_1().send_keys('https://youtu.be/qaritester')

        time.sleep(3)
        Main.info("Clicking on Video Link 2")
        action.video_2().clear()
        time.sleep(2)
        action.video_2().click()
        action.video_2().send_keys('https://youtu.be/qaritester')


case = Register
