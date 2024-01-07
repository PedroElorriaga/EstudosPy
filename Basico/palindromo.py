palindromo = [5, 4, 3, 2, 1]

minha_lista = [1, 2, 3, 4, 5]
outra_lista = [1, 2, 4, 3, 5]

def verificar_se_tem_palindromo(sua_lista):
    if not isinstance(sua_lista, list):
        return print('Aceitamos apenas listas')

    if palindromo == sua_lista:
        return print('Listas iguais, não palíndromo')
    
    index = 0
    for dado in sua_lista[::-1]:
        if dado == palindromo[index]:
            index += 1
        
        else:
            return print('Não é um palíndromo')
    
    return print('É um palíndromo')

verificar_se_tem_palindromo(minha_lista) # OUTPUT É um palíndromo
verificar_se_tem_palindromo(outra_lista) # OUTPUT Não é um palíndromo
verificar_se_tem_palindromo([5, 4, 3, 2, 1]) # OUTPUT Listas iguais, não palíndromo
verificar_se_tem_palindromo('Mercedes') # OUTPUT Aceitamos apenas listas