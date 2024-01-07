from sintaxe import spacePrint, clear

clear()
lista_varias_formas = ['ABC', 123, 'FETUCIA', 6.7, 300, 'HELLO WORLD']
lista_somente_numeros = [variavel for variavel in lista_varias_formas if isinstance(variavel, (int, float))]

print(lista_somente_numeros) # OUTPUT [123, 6.7, 300]
spacePrint()

lista_nomes = ['Pedro', 'Leonardo', 'Thais', 'Juliana', 'Renan', 'Welton', 'Beatriz', 'Paulo']
lista_somente_letra_a = [nome for nome in lista_nomes if 'a' in nome]
lista_somente_letra_t_a = [nome for nome in lista_nomes if 'a' in nome and 't' in nome]

print(lista_somente_letra_a) # OUTPUT ['Leonardo', 'Thais', 'Juliana', 'Renan', 'Beatriz', 'Paulo']
print(lista_somente_letra_t_a) # OUTPUT ['Beatriz']
spacePrint()

lista_somente_strings = [dado for dado in lista_varias_formas if isinstance(dado, str)]
print(lista_somente_strings)