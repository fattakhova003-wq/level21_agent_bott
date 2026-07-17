from telegram import InlineKeyboardButton, InlineKeyboardMarkup


keyboard_start = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "📄 ПОЛУЧИТЬ ПЕРВЫЙ ДОКУМЕНТ",
                callback_data="document"
            )
        ]
    ]
)


keyboard_confirm = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "✅ ПОДТВЕРДИТЬ ПОЛУЧЕНИЕ",
                callback_data="confirm"
            )
        ]
    ]
)


keyboard_wait = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "🛰 ОЖИДАТЬ ДАЛЬНЕЙШИХ ИНСТРУКЦИЙ",
                callback_data="wait"
            )
        ]
    ]
)
