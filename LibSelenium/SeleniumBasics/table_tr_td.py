from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time
import pathlib
import pandas as pd

file_path = pathlib.Path(__file__).parent
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options)

driver.get('https://investidor10.com.br/acoes/rankings/maiores-valor-de-mercado/')

driver.execute_script('window.scrollBy(0, 800);')

time.sleep(2.5)
btn_read_more = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'btn-readmore'))
).click()

rankings = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'tbody'))
)


tr_list = rankings.find_elements(By.TAG_NAME, 'tr')

dados = []
for tr in tr_list[1:]:
    textos = []
    td_list = tr.find_elements(By.TAG_NAME, 'td')

    for td_text in td_list:
        td_text = td_text.text

        if td_text != '':
            textos.append(td_text)

    dados.append(textos)

dados_filtrados = [dado for dado in dados if dado != []]

data_frame = pd.DataFrame(dados_filtrados)
data_frame.columns = ['Código', 'Valor de Mercado',
                      'P/L', 'P/VP', 'Margem Liquida', 'Setor']
data_frame.to_excel(
    str(file_path) + '\\Arquivos_Download\\acoes.xlsx', sheet_name='Ações')

driver.quit()
