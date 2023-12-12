import unittest
import time
from selenium import webdriver


class TestandoCodSelenium(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        return self.driver

    def test_open_website(self):
        self.driver.get('https://docs.python.org/3/library/unittest.html')

    def test_alter_tab(self):
        self.driver.execute_script('window.open("https://github.com/PedroElorriaga/EstudosPy/blob/main/LibSelenium/altTab.py");')
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)
        self.driver.window_handles[1]

    def tearDown(self):
        self.driver.close()
        return


if __name__ == '__main__':
    unittest.main()