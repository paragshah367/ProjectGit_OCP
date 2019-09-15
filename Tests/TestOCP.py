# coding=utf-8
import unittest
from Resources import common_keywords as key
from Pages.OCP.LoginPage import LoginPage
from Pages.OCP.HomePage import HomePage
from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner


class TestOCP(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Open browser and load url """

        url = 'https://ocp.boku.com/'
        cls.driver = key.launch_browser(url)

    def test_1_login(self):

        # Login to OCP
        login = LoginPage(self.driver)
        login.assert_loginpage()
        login.login()

    def test_2_enduser(self):

        # Check End user activity page
        homepage = HomePage(self.driver)
        homepage.assert_homepage()
        homepage.end_user()

    @classmethod
    def tearDownClass(cls):
        """ Quit browser """

        key.quit_browser(cls.driver)


# if __name__ == '__main__':
#     unittest.main()
HTMLTestRunner(output='OCP_project/Results').run(TestLoader().loadTestsFromTestCase(TestOCP))
