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
            InlineKeyboardButton(text=_["S_B_11"], web_app=WebAppInfo(url=config.PROFESSORRR)),
            InlineKeyboardButton(text=_["S_B_12"], web_app=WebAppInfo(url=config.PROFESSORSTATUS)),
        ],
        [
            InlineKeyboardButton(text=_["S_B_13"], web_app=WebAppInfo(url=config.PROFESSORBOTS)),
            InlineKeyboardButton(text=_["S_B_14"], web_app=WebAppInfo(url=config.PROFESSORSMM)),
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], web_app=WebAppInfo(url=config.PROFESSOR)),
        ],
    ]
    return buttons
