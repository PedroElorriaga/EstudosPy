from sintaxe import spacePrint, clear

clear()

texto_1 = 'Testando o split, no python'
print(texto_1.split()) # OUTPUT ['Testando', 'o', 'split', 'no', 'python']
spacePrint()

print(texto_1.split(',')) # OUTPUT ['Testando o split', ' no python']
spacePrint()

print(texto_1.split()[4]) # OUTPUT python
spacePrint()

teste = ['Teste' + str(i) for i in range(1,-1,-1)] 
print(teste) # ['Teste1', 'Teste0']

teste = ['Teste' + str(i) for i in range(5,2,-1)] 
print(teste) # ['Teste5', 'Teste4', 'Teste3', 'Teste2']