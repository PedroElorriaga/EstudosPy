import pandas as pd
import pathlib
import time

from colorama import Fore
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options)
driver.get('https://www.youtube.com/watch?v=QDORlz17dm0&ab_channel=SOLUCIONANDOFILMES')

driver.execute_script('window.scrollBy(0, 800);')
time.sleep(4)
driver.execute_script('window.scrollBy(0, 600);')

eraser = '\r' + '' * 100

# CONTADOR DE COMENTARIOS
print(Fore.GREEN + 'Iniciando o programa' + Fore.RESET)
count_section = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'count-text'))
)
count_int = int(count_section.find_elements(By.TAG_NAME, 'span')[0].text.replace(',', ''))

# CARREGANDO OS COMENTARIOS OCULTOS
print(Fore.RED + 'Contando os comentarios, AGUARDE!!' + Fore.RESET)
for i in range (0, count_int, 10):
    time.sleep(2)
    driver.execute_script('window.scrollBy(0, 1000);')

comments_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'contents'))
    )

# ITERANDO E COLOCANDO EM LISTA
print(Fore.RED + 'Gerando arquivo...' + Fore.RESET)
comments = comments_section.find_elements(By.CLASS_NAME, 'ytd-item-section-renderer')
comments_texts = []
for comment in comments:
    autor = comment.find_element(By.TAG_NAME, 'yt-formatted-string')
    comments_text = comment.find_element(By.ID, 'content-text')
    comments_texts.append({'Autor' : autor.text, 'Comentario' : comments_text.text})

# GERAÇÃO DE XLSX FILE
file_path = pathlib.Path(__file__).parent
df = pd.DataFrame(comments_texts)
file_name = str(count_int) + '_comments.xlsx' 
df.to_excel(str(file_path) + '\\' + file_name, sheet_name='Comentarios') # SALVANDO EM XLSX

print(Fore.GREEN + 'Concluido com sucesso!!' + Fore.RESET)

driver.quit()
