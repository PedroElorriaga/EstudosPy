from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)
driver.get('https://br.financas.yahoo.com/quote/%5EBVSP?p=%5EBVSP')

excel_read_file = pd.read_excel(r'C:\Users\Pedro\Downloads\EstudosPy\LibSelenium\SeleniumBasics\Arquivos_Download\acoes.xlsx', sheet_name='Ações')
codigos = excel_read_file['Código'].tolist()

for codigo in codigos:
    campo_pesquisar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="yfin-usr-qry"]'))
    )

    campo_pesquisar.send_keys(codigo, Keys.RETURN)

    time.sleep(5)
    header_acao = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'mrt-node-Lead-5-QuoteHeader'))
    )
    nome_empresa = header_acao.find_element(By.TAG_NAME, 'h1')
    print(nome_empresa.text)
    
    secao_estatistica = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="quote-nav"]/ul/li[3]/a'))
    ).click()

    table_avaliacoes = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[2]/div[1]/div'))
    )
    tr = table_avaliacoes.find_elements(By.TAG_NAME, 'tr')
    print(tr[1].text)
    # TODO APRIMORAR

    time.sleep(5)
