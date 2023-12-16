from base_page import BasePage
from selenium.webdriver.common.by import By

class Card(BasePage):
    fieldset_todo_id = (By.ID, 'todo')
    cards_todo_id = (By.CLASS_NAME, 'terminal-card')
    name_card = (By.CSS_SELECTOR, 'header.name')
    description_card = (By.CSS_SELECTOR, 'div.description')

    def take_all_cards(self):
        fieldset = self.find_element(self.fieldset_todo_id)
        cards = fieldset.find_elements(*self.cards_todo_id)

        return cards
    
    def urgent_cards_to_doing(self):
        for card in self.take_all_cards():
            if card.text.split()[0].lower() == 'urgente':
                card.find_element(By.CSS_SELECTOR, 'button.do').click()
        
        return True
    
    def remove_cards_give_up(self):
        for card in self.take_all_cards():
            if card.text.split()[0].lower() == 'desistir':
                card.find_element(By.CSS_SELECTOR, 'button.cancel').click()

        return True
    
    def show_all_cards(self):
        for card in self.take_all_cards():
            titulo = card.find_element(*self.name_card).text
            desc = card.find_element(*self.description_card).text
            print(f'Card [Titulo: {titulo}, Descrição: {desc}]')