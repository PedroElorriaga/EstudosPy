from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

import time

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)

driver.get('https://lista.mercadolivre.com.br/chave-range-rover-evoque#D[A:chave%20range%20rover%20evoque]')

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'cookie-consent-banner-opt-out__action'))
    ).click()
except:
    print('Cookies ja foi clicado')

ultima_pagina = False
index_page = 1

preco_geral = 0
index_produtos = 0
while not ultima_pagina:
    try:
        time.sleep(1.5)
        campo_resultados = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ui-search-layout'))
        )

        cards_resultado = WebDriverWait(campo_resultados, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'ui-search-result__wrapper'))
        )
        
        for card in cards_resultado:
            index_produtos += 1
            preco_geral += float(card.find_element(By.CLASS_NAME, 'andes-money-amount__fraction').text)
    
    except StaleElementReferenceException:
        continue

    try:
        btn_proximo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'andes-pagination__button--next'))
        )

        btn_proximo.find_element(By.TAG_NAME, 'a').click()
        index_page += 1
    
    except:
        ultima_pagina = True
        print('Concluido com sucesso!')

media_preco_produtos = lambda x, y: x / y

print(f'A média de preço dos podutos é de: R$ {media_preco_produtos(preco_geral, index_produtos):.2f}')

driver.quit()
