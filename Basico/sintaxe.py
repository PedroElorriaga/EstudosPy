import os
import datetime
import time

clear = lambda: os.system('cls') # LAMBDA CIRA UMA FUNÇÃO ANONIMA

date = datetime.datetime.now()

spacePrint = lambda: print('-' * 60)

def verificarAnoDeNascimento(idade):
    return date.year - idade

if __name__ == '__main__': # ESTOU UTILIZANDO UMA EXPORTAÇÃO E NÃO QUERO QUE ISSO SEJA EXECUTADO EM OUTRA FILE
    print('Testando Sintaxe do Python novamente')
    spacePrint()

    numeroUm = 19
    numeroDois = 2

    print(numeroUm + numeroDois)
    spacePrint()

    print('Apenas pessoas que nasceram antes de 2003 podem jogar!')
    print('Insira suas informações abaixo')

    try :
        nomeInput = input('Nome: ')
        idadeInput = int(input('Idade: '))

        if verificarAnoDeNascimento(idadeInput) > 2002:
            print(f'{nomeInput} nasceu em {verificarAnoDeNascimento(idadeInput)}, não pode jogar!')
        else:
            print(f'{nomeInput} você naceu em {verificarAnoDeNascimento(idadeInput)}, pode jogar!')

    except:
        print('Favor somente números no campo idade')
        
    spacePrint()

    repeticoes = 5

    while repeticoes > 0:
        print(repeticoes)
        repeticoes -= 1
        
        if repeticoes == 0:
            print('Repetições acabou!!')
        
        time.sleep(1.5)


    time.sleep(3)
    clear()