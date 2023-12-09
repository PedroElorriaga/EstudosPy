# Dataclass fornece um decorador e funções
# para adicionar automaticamente métodos especiais
# como o __init__() e __repr()__

from dataclasses import dataclass

@dataclass
class Product:

    preco: float
    nome: str
    quantidade: int
    pedidos = [{'Carrinho': {'Nome': 'Feijão', 'Preço': 18.50, 'Quantidade': 30}, 'id': 0},]

    def acrescentar_produto_no_carrinho(self):
        carrinho = {
            'Carrinho': {
            'Nome': self.nome,
            'Preço': self.preco,
            'Quantidade': self.quantidade
            },
            'id': len(self.pedidos)
        }

        self.pedidos.append(carrinho)
        
        if __name__ == '__main__':
            print(f'Produto: "{self.nome}" foi adicionado no carrinho!')

        return True

    def aplcar_desconto(self, id, percentual):
        localizar_id = [item for item in self.pedidos if item['id'] == id] #LIST COMPREHENSIONS

        if len(localizar_id) == 0:
            return print('Pedido não localizado!')
        
        for item in localizar_id:
            nome = item['Carrinho']['Nome']
            preco = item['Carrinho']['Preço']
            self.preco = preco - (self.preco * (percentual / 100)) # DESCONTO
            self.preco = "%.2f" % self.preco # DECIMAL 2 CASAS]]

            self.preco = float(self.preco)
            item['Carrinho']['Preço'] = self.preco # MODIFICANDO O DICT

        if __name__ == '__main__':
        
            print(f'O produto: {nome} de R${preco} teve desconto de {percentual}%')
            print(f'{nome} agora está: R${self.preco}')
        
        return self.preco

if __name__ == '__main__':
    shop = Product(10.99, 'Bala Fini', 7)
    shop.acrescentar_produto_no_carrinho()
    print(f'Pedidos: {shop.pedidos}')
    print('-' * 60)

    shop.aplcar_desconto(1, 20)
    print('-' * 60)

    print(shop.pedidos)