# É BASTANATE UTILIZADO PARA VALIDAR ATRIBUTOS

class Pessoa:
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade

    def print_age_and_name_init(self):
        return print(f'{self.nome} and {self.idade}')

    @property
    def nome(self):
        # Este código é executado quando alguém for
        # ler o valor de self.nome
        return self._nome
    
    @nome.setter
    def nome(self, value):
        # este código é executado sempre que alguém fizer 
        # self.nome = value
        if not isinstance(value, str):
            raise ValueError('O nome deve ser String')
        value = str(value.title())
        self._nome = value
        return self._nome

if __name__ == '__main__':
    pessoa = Pessoa('pedro henrique', 25)
    pessoa.print_age_and_name_init() # OUTPUT Pedro Henrique and 25