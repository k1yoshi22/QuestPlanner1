import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes


TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    try:
        response = requests.post(
            "http://backend:8000/ai",
            json={"message": user_message},
            timeout=60
        )

        data = response.json()
        answer = data.get("response") or data.get("error") or "Ошибка ответа"

    except Exception as e:
        answer = f"Ошибка: {e}"

    await update.message.reply_text(answer)


def main():
    print("TOKEN:", TELEGRAM_BOT_TOKEN)

    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("БОТ ЗАПУЩЕН")
    app.run_polling()


if __name__ == "__main__":
    main()
