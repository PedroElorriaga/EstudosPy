import unittest
from selenium import webdriver

class SearchPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.python.org/')

    def test_open_web(self):
        assert True

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()