def fatia_de_pizza(tamanho: int):
    fatia = 1
    while fatia <= tamanho:
        yield fatia
        fatia += 1


minha_pizza = fatia_de_pizza(8)

for pedaco in minha_pizza:
    print(pedaco)


print('-' * 60)


def fatia_de_pizza_sem_yield(tamanho: int):
    fatia = 1
    while fatia <= tamanho:
        return fatia
        fatia += 1


minha_pizzinha = fatia_de_pizza_sem_yield(4)

print(minha_pizzinha)
