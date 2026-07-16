import os
import logging

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
    keyboard_road,
    keyboard_hotel,
    keyboard_aerotube,
    keyboard_football,
    keyboard_lounge,
    keyboard_final,
)

from messages import MESSAGES


logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO
)


BOT_TOKEN = os.getenv("BOT_TOKEN")


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


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        START_TEXT,
        reply_markup=keyboard_start
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()


    if query.data == "document":

        await query.edit_message_text(
            MESSAGES["document"],
            reply_markup=keyboard_confirm
        )


    elif query.data == "confirm":

        await query.edit_message_text(
            MESSAGES["confirm"],
            reply_markup=keyboard_wait
        )


    elif query.data == "wait":

        await query.edit_message_text(
            MESSAGES["wait"]
        )

        await query.message.reply_text(
            MESSAGES["road"],
            reply_markup=keyboard_road
        )


    elif query.data == "road":

        await query.message.reply_text(
            MESSAGES["hotel"],
            reply_markup=keyboard_hotel
        )


    elif query.data == "hotel":

        await query.message.reply_text(
            MESSAGES["aerotube"],
            reply_markup=keyboard_aerotube
        )


    elif query.data == "aerotube":

        await query.message.reply_text(
            MESSAGES["football"],
            reply_markup=keyboard_football
        )


    elif query.data == "football":

        await query.message.reply_text(
            MESSAGES["lounge"],
            reply_markup=keyboard_lounge
        )


    elif query.data == "lounge":

        await query.message.reply_text(
            MESSAGES["final"],
            reply_markup=keyboard_final
        )


    elif query.data == "final":

        await query.message.reply_text(
            MESSAGES["final"]
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
