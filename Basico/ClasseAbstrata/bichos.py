from tipo import Selvagem, Domestico

class Dog(Domestico):

    def __init__(self, nome):
        self.nome = nome
    
    def som(self):
        print(f'{self.nome} está latindo')

    # ESSE MÉTODO DEVE SER ATRIBUIDO A ESTÁ CLASSE, POIS ELE É OBRIGATÓRIO
    def tipo_obrigatorio(self):
        print('Obrigatorio chamado')


class Tiger(Selvagem):

    def __init__(self, nome):
        self.nome = nome

    def som(self):
        print(f'{self.nome} está rugindo')

    def tipo_obrigatorio(self):
        print('Obrigatorio chamado')
        

class TesteParaDarErro(Selvagem):

    def qualquerCoisa(self):
        print('Qualque coisa')
        

if __name__ == '__main__':
    dog = Dog('Bandit')
    dog.som()
    dog.tipo_obrigatorio()
    dog.tipo_animal()
    print('-' * 60)

    tiger = Tiger('Simba')
    tiger.som()
    tiger.tipo_obrigatorio()
    tiger.tipo_animal()
    print('-' * 60)

    print('Vai dar erro!!')
    try:
        teste = TesteParaDarErro()
    
    except TypeError as err:
        print(err)