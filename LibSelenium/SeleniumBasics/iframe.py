from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/derivativos/ajustes-do-pregao/')

time.sleep(1.5)
try:
    teste = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler'))
    ).click()
except:
    print('Cookies ja locados')

driver.switch_to.frame('bvmf_iframe') # QUANDO UTILIZAMOS IFRAME, DEVEMOS UTILIZAR ESTE MÉTODO

tabela = driver.find_element(By.ID, 'tblDadosAjustes')
th = tabela.find_element(By.TAG_NAME, 'th')

print(th.text)

driver.quit()
