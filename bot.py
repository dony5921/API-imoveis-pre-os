from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters
import requests
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
# print("TOKEN:", TOKEN)
API_URL = "http://localhost:8000"

async def responder(update: Update, context):
    texto = update.message.text.lower()

    # 🔹 comando: baratos
    if "barato" in texto:
        url = f"{API_URL}/baratos"
        dados = requests.get(url).json()

        if not dados.get("baratos"):
            await update.message.reply_text("Nenhum imóvel barato encontrado")
            return

        resposta = " Imóveis baratos:\n\n"

        for i in dados["baratos"]:
            resposta += f"{i['bairro']} - R${i['preco']}\n"

        await update.message.reply_text(resposta)
        return

    # 🔹 comando: bairro
    if "bairro" in texto:
        bairro = texto.replace("bairro", "").strip()

        url = f"{API_URL}/imoveis/{bairro}"
        dados = requests.get(url).json()

        resposta = f" Imóveis em {bairro}:\n\n"

        for i in dados:
            resposta += f"R${i['preco']}\n"

        await update.message.reply_text(resposta)
        return

    # 🔹 fallback
    await update.message.reply_text(
        "Digite:\n"
        "👉 baratos\n"
        "👉 bairro centro"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, responder))

app.run_polling()