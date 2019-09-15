# coding=utf-8
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class HomePage:
    """ OCP Home Page """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

        self.welcome_xpath = "// div[contains(text(), 'Welcome to OCP')]"
        self.consumers_xpath = "//*[*='Consumers']"
        self.enduser_xpath = "//a[contains(text(),'End-User Activity')]"

    def assert_homepage(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.welcome_xpath).is_displayed()
        print('HomePage')

    def end_user(self):
        time.sleep(1)
        self.driver.find_element_by_xpath(self.consumers_xpath).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.enduser_xpath))).click()
