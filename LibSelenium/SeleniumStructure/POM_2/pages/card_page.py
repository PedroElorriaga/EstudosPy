from base_page import BasePage
from selenium.webdriver.common.by import By

class Card(BasePage):
    fieldset_todo_id = (By.ID, 'todo')
    cards_todo_id = (By.CLASS_NAME, 'terminal-card')

    def take_all_cards(self):
        fieldset = self.find_element(self.fieldset_todo_id)
        cards = fieldset.find_elements(*self.cards_todo_id)
        return cards
    
    def urgent_cards_to_doing(self):
        for card in self.take_all_cards():
            if card.text.split()[0].lower() == 'urgente':
                card.find_element(By.XPATH, '//*[@id="todo"]/div[1]/div[2]/button[1]').click()
                return True

            return False