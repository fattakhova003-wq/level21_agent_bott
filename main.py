import os
import logging
import httpx

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

from keyboards import (
    keyboard_start,
    keyboard_confirm,
    keyboard_wait,
)

from messages import MESSAGES


logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO
)


BOT_TOKEN = os.getenv("BOT_TOKEN")

OPERATOR_TOKEN = os.getenv("OPERATOR_TOKEN")
OPERATOR_ID = os.getenv("OPERATOR_ID")


START_TEXT = """
🔐 LEVEL 21 SYSTEM

Соединение установлено...

Проверка личности...

██████████ 100%

Доступ подтверждён.

Добро пожаловать, Агент.

Ваша операция готова к запуску.

Нажмите кнопку ниже для получения первого документа.
"""


async def notify_operator(text):

    url = f"https://api.telegram.org/bot{OPERATOR_TOKEN}/sendMessage"

    async with httpx.AsyncClient() as client:

        await client.post(
            url,
            json={
                "chat_id": OPERATOR_ID,
                "text": text
            }
        )



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        START_TEXT,
        reply_markup=keyboard_start
    )



async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()


    if query.data == "document":

        await notify_operator(
            "🟢 АГЕНТ ПРОСНУЛСЯ\n\n"
            "Нажата кнопка:\n"
            "📄 ПОЛУЧИТЬ ПЕРВЫЙ ДОКУМЕНТ"
        )


        await query.edit_message_text(
            MESSAGES["document"],
            reply_markup=keyboard_confirm
        )



    elif query.data == "confirm":

        await notify_operator(
            "📍 АГЕНТ ПОДТВЕРДИЛ ПОЛУЧЕНИЕ\n\n"
            "Первый документ принят."
        )


        await query.edit_message_text(
            MESSAGES["confirm"],
            reply_markup=keyboard_wait
        )



    elif query.data == "wait":

        await notify_operator(
            "🛰 АГЕНТ В РЕЖИМЕ ОЖИДАНИЯ\n\n"
            "Готов получать дальнейшие инструкции."
        )


        await query.edit_message_text(
            MESSAGES["wait"]
        )



def main():

    app = Application.builder().token(BOT_TOKEN).build()


    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )


    app.add_handler(
        CallbackQueryHandler(
            button_handler
        )
    )


    print("LEVEL21 AGENT BOT STARTED")


    app.run_polling()



if __name__ == "__main__":
    main()
