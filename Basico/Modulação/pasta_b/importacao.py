import sys
import os


""" OUTPUT -> Users\pedro.elorriaga\Downloads\EstudosPy\Basico\Modulação\pasta_b """
caminho_arquivo = os.path.dirname(__file__) # PEGA O CAMINHO DO ARQUIVO ATUAL

""" OUTPUT -> Users\pedro.elorriaga\Downloads\EstudosPy\Basico\Modulação\pasta_b\..\pasta_a"""
pasta_a_caminho = os.path.join(caminho_arquivo, '..' ) # PEGA O CAMINHO PARA MODULÇÃO

sys.path.append(pasta_a_caminho) # ADICIONA O CAMINHO NO sys.path

from pasta_a.exportacao import Product

test = Product(1.90, 'Bala', 6)
test.acrescentar_produto_no_carrinho()
test.aplcar_desconto(1, 50)

print(test.pedidos)