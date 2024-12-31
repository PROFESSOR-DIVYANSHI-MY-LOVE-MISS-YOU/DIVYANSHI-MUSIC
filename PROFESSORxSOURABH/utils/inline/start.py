from pyrogram.types import InlineKeyboardButton
from telegram import WebAppInfo

import config
from PROFESSORxSOURABH import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], web_app=WebAppInfo(url=config.PROFESSOR)),
            InlineKeyboardButton(text=_["S_B_2"], web_app=WebAppInfo(url=config.PROFESSOR)),
        ],
        [
            InlineKeyboardButton(text=_["S_B_7"], web_app=WebAppInfo(url=config.PROFESSOR)),
            InlineKeyboardButton(text=_["S_B_10"], web_app=WebAppInfo(url=config.PROFESSOR)),
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], web_app=WebAppInfo(url=config.PROFESSOR)),
        ],
    ]
    return buttons
