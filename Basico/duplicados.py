from sintaxe import clear, spacePrint

clear()
lista = [10, 5, 4, 8, 2, 4, 3, 6, 2, 4]

def verificar_duplicados(lista):
    if not isinstance(lista, list):
        return print('Favor colocar uma lista')

    lista_sem_duplicados = list(set([dado for dado in lista]))
    return print(lista_sem_duplicados)

verificar_duplicados(lista)
spacePrint()
