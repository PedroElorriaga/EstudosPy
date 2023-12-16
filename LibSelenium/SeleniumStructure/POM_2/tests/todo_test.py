import sys
import os

file_path = os.path.dirname(__file__)
pages_path = os.path.join(file_path, '..', 'pages')
sys.path.append(pages_path)

from todo_page import Todo
from card_page import Card
from selenium import webdriver
import unittest

class TodoTest(unittest.TestCase):

    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome()
        return self.driver
    
    def test_todo(self):
        todo = Todo(self.driver, 'https://selenium.dunossauro.live/todo_list.html')
        todo.open_url()

        self.assertTrue(todo.fill_todo_forms('Estudar Python', 'Estudar POM e Testes'))

    def test_cards(self):
        todo = Todo(self.driver, 'https://selenium.dunossauro.live/todo_list.html')
        todo.open_url()

        self.assertTrue(todo.fill_todo_forms('Estudar Python', 'Estudar POM e Testes'))
        self.assertTrue(todo.fill_todo_forms('Estudar Java', 'Estudar POO'))
        self.assertTrue(todo.fill_todo_forms('Urgente', 'Ultimo enviado', True))

        cards = Card(self.driver)
        cards.take_all_cards()

        self.assertTrue(cards.urgent_cards_to_doing())

    def tearDown(self):
        return self.driver.quit()
    

if __name__ == '__main__':
    unittest.main()