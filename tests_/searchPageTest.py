import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.loginPage import LoginPage
from pages_.navigationBar import NavigationBar
from pages_.cartPage import CartPage


class SearchProduct(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field("narine.narine.1962@mail.ru")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field("Sahakyan1963!")
        loginPageObj.click_to_signin_button()
        time.sleep(5)

    def test_search_product_first(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.send_text_to_search_box("paper towels rolls")
        time.sleep(4)
        navigationBarObj.click_to_nav_search_submit()
        time.sleep(5)

    def test_search_product_second(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.send_text_to_search_box("cat ears")
        time.sleep(4)
        navigationBarObj.click_to_nav_search_submit()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()
