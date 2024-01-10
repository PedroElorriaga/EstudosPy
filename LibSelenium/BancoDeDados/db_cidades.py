import sqlalchemy
import pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

pymysql.install_as_MySQLdb()
engine = sqlalchemy.create_engine(
    'mysql://pedro:123456@localhost/banco_produtos')
Base = sqlalchemy.ext.declarative.declarative_base()


class Cidades(Base):
    __tablename__ = 'cidades'
    cod = Column(Integer, primary_key=True)
    uf = Column(String(250))
    nome = Column(String(250))
    habitantes = Column(String(250))


Base.metadata.create_all(engine)

# CRIA UMA SESSÃO QUE É RESPONSAVEL POR TRANSFORMAR OBJETOS EM LINHAS DO BANCO DE DADOS
theSession = sessionmaker(bind=engine)
session = theSession()
