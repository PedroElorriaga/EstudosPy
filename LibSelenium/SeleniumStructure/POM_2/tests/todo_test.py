import sys
import os

file_path = os.path.dirname(__file__)
pages_path = os.path.join(file_path, '..')
sys.path.append(pages_path)

from pages.todo_page import Todo
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

    def tearDown(self):
        return self.driver.close()
    

if __name__ == '__main__':
    unittest.main()