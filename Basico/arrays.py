import datetime
import time

from sintaxe import clear, spacePrint # EXPORTANDO FUNÇÃO DE OUTRA FILE
from collections import Counter

clear()

marcasCarros = ['Mercedes', 'Porsche', 'BMW', 'Land Rover', 'Audi']

mostrarQtdMarcas = len(marcasCarros)
print(f'Temos {mostrarQtdMarcas} de marcas de carros no array')
spacePrint()


def mostrarOrdAlpha():
    marcasOrdem = marcasCarros.copy() # CRIA UMA CÓPIA DO ARRAY, NÃO ALTERANDO O ORIGINAL
    marcasOrdem.sort()
    print('Mostrando array em ordem alfabética: ', marcasOrdem)
    return

mostrarOrdAlpha()
print('Original: ', marcasCarros)
spacePrint()


def incluirNovaMarca(valor):
    marcasCarros.append(valor)
    print(f'{valor} adicionado!')
    print(marcasCarros)
    return

incluirNovaMarca('Lamborghini')
print('Original: ', marcasCarros) # ALTERA O VALOR NO ORIGINAL
spacePrint()


def mostrarIndexDaMarca(valor):
    for marca in marcasCarros:
        if marca == valor:
            return print('Sua marca está na posição: ', marcasCarros.index(valor))
    
    return print('A marca não está na lista')

mostrarIndexDaMarca(input('Insira uma marca: '))
spacePrint()

arr = [1, 2, 2, 3, 4, 4, 4, 5]


def iterandoArray() :
    print('Iterando o array: ')
    for item in arr:
        print(item)

iterandoArray()
spacePrint()


def pegandoDuplicadas():
    counter = Counter(arr) # CONTA QUANTAS VEZES O ITEM FOI REPETIDO
    print('Counter: ', counter.items())
    duplicados = {chave: valor for chave, valor in counter.items() if valor > 1}
    
    somaDosDuplicados = sum(duplicados.values())

    for conjunto in duplicados.items():
        print(f'O valor {conjunto[0]} apareceu {conjunto[1]} vezes')

    print('Total duplicados: ', somaDosDuplicados)

pegandoDuplicadas()