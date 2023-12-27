from abc import ABC

class BasePage(ABC):
    def __init__(self, webDriver):
        self.webDriver = webDriver