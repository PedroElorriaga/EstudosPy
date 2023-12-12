from abc import ABC, abstractmethod

class Selvagem(ABC):
    
    @abstractmethod
    def tipo_obrigatorio(self):
        pass

    def tipo_animal(self):
        print('Animal terrestre')


class Domestico(ABC):

    @abstractmethod
    def tipo_obrigatorio(self):
        pass

    def tipo_animal(self):
        print('Animal terrestre')


