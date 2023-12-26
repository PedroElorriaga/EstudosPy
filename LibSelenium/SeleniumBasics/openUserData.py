import os
import time
import getpass # PEGAR USUARIO

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import SessionNotCreatedException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class Main_code:
    def __init__(self, directory, user = 'Default'):
        self.directory = directory
        self.user = user
        self.options = webdriver.ChromeOptions()
        self.argument = f'--user-data-dir={self.directory}', '--no-sandbox', f'--profile-directory={self.user}',
        self.browser = self.make_driver_chrome(*self.argument)

    def make_driver_chrome(self, *args):
        if args is not None:
            for arg in args:
                self.options.add_argument(arg)

        self.options.add_experimental_option('detach', True)

        driver = webdriver.Chrome(
            options=self.options
        )

        return driver

    def get_website_url(self, url):
        self.browser.get(url)
        
        self.browser.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.CONTROL, 't')
        

if __name__ == '__main__':
    # PARA ABRIR EM UM PROFILE O CHROME NÃO DEVE TER NENHUMA SESSÃO EM ABERTO
    start = Main_code(r'C:\Users\{}\AppData\Local\Google\Chrome\User Data'.format(getpass.getuser()), 'Profile 1')
    start.get_website_url('https://www.google.com/')