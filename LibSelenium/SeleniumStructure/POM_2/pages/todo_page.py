from base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

class Todo(BasePage):
    nome_tarefa_id = (By.ID, 'todo-name')
    descricao_id = (By.ID, 'todo-desc')
    urgente_id = (By.ID, 'todo-next')
    botao_id = (By.ID, 'todo-submit')

    def fill_todo_forms(self, nome_tarefa, desc_tarefa, urgent=False):
        self.find_element(self.nome_tarefa_id).send_keys(nome_tarefa)
        self.find_element(self.descricao_id).send_keys(desc_tarefa)

        if urgent:
            self.find_element(self.urgente_id).click()

        self.find_element(self.botao_id).click()
        return True

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
                                    
    driver = webdriver.Chrome(options=options)

    todo = Todo(driver, 'https://selenium.dunossauro.live/todo_list.html')
    todo.open_url()
    todo.fill_todo_forms(
        'Estudar python',
        'Estudar sobre POM e Tests',
        urgent= True
    )
