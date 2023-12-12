import unittest
from selenium import webdriver
from dataclasses import is_dataclass
from dataClass import Product


class ProductTestes(unittest.TestCase):

    def setUp(self):
        self.product = Product(5, 'Amendoim', 2)
        return print('Executando testes')

    def test_if_product_is_dataclass(self):
        self.assertTrue(is_dataclass(Product))

    def test_constructor(self):
        self.assertEqual(self.product.preco, 5)
        self.assertEqual(self.product.nome, 'Amendoim')
        self.assertEqual(self.product.quantidade, 2)

    def test_add_to_cart(self):
        self.assertTrue(self.product.acrescentar_produto_no_carrinho())

    def test_take_discount(self):
        self.product.aplcar_desconto(1, 50)
        self.assertEqual(self.product.preco, 2.50)

    def tearDown(self):
        print('Teste finalizado')

if __name__ == '__main__':
    unittest.main()
    