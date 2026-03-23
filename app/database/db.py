from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# cria o banco (arquivo imoveis.db)
engine = create_engine("sqlite:///imoveis.db")

# cria conexão com o banco
SessionLocal = sessionmaker(bind=engine)

# base para criar tabelas
Base = declarative_base()