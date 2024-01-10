import sqlalchemy
import pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

pymysql.install_as_MySQLdb()
engine = sqlalchemy.create_engine(
    'mysql://pedro:123456@localhost/banco_produtos')
Base = sqlalchemy.ext.declarative.declarative_base()


class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(250))
    preco = Column(String(250))
    avaliacao = Column(String(250))


Base.metadata.create_all(engine)

# CRIA UMA SESSÃO QUE É RESPONSAVEL POR TRANSFORMAR OBJETOS EM LINHAS DO BANCO DE DADOS
theSession = sessionmaker(bind=engine)
session = theSession()
