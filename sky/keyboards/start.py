from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ButtonStyle

start_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("охота", callback_data="hunt"),
            InlineKeyboardButton("арена", callback_data="arena"),
            InlineKeyboardButton("инвентарь", callback_data="inventory"),
        ],
        [
            InlineKeyboardButton("рейтинг", callback_data="rating"),
            InlineKeyboardButton("топ", callback_data="top"),
            InlineKeyboardButton("рынок", callback_data="market"),
        ],
        [
            InlineKeyboardButton("коллекция", callback_data="collection"),
            InlineKeyboardButton("донат", callback_data="donate", style=ButtonStyle.PRIMARY),
            InlineKeyboardButton("настройки", callback_data="settings"),
        ],
        [
            InlineKeyboardButton("комьюнити", callback_data="community", style=ButtonStyle.PRIMARY),
        ],
    ]
)