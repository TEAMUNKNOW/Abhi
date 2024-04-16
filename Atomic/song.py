from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.enums import ChatAction
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaAudio,
                            InputMediaVideo, Message)




def song_markup(_, vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴜᴅɪᴏ",
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text="ᴠɪᴅᴇᴏ",
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="CLOSE_BUTTON", callback_data="close"
            ),
        ],
    ]
    return buttons