import os
import time
import dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

dotenv.load_dotenv()
options = webdriver.ChromeOptions() # INSTANCIANDO CHROMEDRIVER
actions_keys = ActionChains(options)

def make_chrome_browse(*optionsParam):
    if optionsParam is not None:
        for option in optionsParam:
            options.add_argument(option)

    driver = webdriver.Chrome(
        options=options, # UTILIZANDO AS OPÇÕES DO CRHOME
    )

    return driver

if __name__ == '__main__':
    
    errors = []
    options_tuple = '--start-maximized', '--disable-gpu',
    browser = make_chrome_browse(*options_tuple)

    browser.get('https://www.google.com.br')

    try:
        # PESQUISAR POR CORINTHIANS     
        element_search = WebDriverWait(browser, 4).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'gLFyf'))
        ) # UTILIZADO QUANDO TEMOS QUE ESPERAR ALGUNS ELEMENTOS JS CARREGAR
        element_search.send_keys('Corinthians')
        element_search.send_keys(Keys.ENTER)

        # PEQUISAR POR X
        element_search = browser.find_element(By.XPATH, '//*[@id="APjFqb"]')
        element_search.click()
        element_search.send_keys(Keys.CONTROL, 'a')
        element_search.send_keys('x')
        element_search.send_keys(Keys.ENTER)

        # CLICAR NA PRIMEIRA PESQUISA
        element_listar_links = browser.find_element(By.ID, 'search')
        links = element_listar_links.find_elements(By.TAG_NAME, 'a')
        links[0].click()

        # CLICAR PARA FAZER LOGIN
        element_entrar = WebDriverWait(browser, 4).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'r-2o02ov'))
        )
        links = element_entrar.find_elements(By.TAG_NAME, 'a')
        links[0].click()
        
        # INSERIR EMAIL
        element_email_x = WebDriverWait(browser, 4).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'r-30o5oe'))
        )
        element_email_x.send_keys(os.getenv('USER_MAIL'))
        element_email_x.send_keys(Keys.ENTER)

        # INSERIR USER
        element_temp_x = WebDriverWait(browser, 4).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'r-30o5oe'))
        )
        element_temp_x.send_keys(os.getenv('USER_x'))
        element_temp_x.send_keys(Keys.ENTER)

        # INSERIR SENHA
        element_password_x = WebDriverWait(browser, 4).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        element_password_x.send_keys(os.getenv('USER_PASSWORD'))
        element_password_x.send_keys(Keys.ENTER)

    except:
        errors.append('Não encontrado')
        browser.quit()
        
    finally:
        if not errors:
            print('Deu tudo certo')

        else:
            print(errors)

        time.sleep(10)
    