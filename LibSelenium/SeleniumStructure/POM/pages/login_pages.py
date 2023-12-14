from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

class BasePage(object):
    def __init__(self, driver, url=''):
        self.driver = driver
        self.url = url

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def open_page(self):
        self.driver.get(self.url)

class LoginPage(BasePage):
    """ atributo = locator """
    username = (By.ID, 'uname')
    password = (By.ID, 'pwd')
    submit = (By.XPATH, '/html/body/div[3]/div[1]/fieldset/form/div/input[3]')

    def fill_login_forms(self, username, password):
        self.find_element(self.username).send_keys(username)
        self.find_element(self.password).send_keys(password)
        self.find_element(self.submit).click()

class Result_login_page(BasePage):
    """ atributo = locator """
    title_h2 = (By.TAG_NAME, 'h2')
    
    def page_confirms_login(self):
        time.sleep(3)
        print(self.find_element(self.title_h2).text)
        if 'Login Successful :)' in self.find_element(self.title_h2).text: # PEGA VALOR DE TEXTO h2
            return True
        
        return False


if __name__ == "__main__":

    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)

    driver = webdriver.Chrome(options=options)
    url = 'https://trytestingthis.netlify.app/'

    login_element = LoginPage(driver, url)
    login_element.open_page()

    login_element.fill_login_forms(
        'test',
        'test'
    )

    result_element = Result_login_page(driver)
    print(result_element.page_confirms_login())