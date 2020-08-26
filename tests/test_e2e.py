import pytest
from selenium import webdriver
# browser exposes one executable file
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.shopItems().click()
        checkOutPage = CheckOutPage(self.driver)
        log.info("Getting all the card titles")
        cards = checkOutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i+1
            cardText = card.text
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()

        #self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        checkOutPage.getCardButton().click()
        log.info("Entering country name")
        #self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        checkOutPage.getCheckOutItems().click()
        self.driver.find_element_by_id("country").send_keys("ind")
        self.verifyLinkPresence("India")
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        textMatch = self.driver.find_element_by_css_selector("[class*='alert-success']").text

        assert ("Success! Thank you!" in textMatch)


