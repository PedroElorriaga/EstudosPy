from abc import ABC

class BasePage(ABC):
    def __init__(self, driver, url=''):
        self.driver = driver
        self.url = url
    
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def open_url(self):
        return self.driver.get(self.url)
