#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) L_s_meena

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types.bots_and_keyboards import InlineKeyboardButton, InlineKeyboardMarkup


@pyrogram.Client.on_message(pyrogram.filters.command(["help"]))
async def help_user(bot, update):
    if update.from_user.id in Config.AUTH_USERS:
        # logger.info(update)
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.HELP_USER,
            parse_mode="html",
            disable_web_page_preview=True,
            reply_to_message_id=update.message_id
        )


@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))
async def start(bot, update):
    if update.from_user.id in (Config.AUTH_USERS & Config.L_S_MEENA):
        # logger.info(update)
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.L_S_MEENA_TEXT.format(update.from_user.first_name),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("â¡ï¸Åğ²ğ­ğ­ğ¬ğ¯ğ±", url="https://t.me/CHATWITHANOTHERbot"),
                        InlineKeyboardButton("âª ï¼¹ï¼´ âª", url="https://youtube.com/@L_S_MEENA"),
                        InlineKeyboardButton("â¡ï¸ Uğğğğe", url="https://t.me/CHATWITHANOTHERbot"),
                    ],
                    [InlineKeyboardButton("â­ğ¢ ğ ğ¾ ğ² ğ ğ° ğ» ğ¢â­", url="https://t.me/CHATWITHANOTHERbot")],
                    [InlineKeyboardButton("ğ¦ â­ââââ«â¦â¦ O W N E R â¦â¦â£ââââ­ ğ¦", url="https://t.me/CHATWITHANOTHERbot")],
                ]
            ),
            reply_to_message_id=update.message_id
        )
    elif update.from_user.id in Config.AUTH_USERS:
        # logger.info(update)
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.START_TEXT.format(update.from_user.first_name),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("â¡ï¸Åğ²ğ­ğ­ğ¬ğ¯ğ±", url="https://t.me/CHATWITHANOTHERbot"),
                        InlineKeyboardButton("âª ï¼¹ï¼´ âª", url="https://youtube.com/@L_S_MEENA"),
                        InlineKeyboardButton("â¡ï¸ Uğğğğe", url="https://t.me/CHATWITHANOTHERbot"),
                    ],
                    [InlineKeyboardButton("â­ğ¢ ğ ğ¾ ğ² ğ ğ° ğ» ğ¢â­", url="https://t.me/CHATWITHANOTHERbot")],
                    [InlineKeyboardButton("ğ¦ â­ââââ«â¦â¦ O W N E R â¦â¦â£ââââ­ ğ¦", url="https://t.me/CHATWITHANOTHERbot")],
                ]
            ),
            reply_to_message_id=update.message_id
        )
    else:
        # logger.info(update) ==         
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.L_S_MEENA_START_TEXT.format(update.from_user.first_name),
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("ğ¦ â­ââââ«â¦â¦ O W N E R â¦â¦â£ââââ­ ğ¦", url="https://t.me/CHATWITHANOTHERbot")],
                    [
                        InlineKeyboardButton("âââââ UPDATE âââââ", url="https://t.me/CHATWITHANOTHERbot"),
                    ],
                    [InlineKeyboardButton("â­ğ¢ ğ ğ¾ ğ² ğ ğ° ğ» ğ¢â­", url="https://t.me/CHATWITHANOTHERbot")],
                ]
            ),
            reply_to_message_id=update.message_id
        )
         
