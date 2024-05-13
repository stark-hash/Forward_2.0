import os
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
import sys

START_MSG="Hi {}, This is a simple bot to forward all messages from one channel to other!"
HELP_MSG="Available commands:-\n\n/index - To index a channel\n/forward - To start forwarding\n/total - Count total messages in DB\n/status - Check Current status\n/help - Help data\n/stop - To stop all running processes. \n\nUse /index to index messages from a channel to database.\n\nAfter indexing you can start forwarding by using /forward.\n\n<b>Note:</b>\nYou will require the following data to index a channel:-\n\n<b>SKIP_NO</b>:-From where you want to start Forwarding files.Give 0 if from starting\n\n<b>Caption</b>:- Custom Caption for forwarded files. Use 0 to use default captions."
buttons=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Help", callback_data="help"),
                InlineKeyboardButton("How Does This Works?", callback_data="abt")
            ],
            [
                InlineKeyboardButton("Source Code", url="https://youtu.be/xvFZjo5PgG0"),
                InlineKeyboardButton("Report a Bug", url="https://t.me/TGTesla")
            ]
        ]
        )

@Client.on_message(filters.private & filters.command('start'))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=START_MSG.format(
                message.from_user.first_name),
        reply_markup=buttons,
        parse_mode="html")


@Client.on_message(filters.command("stop"))
async def stop_button(bot, message):

    if str(message.from_user.id) not in Config.OWNER_ID:
        return
    msg = await bot.send_message(
        text="Stoping all processes...",
        chat_id=message.chat.id
    )
    await asyncio.sleep(1)
    await msg.edit("All Processes Stopped and Restarted")
    os.execl(sys.executable, sys.executable, *sys.argv)


@Client.on_message(filters.private & filters.command('help'))
async def help(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=HELP_MSG,
        parse_mode="html")


@Client.on_callback_query(filters.regex(r'^help$'))
async def cb_help(bot, cb):
    await cb.message.edit_text(HELP_MSG)



@Client.on_callback_query(filters.regex(r'^abt$'))   
async def cb_abt(bot, cb):
    await cb.message.edit_text("Talking is cheap, Read Code.",
    reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Source", url="https://youtu.be/xvFZjo5PgG0"),
            ]
        ]
    )
    )
