from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ButtonStyle

def start_button():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "охота",
                    callback_data="hunt",
                    icon_custom_emoji_id=6028477497518068483
                ),
                InlineKeyboardButton(
                    "арена",
                    callback_data="arena",
                    icon_custom_emoji_id=6028477497518068484
                ),
                InlineKeyboardButton(
                    "инвентарь",
                    callback_data="inventory",
                    icon_custom_emoji_id=6028477497518068485
                ),
            ],
            [
                InlineKeyboardButton(
                    "рейтинг",
                    callback_data="rating",
                    icon_custom_emoji_id=6028477497518068486
                ),
                InlineKeyboardButton(
                    "топ",
                    callback_data="top",
                    icon_custom_emoji_id=6028477497518068487
                ),
                InlineKeyboardButton(
                    "рынок",
                    callback_data="market",
                    icon_custom_emoji_id=6028477497518068488
                ),
            ],
            [
                InlineKeyboardButton(
                    "коллекция",
                    callback_data="collection",
                    icon_custom_emoji_id=6028477497518068489
                ),
                InlineKeyboardButton(
                    "донат",
                    callback_data="donate",
                    style=ButtonStyle.PRIMARY,  # ✅ ONLY HERE
                    icon_custom_emoji_id=6028477497518068490
                ),
                InlineKeyboardButton(
                    "настройки",
                    callback_data="settings",
                    icon_custom_emoji_id=6028477497518068491
                ),
            ],
            [
                InlineKeyboardButton(
                    "комьюнити",
                    callback_data="community",
                    style=ButtonStyle.PRIMARY,  # ✅ ONLY HERE
                    icon_custom_emoji_id=6028477497518068492
                ),
            ]
        ]
    )