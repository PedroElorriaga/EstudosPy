import db_produtos

produto = db_produtos.Produto()
produto.titulo = 'Iphone 15 pro max'
produto.preco = '8.250.00'
produto.avaliacao = '8'

# INSERE NO BANCO DE DADOS A INSTANCIA PRODUTO
db_produtos.session.add(produto)
db_produtos.session.commit()  # COMMITA A TRANSAÇÃO
