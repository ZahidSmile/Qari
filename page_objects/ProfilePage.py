from selenium.webdriver.common.by import By


class LoginPage:
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
        return self.driver.find_element(By.CSS_SELECTOR, '.PackBox div.FieldBox .multi_default ng-select')

    def day_1(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#mat-slide-toggle-1')

    def day_2(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#mat-slide-toggle-2')

    def cls_duration(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.ClassDuration [alt="add"]')

    def iban(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="IBAN"]')

    def account(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Account title"]')

    def billing(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Billing address"]')
