# coding=utf-8
import time
from Resources import common_keywords as key
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    """ OCP Login Page """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

        self.heading = 'OCP Login'
        self.heading_xpath = "//h2[@class='form-signin-heading']"
        self.user_xpath = "//input[@id='username']"
        self.pass_xpath = "//input[@id='password']"
        self.login_xpath = "//input[@value='Login']"

    def assert_loginpage(self):
        self.driver.implicitly_wait(10)
        if not 'OCP Login' in self.driver.title:
            raise Exception('Unable to load OCP')
        print('Page title -', self.driver.title)
        # assert 'OCP Login' in self.driver.title, 'Title mismatch'

    def login(self):
        time.sleep(1)
        self.wait.until(EC.text_to_be_present_in_element((By.XPATH, self.heading_xpath), self.heading))
        self.driver.find_element_by_xpath(self.user_xpath).send_keys(key.username)
        self.driver.find_element_by_xpath(self.pass_xpath).send_keys(key.password)
        self.driver.find_element_by_xpath(self.login_xpath).click()
        print('Logged in')
