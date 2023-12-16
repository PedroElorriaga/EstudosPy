import sys
import os

file_path = os.path.dirname(__file__)
pages_path = os.path.join(file_path, '..', 'pages')
sys.path.append(pages_path)

from todo_page import Todo
from card_page import Card
from selenium import webdriver
import unittest
import time

class TodoTest(unittest.TestCase):

    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome()
        return self.driver
    
    def test_todo(self):
        todo_element = Todo(self.driver, 'https://selenium.dunossauro.live/todo_list.html')
        todo_element.open_url()

        self.assertTrue(todo_element.fill_todo_forms('Estudar Python', 'Estudar POM e Testes'))

    def test_cards(self):
        todo_element = Todo(self.driver, 'https://selenium.dunossauro.live/todo_list.html')
        todo_element.open_url()

        self.assertTrue(todo_element.fill_todo_forms('Desistir', 'Estudar POO'))
        self.assertTrue(todo_element.fill_todo_forms('Estudar C#', 'ALL'))
        self.assertTrue(todo_element.fill_todo_forms('Urgente', 'Segundo enviado', True))
        self.assertTrue(todo_element.fill_todo_forms('Estudar POKER', 'All in'))
        self.assertTrue(todo_element.fill_todo_forms('Estudar Python', 'Estudar POM e Testes'))
        self.assertTrue(todo_element.fill_todo_forms('Desistir', 'Estudar POO'))
        self.assertTrue(todo_element.fill_todo_forms('Urgente', 'Ultimo enviado', True))

        cards_element = Card(self.driver)
        cards_element.take_all_cards()

        self.assertTrue(cards_element.urgent_cards_to_doing())
        self.assertTrue(cards_element.remove_cards_give_up())
        cards_element.show_all_cards()
        time.sleep(10)

    def tearDown(self):
        return self.driver.quit()
    

if __name__ == '__main__':
    unittest.main()