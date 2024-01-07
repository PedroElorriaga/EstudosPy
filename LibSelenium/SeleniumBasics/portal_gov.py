from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException

import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)
driver.get('https://portaldatransparencia.gov.br/beneficios/consulta?ordenarPor=mesAno&direcao=desc')

btn_uf = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="id-box-filtro"]/div/div/ul/li[4]/div/button'))
).click()
time.sleep(0.5)

uf_sp = driver.find_element(By.XPATH, '//*[@id="id-box-filtro"]/div/div/ul/li[4]/div/div/div/div[2]/div[2]/ul/li[28]/a/label/input').click()

btn_adicionar = driver.find_element(By.XPATH, '//*[@id="id-box-filtro"]/div/div/ul/li[4]/div/div/div/div[2]/div[2]/ul/li[2]/input').click()

btn_consultar = driver.find_element(By.XPATH, '//*[@id="box-filtros-aplicados-com-botao"]/p/button[1]').click()

btn_paginacao = driver.find_element(By.XPATH, '//*[@id="lista_wrapper"]/div/div[2]/div[3]/button').click()

ultima_pagina = False
index_pagina = 1

lista_dados = []
while not ultima_pagina:
    try:
        tbody = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'tbody'))
        )
        tr = tbody.find_elements(By.TAG_NAME, 'tr')

        if index_pagina == 1:
            time.sleep(2)

        for td in tr:
            lista_dado = []
            for dado in td.find_elements(By.TAG_NAME, 'td')[1:]:
                lista_dado.append(dado.text)
            
            lista_dados.append(lista_dado) # EX: ['Novo Bolsa Família', '11/2023', '1.600.915.566,00']
        
        index_pagina += 1
            
    except StaleElementReferenceException:
        continue
    
    paginacao = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'pagination'))
    )

    btn_proximo = WebDriverWait(paginacao, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'next'))
    ).click()

    try:
        if WebDriverWait(paginacao, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li#lista_next.paginate_button.next.disabled'))):
            ultima_pagina = True
            print('Ultima página')
    except:
        ...

data_frame = pd.DataFrame(lista_dados)
data_frame.columns = ['Programa Social', 'Mês/Ano', 'Valor Disponibilizado']
data_frame.to_excel(r'C:\Users\Pedro\Downloads\EstudosPy\LibSelenium\SeleniumBasics\Arquivos_Download\Governo.xlsx', sheet_name='Pagina1', index=False)

driver.quit()
