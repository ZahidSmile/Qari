from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def start(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".FillingButton button")

    def profile(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#profilepicture')

    def profile_exist(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.ProfileImage span.cancel')

    def country(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#Country")

    def state(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#stateId')

    def city(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#cityId')

    def address(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#Address')

    def gender(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[value="male"]')

    def language(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#cdk-step-content-0-1 ng-select div.ng-input input[type=text]')

    def ex_lang(self):
        return self.driver.find_elements(By.CSS_SELECTOR, 'span.ng-value-icon')[0]

    def about(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#About')

    def step_2(self):
        return self.driver.find_elements(By.CSS_SELECTOR, 'button span.ng-star-inserted')[0]

    def qualifications(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#cdk-step-content-0-2 div.ng-input > input[type=text]')

    def ex_qualf(self):
        return self.driver.find_elements(By.CSS_SELECTOR, 'span.ng-value-icon')[1]

    def certificate(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#item_images')

    def certificate_exist(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.ImageList span.cancel')

    def ex_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.ExperiecesDetails [formcontrolname="title"]')

    def from_date(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.Dates [placeholder="From"]')

    def to_date(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.Dates [placeholder="to"]')

    def exp_details(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#exp_details')

    def video_1(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#video1')

    def video_2(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#video2')

    def step_1(self):
        return self.driver.find_elements(By.CSS_SELECTOR, '.tab')[0]

    def step_3(self):
        return self.driver.find_elements(By.CSS_SELECTOR, 'button span.ng-star-inserted')[1]

    def step_4(self):
        return self.driver.find_elements(By.CSS_SELECTOR, 'button span.ng-star-inserted')[2]





