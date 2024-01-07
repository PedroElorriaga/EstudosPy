import datetime
import time

from sintaxe import clear, spacePrint # EXPORTANDO FUNÇÃO DE OUTRA FILE
from collections import Counter

clear()

marcasCarros = ['Mercedes', 'Porsche', 'BMW', 'Land Rover', 'Audi']

# LEN()
mostrarQtdMarcas = len(marcasCarros)
print(f'Temos {mostrarQtdMarcas} de marcas de carros no array')
spacePrint()

# SORT()
def mostrarOrdAlpha():
    marcasOrdem = marcasCarros.copy() # CRIA UMA CÓPIA DO ARRAY, NÃO ALTERANDO O ORIGINAL
    marcasOrdem.sort()
    print('Mostrando array em ordem alfabética: ', marcasOrdem)
    return

mostrarOrdAlpha()
print('Original: ', marcasCarros)
spacePrint()

# APPEND()
def incluirNovaMarca(valor):
    marcasCarros.append(valor)
    print(f'{valor} adicionado!')
    print(marcasCarros)
    return

incluirNovaMarca('Lamborghini')
print('Original: ', marcasCarros) # ALTERA O VALOR NO ORIGINAL
spacePrint()

# INDEX()
def mostrarIndexDaMarca(valor):
    for marca in marcasCarros:
        if marca == valor:
            return print('Sua marca está na posição: ', marcasCarros.index(valor))
    
    return print('A marca não está na lista')

mostrarIndexDaMarca(input('Insira uma marca: '))
spacePrint()

arr = [1, 2, 2, 3, 4, 4, 4, 5]

# ITERAÇÃO
def iterandoArray() :
    print('Iterando o array: ')
    for item in arr:
        print(item)

iterandoArray()
spacePrint()

# POP()
def deletandoMarcaEspecifica(valor):
    try:
        marcasCarros.pop(valor)
        return print(marcasCarros)
    except:
        print('Valor não existe')

deletandoMarcaEspecifica(int(input('Insira um index para deletar um carro: ')))

# LÓGICA DE DUPLICADAS
def pegandoDuplicadas():
    counter = Counter(arr) # CONTA QUANTAS VEZES O ITEM FOI REPETIDO
    print('Counter: ', counter.items())
    duplicados = {chave: valor for chave, valor in counter.items() if valor > 1}
    
    somaDosDuplicados = sum(duplicados.values())

    for conjunto in duplicados.items():
        print(f'O valor {conjunto[0]} apareceu {conjunto[1]} vezes')

    print('Soma dos duplicados: ', somaDosDuplicados)

pegandoDuplicadas()
spacePrint()