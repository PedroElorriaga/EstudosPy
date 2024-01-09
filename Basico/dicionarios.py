dicionario = {}

dicionario['TESTE'] = ['1', '2']
dicionario['TESTE2'] = ['3', '4']

print(dicionario)  # OUTPUT {'TESTE': ['1', '2'], 'TESTE2': ['3', '4']}

for chave in dicionario.keys():
    print(chave)

for valor in dicionario.values():
    print(valor)
