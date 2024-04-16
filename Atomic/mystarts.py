#ignore this file

from telethon import events, Button
from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.enums import ChatAction
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaAudio,
                            InputMediaVideo, Message)




async def start_srb(event, st):
    await event.reply(st, 
                      buttons=[
                              [Button.inline("SET THUMB.", data="set"),
                               Button.inline("REM THUMB.", data="rem")],
                              [Button.url("DEV", url="t.me/MaheshChauhan")]])
                              
    
async def vc_menu(event):
    await event.edit("**VIDEO CONVERTOR v1.4**", 
                    buttons=[
                        [Button.inline("info.", data="info"),
                         Button.inline("SOURCE", data="source")],
                        [Button.inline("NOTICE.", data="notice"),
                         Button.inline("Main.", data="help")],
                        [Button.url("DEVELOPER", url="t.me/MaheshChauhan")]])
    
