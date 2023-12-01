import time
import datetime
from sintaxe import clear, spacePrint

clear()

date = datetime.datetime.now()

class Pessoa:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano

    def verificarPessoa(self):
        print(f'Olá {self.nome} obrigado por cadastrar no sistema!')

    def permissaoCadastro(self):
        age = lambda yearInt: date.year - yearInt

        if age(self.ano) > 18:
            return print(f'{self.nome}, você tem {age(self.ano)} anos, entrada liberada!')

        else:
            return print(f'{self.nome}, você tem {age(self.ano)} anos, entrada negada!')

def executarPessoa(nome, ano):

    pessoa = Pessoa(nome, ano)
    spacePrint()

    pessoa.verificarPessoa()
    spacePrint()

    print('Carregando suas informações...')
    time.sleep(3.5)

    pessoa.permissaoCadastro()
    spacePrint()


executarPessoa(input('Digite seu nome: '), int(input('Digite sua data de nascimento: ')))
executarPessoa(input('Digite seu nome: '), int(input('Digite seu ano de nascimento: ')))