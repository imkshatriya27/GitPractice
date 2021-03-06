from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")
    cardButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def getCardButton(self):
        return self.driver.find_element(*CheckOutPage.cardButton)

    def getCheckOutItems(self):
        return self.driver.find_element(*CheckOutPage.checkOut)