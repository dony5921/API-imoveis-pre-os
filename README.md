# 🏠 API de Imóveis com Análise Inteligente de Preços

API REST desenvolvida em Python para coleta, armazenamento e análise de preços de imóveis, integrada com um bot no Telegram para consultas em tempo real.

---

## 🚀 Funcionalidades

- 📊 Análise de preços de imóveis
- 🏠 Identificação de imóveis abaixo da média (oportunidades)
- 🔎 Consulta por bairro
- 🤖 Integração com bot do Telegram
- ⚡ Respostas em tempo real

---

## 🧠 Inteligência do Sistema

O sistema calcula a média de preços dos imóveis e identifica automaticamente aqueles com valores abaixo da média, auxiliando na tomada de decisão.

---

## 🛠️ Tecnologias

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Telegram Bot API

---

## ▶️ Como executar

```bash
git clone https://github.com/SEU_USUARIO/API-imoveis-pre-os.git
cd API-imoveis-pre-os

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
