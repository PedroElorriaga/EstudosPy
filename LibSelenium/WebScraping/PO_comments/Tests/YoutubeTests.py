import os
import sys
file_path = os.path.dirname(__file__)
folder_pages_path = os.path.join(file_path, '..')
sys.path.append(folder_pages_path)

from selenium import webdriver
from Pages.YoutubePage import YoutubePage
import unittest


class YoutubeTest(unittest.TestCase):

    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--start-maximized')
        self.webdriver = webdriver.Chrome(options=self.options)
        
    
    def test_youtube_comments(self):
        # ABRIR VÍDEO DO YOUTUBE
        self.youtube_page = YoutubePage(self.webdriver)
        self.youtube_page.abrir_video_youtube('https://www.youtube.com/watch?v=QDORlz17dm0&ab_channel=SOLUCIONANDOFILMES')

        # CARREGAR QUANTIDADE DE COMENTARIOS CARREGANDO O SCRIPT
        self.youtube_page.carregar_scroll_comentarios()

        # PEGAR QUANTIDADE DE COMENTARIOS 
        quantidade_comentarios = self.youtube_page.contar_quantidade_comentarios_em_inteiros()

        # CARREGAR TODOS COMENTARIOS
        comentarios_element = self.youtube_page.carregar_todos_comentarios(quantidade_comentarios)

        # LISTANDO TODOS OS COMENTARIOS EM FORMA DE TEXTO
        lista_comentarios = self.youtube_page.listando_todos_comentarios(comentarios_element)

        # GERAR ARQUIVO XLSX
        self.youtube_page.gerar_arquivo_xlsx(lista_comentarios)

    def tearDown(self):
        self.webdriver.quit()


if __name__ == '__main__':
    unittest.main()