from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)
driver.get('https://br.financas.yahoo.com/quote/%5EBVSP?p=%5EBVSP')

excel_read_file = pd.read_excel(r'C:\Users\Pedro\Downloads\EstudosPy\LibSelenium\SeleniumBasics\Arquivos_Download\acoes.xlsx', sheet_name='Ações')
codigos = excel_read_file['Código'].tolist()

empresa = []
valor_empresa = []
for codigo in codigos:
    try:
        dado_codigo = []
        campo_pesquisar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="yfin-usr-qry"]'))
        )

        campo_pesquisar.send_keys(codigo, Keys.RETURN)
        time.sleep(2)

        header_acao = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'mrt-node-Lead-5-QuoteHeader'))
        )
        nome_empresa = header_acao.find_element(By.TAG_NAME, 'h1')
        empresa.append(nome_empresa.text)
        
        secao_estatistica = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="quote-nav"]/ul/li[3]/a'))
        ).click()

        table_avaliacoes = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[2]/div[1]/div'))
        )
        tr = table_avaliacoes.find_elements(By.TAG_NAME, 'tr')
        valor_empresa.append(tr[1].text.split()[3])

        time.sleep(1.5)

    except TimeoutException:
        driver.back()
        empresa.append('N/A')
        valor_empresa.append('N/A')
        time.sleep(2)
        continue

data = {'Código' : excel_read_file.iloc[:,1], 'Nome da empresa' : empresa, 'Valor da empresa' : valor_empresa}
df = pd.DataFrame(data)

with pd.ExcelWriter(r'C:\Users\Pedro\Downloads\EstudosPy\LibSelenium\SeleniumBasics\Arquivos_Download\acoes.xlsx', engine='openpyxl', mode='a') as writer:
    df.to_excel(writer, sheet_name='ValoresYahoo', index=False)

driver.quit()
