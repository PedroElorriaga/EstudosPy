import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

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
    
    user_data_path = r'C:\Users\Pedro\AppData\Local\Google\Chrome\User Data'
    options_tuple = '--no-sandbox', '--start-maximized', f'--user-data-dir={user_data_path}',
    browser = make_chrome_browse(*options_tuple)

    browser.get('https://www.google.com.br')

    try:
        # PESQUISAR POR CORINTHIANS
        element_search = WebDriverWait(browser, 4).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'gLFyf'))
        ) # UTILIZADO QUANDO TEMOS QUE ESPERAR ALGUNS ELEMENTOS JS CARREGAR
        element_search.send_keys('Corinthians')
        element_search.send_keys(Keys.ENTER)

        # CLICAR NO PROXIMO JOGO
        element_next_game = browser.find_element(By.CLASS_NAME, 'abhAW')
        element_next_game.click()

        # CLICAR PARA SAIR DO JOGO
        element_exit_game = WebDriverWait(browser, 6).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="liveresults-sports-immersive__match-fullpage"]/div/div[2]/div[1]/div/div[1]'))
        )
        element_exit_game.click()
        time.sleep(1.5)

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
        
    except:
        print('Não encontrado')
        time.sleep(3)
        browser.quit()

    finally:
        time.sleep(5)
    