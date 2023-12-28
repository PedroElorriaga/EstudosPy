from abc import ABC, abstractmethod

class BasePage(ABC):
    @abstractmethod
    def __init__(self, web_driver):
        self.web_driver = web_driver
