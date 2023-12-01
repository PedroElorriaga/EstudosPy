from sintaxe import clear, spacePrint
# LAMBDA É UMA PEQUENA FUNÇÃO ANONIMA, QUE SÓ PODE TER UMA EXPRESSÃO

clear()

lambdaQuadrado = lambda x: x * 2

print(lambdaQuadrado(2)) # 4
spacePrint()

duplicarNumeros = lambda x,y: x * y

print(duplicarNumeros(5,5))
spacePrint()
