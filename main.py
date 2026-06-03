import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Replace with your actual API keys
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY")

async def get_news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Example: Fetching news from an API
    # response = requests.get(f"https://api-football-v1.p.rapidapi.com/v3/news?key={FOOTBALL_API_KEY}")
    await update.message.reply_text("Here is your latest football news: [Your news content here]")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("news", get_news))
    app.run_polling()
