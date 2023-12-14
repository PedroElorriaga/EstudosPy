import os
import sys

file_path = os.path.dirname(__file__)
parent_path = os.path.join(file_path, '..')
sys.path.append(parent_path)

from pages.login_pages import LoginPage, Result_login_page
import unittest
from selenium import webdriver

class PageLoginTest(unittest.TestCase):

    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome()

    def test_fill_login(self):
        login_element = LoginPage(self.driver, 'https://trytestingthis.netlify.app/')
        login_element.open_page()
        login_element.fill_login_forms(
            'test',
            'test'
        )

        result_element = Result_login_page(self.driver)
        self.assertEqual(result_element.page_confirms_login(), 'Login Successful :)')
    
    def tearDown(self):
        return self.driver.close()

if __name__ == '__main__':
    unittest.main()