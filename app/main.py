from fastapi import FastAPI
from app.database.db import Base, engine, SessionLocal
from app.models.imovel import Imovel

app = FastAPI()

# cria banco automaticamente
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"msg": "API rodando"}


@app.get("/imoveis")
def listar():
    db = SessionLocal()
    dados = db.query(Imovel).all()

    return [{"bairro": i.bairro, "preco": i.preco} for i in dados]


@app.get("/analise")
def analise():
    db = SessionLocal()
    imoveis = db.query(Imovel).all()

    # evitar erro se não tiver dados
    if len(imoveis) == 0:
        return {"msg": "Nenhum imóvel encontrado"}

    media = sum(i.preco for i in imoveis) / len(imoveis)

    resultado = []

    for i in imoveis:
        if i.preco < media:
            status = "barato"
        else:
            status = "caro"

        resultado.append({
            "bairro": i.bairro,
            "preco": i.preco,
            "status": status
        })

    return {
        "media": media,
        "dados": resultado
    }
    
@app.get("/baratos")
def baratos():
    db = SessionLocal()
    imoveis = db.query(Imovel).all()
    if len(imoveis) == 0:
        return {"msg": "Nenhum imóvel encontrado"}


    media = sum(i.preco for i in imoveis) / len(imoveis)

    baratos = []

    for i in imoveis:
        if i.preco < media:
            baratos.append({
                "bairro": i.bairro,
                "preco": i.preco
            })

    return {"baratos": baratos}

@app.get("/imoveis/{bairro}")
def por_bairro(bairro: str):
    db = SessionLocal()
    dados = db.query(Imovel).filter(Imovel.bairro == bairro).all()

    return [{"bairro": i.bairro, "preco": i.preco} for i in dados]