from telegram.ext import ApplicationBuilder, MessageHandler, filters
from telegram import Update
import requests
from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

API_URL = "http://127.0.0.1:8000/ask"

async def handle(update: Update, context):

    text = update.message.text

    response = requests.post(API_URL, json={"question": text})

    answer = response.json()["response"]

    await update.message.reply_text(answer)

app = ApplicationBuilder().token("TELEGRAM_TOKEN").build()

app.add_handler(MessageHandler(filters.TEXT, handle))

app.run_polling()