from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.bag()

    def bag(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#item_4_img_link")

    def add(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")

    def cart(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')

    def contshop(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#continue-shopping')

    def light(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bike-light')

    def tshirt(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt')







