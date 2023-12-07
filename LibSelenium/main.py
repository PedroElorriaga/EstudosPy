import os
import time

from dotenv import load_dotenv

from colorama import Fore
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

load_dotenv()
class Automate:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        # self.actions_keys = ActionChains(self.options)
        self.errors = []
        self.options_tuple = '--start-maximized', '--disable-gpu',
        self.browser = self.make_chrome_driver(*self.options_tuple)
        

    def make_chrome_driver(self, *optionsParam):
        if optionsParam is not None:
            for option in optionsParam:
                self.options.add_argument(option)

        driver = webdriver.Chrome(
            options=self.options, # UTILIZANDO AS OPÇÕES DO CRHOME
        )

        return driver
    
    def open_chrome_and_open_x(self):
        self.browser.get('https://www.google.com.br')

        try:
            # PESQUISAR POR CORINTHIANS     
            element_search = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'gLFyf'))
            ) # UTILIZADO QUANDO TEMOS QUE ESPERAR ALGUNS ELEMENTOS JS CARREGAR
            element_search.send_keys('Corinthians')
            element_search.send_keys(Keys.ENTER)

            # PEQUISAR POR X
            element_search = self.browser.find_element(By.XPATH, '//*[@id="APjFqb"]')
            element_search.click()
            element_search.send_keys(Keys.CONTROL, 'a')
            element_search.send_keys('x')
            element_search.send_keys(Keys.ENTER)

            # CLICAR NA PRIMEIRA PESQUISA
            element_listar_links = self.browser.find_element(By.ID, 'search')
            links = element_listar_links.find_elements(By.TAG_NAME, 'a')
            links[0].click()

        except TimeoutException as e:
            self.errors.append('Não encontrado')
            print(f'Erro: {e.stacktrace[0]}')
            
        except TypeError as e:
            self.errors.append('Erro de tipo')
            print(f'Erro: {e}')

        finally:
            if not self.errors:
                print(Fore.GREEN + 'open_chrome passed' + Fore.RESET)
                self.login_page_x()

            else:
                print(self.errors)
                self.browser.quit()

    def login_page_x(self):
        try:
            # CLICAR PARA FAZER LOGIN
            element_entrar = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'r-2o02ov'))
            )
            links = element_entrar.find_elements(By.TAG_NAME, 'a')
            links[0].click()
            
            # INSERIR EMAIL
            element_email_x = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'r-30o5oe'))
            )
            element_email_x.send_keys(os.getenv('USER_MAIL'))
            element_email_x.send_keys(Keys.ENTER)

            # INSERIR SENHA
            element_password_x = WebDriverWait(self.browser, 4).until(
                EC.presence_of_element_located((By.NAME, 'password'))
            )
            print(element_password_x)
            element_password_x.send_keys(os.getenv('USER_PASSWORD'))
            element_password_x.send_keys(Keys.ENTER)
        
        except TimeoutException as err:
            self.put_user_x_and_log()
        
        finally:
            time.sleep(10)

    def put_user_x_and_log(self):
        # INSERIR USER
        element_temp_x = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'r-30o5oe'))
        )
        element_temp_x.send_keys(os.getenv('USER_X'))
        element_temp_x.send_keys(Keys.ENTER)

        # INSERIR SENHA
        element_password_x = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        element_password_x.send_keys(os.getenv('USER_PASSWORD'))
        element_password_x.send_keys(Keys.ENTER)


if __name__ == '__main__':
    start = Automate()
    start.open_chrome_and_open_x()