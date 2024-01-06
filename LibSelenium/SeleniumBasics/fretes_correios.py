from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time
import pandas as pd
import xlsxwriter

df = pd.read_excel(r'C:\Users\Pedro\Downloads\EstudosPy\LibSelenium\SeleniumBasics\Arquivos_Download\Correios_frete.xlsx')

entrega = []
valor = []

driver = webdriver.Chrome()
driver.get('https://www2.correios.com.br/sistemas/precosPrazos/')

for index, row in df.iterrows():

    cep_origem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[3]/form/div/div/span[3]/label/input'))
    )
    cep_origem.send_keys(f'{row["Origem"]:08.0f}')

    cep_destino = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[3]/form/div/div/span[5]/label/input')
    cep_destino.send_keys(f'{row["Destino"]:08.0f}')

    select_servico = Select(driver.find_element(By.NAME, 'servico'))
    select_servico.select_by_value('04510')


    # LOAD SCRIPT DEPOIS DE SERVICO SELECIONADO
    select_embalagem = Select(WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'embalagem1'))
    ))
    select_embalagem.select_by_value('outraEmbalagem1')

    altura_cm = driver.find_element(By.NAME, 'Altura').send_keys(int(row['Altura']))
    largura_cm = driver.find_element(By.NAME, 'Largura').send_keys(int(row['Largura']))
    comprimento_cm = driver.find_element(By.NAME, 'Comprimento').send_keys(int(row['Comprimento']))

    select_peso = Select(driver.find_element(By.NAME, 'peso'))
    select_peso.select_by_value(str(int(row['Peso'])))

    servicos_opcionais = driver.find_element(By.NAME, 'MaoPropria').click()
    time.sleep(1)

    btn_calcular = driver.find_element(By.XPATH, '//*[@id="spanBotao"]/input').click()
    time.sleep(1.5)


    # EXTRAIR DADOS DE RESULTADO NA NOVA JANELA
    WebDriverWait(driver, 10).until(
        EC.number_of_windows_to_be(2)
    )
    janelas = driver.window_handles

    for janela in janelas:
        if janela != driver.current_window_handle:
            driver.switch_to.window(janela)
            break

    tbody = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'tbody'))
    )
    tr_geral = tbody.find_elements(By.TAG_NAME, 'tr')

    entrega_text = tr_geral[2].find_element(By.TAG_NAME, 'td').text

    tfoot = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'tfoot'))
    )
    valor_text = tfoot.find_element(By.TAG_NAME, 'td').text

    entrega.append(entrega_text)
    valor.append(valor_text)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()

print(valor, entrega)
driver.quit()
