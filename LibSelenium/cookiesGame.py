import os
import time

from colorama import Fore
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException


class Game():
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options_tuple = '--start-maximized',
        self.browser = self.make_chrome_driver(*self.options_tuple)

    def make_chrome_driver(self, *args):
        if args is not None:
            for arg in args:
                self.options.add_argument(arg)
        
        self.options.add_experimental_option('detach', True) # Deixa o navegador aberto

        driver = webdriver.Chrome(
            options=self.options
        )

        return driver
    
    def start_game(self):
        self.browser.get('https://orteil.dashnet.org/cookieclicker/')
        self.browser.implicitly_wait(4)

        print(f'Options: ')
        for i in self.options_tuple:
            print(Fore.CYAN + i)

        print(Fore.GREEN + 'Inicializando o game...' + Fore.RESET)

        self.get_website_game()
    
    def get_website_game(self):
        accept_cookie = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/a[1]'))
        )
        accept_cookie.click()

        choose_language = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, 'langSelect-EN'))
        )
        choose_language.click()

        self.get_cookies_points()

    def get_cookies_points(self):
        self.browser.implicitly_wait(5)

        get_cookie_image = self.browser.find_element(By.ID, 'bigCookie')
        get_cookie_count = self.browser.find_element(By.ID, 'cookies')
        itens_store = [self.browser.find_element(By.ID, 'productPrice' + str(i)) for i in range(1,-1,-1)] # OUTPUT [productPrice1, productPrice0]

        action_keys = ActionChains(self.browser)
        for i in range(5000):
            action_keys.click(get_cookie_image)
            action_keys.perform()
            count = get_cookie_count.text
            for item in itens_store:
                value = item.text
                if int(value) <= int(count.split()[0]):
                    self.buy_new_itens_store(item)

    def buy_new_itens_store(self, item):
        upgrade_store = ActionChains(self.browser)
        upgrade_store.move_to_element(item)
        upgrade_store.click()
        upgrade_store.perform()



if __name__ == '__main__':
    game = Game()
    game.start_game()