import db_cidades

cidade = db_cidades.Cidades()
cidade.cod = 31
cidade.uf = 'MG'
cidade.nome = 'Minas gerais'
cidade.habitantes = '20 Milhões'

busca_na_base = db_cidades.session.query(
    db_cidades.Cidades).filter(db_cidades.Cidades.cod == cidade.cod).all()

cidades_nomes = db_cidades.session.query(db_cidades.Cidades.nome).all()

for nome in cidades_nomes:
    print(nome[0])  # RETORNA OS NOMES DAS CIDADES

print('-' * 40)

busca_usando_get = db_cidades.session.query(db_cidades.Cidades).get(31)
print('Cidade buscada por ID, ' + busca_usando_get.nome +
      ' UF: ' + busca_usando_get.uf)

print('-' * 40)

# INSERE NO BANCO DE DADOS SE NÃO ESTIVER CADASTRADO
if len(busca_na_base) < 1:
    db_cidades.session.add(cidade)
    db_cidades.session.commit()  # COMMITA A TRANSAÇÃO
else:
    print('Cidade ' + cidade.nome + ' ja foi adicionada')
