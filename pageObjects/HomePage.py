

from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop) # This means driver.find_element_by_css_selector("a[href*='shop']").click()
        # Above * is used to deserialized the tupple