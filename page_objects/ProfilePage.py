from selenium.webdriver.common.by import By


class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    def get_hired(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.Button .btn-primary')

    def teach(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[value="both"]')

    def class_pw(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.PackBox div.FieldBox:nth-child(2) img[alt="add"]')

    def charges_pm(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.PackBox div.FieldBox:nth-child(3) img[alt="add"]')

    def class_duration(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.PackBox div.FieldBox:nth-child(4) img[alt="add"]')

    def subjects(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.PackBox div.FieldBox .multi_default ng-select input')

    def add_package(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.addpackage')

    def remove_package(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.fa-trash')

    def add_timing(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.DaySection .Add')

    def remove_timing(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.Times .Delete .fa-trash-alt')

    def day_2(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#mat-slide-toggle-2')

    def day_7(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#mat-slide-toggle-7')

    def cls_duration(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.ClassDuration [alt="add"]')

    def iban(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="IBAN"]')

    def account(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Account title"]')

    def billing(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Billing address"]')

    def submit(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
