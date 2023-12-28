import os
import sys
file_path = os.path.dirname(__file__)
folder_pages_path = os.path.join(file_path, '..')
sys.path.append(folder_pages_path)

import time
import pathlib
import pandas as pd
from BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class YoutubePage(BasePage):

    localizador_secao_titulo = (By.CLASS_NAME, 'count-text')
    localizador_quantidade_comentarios = (By.TAG_NAME, 'span')
    localizador_secao_comentarios = (By.ID, 'contents')
    localizador_comentarios = (By.CLASS_NAME, 'ytd-item-section-renderer')
    localizador_autor_id = (By.TAG_NAME, 'yt-formatted-string')
    localizador_texto_comentado = (By.ID, 'content-text')

    def __init__(self, web_driver):
        super().__init__(web_driver)


    def abrir_video_youtube(self, url):
        self.web_driver.get(url)


    def carregar_scroll_comentarios(self):
        self.web_driver.execute_script('window.scrollBy(0, 700);')
        time.sleep(4)
        self.web_driver.execute_script('window.scrollBy(0, 500);')


    def contar_quantidade_comentarios_em_inteiros(self):
        secao_quantidade = WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located(self.localizador_secao_titulo)
        )

        return int(secao_quantidade.find_elements(*self.localizador_quantidade_comentarios)[0].text.replace(',', ''))
    

    def carregar_todos_comentarios(self, secao_quantidade):
        for i in range (0, secao_quantidade, 10):
            time.sleep(3)
            self.web_driver.execute_script('window.scrollBy(0, 1000);')

        secao_comentarios = WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located(self.localizador_secao_comentarios)
        )

        return secao_comentarios

    def listando_todos_comentarios(self, secao_comentarios):
        lista_comentarios = []
        comentarios = secao_comentarios.find_elements(*self.localizador_comentarios)

        for comentario in comentarios:
            autor_id = comentario.find_element(*self.localizador_autor_id)
            texto_comentado = comentario.find_element(*self.localizador_texto_comentado)
            lista_comentarios.append({'Autor' : autor_id.text, 'Comentario' : texto_comentado.text})

        return lista_comentarios


    def gerar_arquivo_xlsx(self, lista_comentarios):
        caminho_pai_arquivo = pathlib.Path(__file__).parent.parent # c:\Users\usuario\Downloads\EstudosPy\LibSelenium\WebScraping\PO_comments
        data_frame = pd.DataFrame(lista_comentarios)
        data_frame.to_excel(str(caminho_pai_arquivo) + '\\arquivos' + '\\' + self.gerar_nome_de_arquivo_xlsx(), sheet_name='Comentarios')


    def gerar_nome_de_arquivo_xlsx(self):
        seconds = str(time.time()).split('.')[0]
        nome_arquivo = seconds + '_comentarios.xlsx'
        return nome_arquivo
    