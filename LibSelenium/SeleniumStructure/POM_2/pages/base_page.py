from abc import ABC

class PageElement(ABC):
    def __init__(self, driver, url=''):
        self.driver = driver
        self.url = url

    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

class Page(PageElement, ABC):
    
    def open_url(self):
        return self.driver.get(self.url)

