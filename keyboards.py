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


keyboard_road = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "➡️ ПРОДОЛЖИТЬ ОПЕРАЦИЮ",
                callback_data="road"
            )
        ]
    ]
)


keyboard_hotel = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "🏨 ПОДТВЕРДИТЬ ОТЕЛЬ",
                callback_data="hotel"
            )
        ]
    ]
)


keyboard_aerotube = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "🌪 ЗАПУСТИТЬ АКТИВНОСТЬ",
                callback_data="aerotube"
            )
        ]
    ]
)


keyboard_football = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "⚽ ПЕРЕЙТИ К ИСПЫТАНИЮ",
                callback_data="football"
            )
        ]
    ]
)


keyboard_lounge = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "🛋 ОТКРЫТЬ ДОСТУП",
                callback_data="lounge"
            )
        ]
    ]
)


keyboard_final = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "🔐 ЗАВЕРШИТЬ ОПЕРАЦИЮ",
                callback_data="final"
            )
        ]
    ]
)
