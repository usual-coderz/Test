from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ButtonStyle

def start_button():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "охота",
                    callback_data="hunt",
                    icon_custom_emoji_id=5434121252874756456
                ),
                InlineKeyboardButton(
                    "арена",
                    callback_data="arena",
                    icon_custom_emoji_id=5420315771991497307
                ),
                InlineKeyboardButton(
                    "инвентарь",
                    callback_data="inventory",
                    icon_custom_emoji_id=5449428597922079323
                ),
            ],
            [
                InlineKeyboardButton(
                    "рейтинг",
                    callback_data="rating",
                    icon_custom_emoji_id=5332679872009484448
                ),
                InlineKeyboardButton(
                    "топ",
                    callback_data="top",
                    icon_custom_emoji_id=5028746137645876535
                ),
                InlineKeyboardButton(
                    "рынок",
                    callback_data="market",
                    icon_custom_emoji_id=5246762912428603768
                ),
            ],
            [
                InlineKeyboardButton(
                    "коллекция",
                    callback_data="collection",
                    icon_custom_emoji_id=4956721670690702265
                ),
                InlineKeyboardButton(
                    "донат",
                    callback_data="donate",
                    style=ButtonStyle.PRIMARY,  # ✅ ONLY HERE
                    icon_custom_emoji_id=6005661956931850799
                ),
                InlineKeyboardButton(
                    "настройки",
                    callback_data="settings",
                    icon_custom_emoji_id=5341715473882955310
                ),
            ],
            [
                InlineKeyboardButton(
                    "комьюнити",
                    url="https://t.me/Nexacoders",
                    style=ButtonStyle.PRIMARY,  # ✅ ONLY HERE
                    icon_custom_emoji_id=5447410659077661506
                ),
            ]
        ]
    )