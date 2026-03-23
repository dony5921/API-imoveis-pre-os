from app.database.db import SessionLocal
from app.models.imovel import Imovel

db = SessionLocal()

imoveis = [
    Imovel(bairro="Centro", preco=200000, quartos=2),
    Imovel(bairro="Paulista", preco=250000, quartos=3),
    Imovel(bairro="Centro", preco=180000, quartos=2),
    Imovel(bairro="Jardim", preco=300000, quartos=4),
]

db.add_all(imoveis)
db.commit()

print("Dados inseridos com sucesso!")