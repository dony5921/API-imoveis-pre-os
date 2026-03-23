from sqlalchemy import Column, Integer, String
from app.database.db import Base

class Imovel(Base):
    __tablename__ = "imoveis"

    id = Column(Integer, primary_key=True)
    bairro = Column(String)
    preco = Column(Integer)
    quartos = Column(Integer)