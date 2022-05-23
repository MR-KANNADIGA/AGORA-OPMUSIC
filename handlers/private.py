import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/45578a74150526197c5bb.jpg",
        caption=f"""**𝗧𝗛𝗜𝗦 𝗜𝗦 𝗕𝗘𝗦𝗧 𝗕𝗢𝗧 𝗢𝗙 𝗕𝗥𝗢𝗧𝗛𝗘𝗥𝗦 𝗧𝗘𝗥𝗥𝗜𝗧𝗢𝗥𝗬 𝗠𝗔𝗗𝗘 𝗕𝗬 [𝗕𝗜𝗚 𝗕𝗥𝗢𝗧𝗛𝗘𝗥](https://t.me/MR_AGORA)

𝗖𝗥𝗘𝗔𝗧𝗢𝗥 :- [𝗕𝗜𝗚 𝗕𝗥𝗢𝗧𝗛𝗘𝗥](https://t.me/MR_AGORA)
𝗧𝗘𝗥𝗥𝗜𝗧𝗢𝗥𝗬 :- [𝗖𝗟𝗨𝗕](https://t.me/BROTHERS_TERRITORY)
𝗨𝗣𝗗𝗔𝗧𝗘𝗦 :- [𝗔𝗚𝗢𝗥𝗔](https://t.me/AGORAEMPIRE)

 𝗜𝗙 𝗬𝗢𝗨 𝗪𝗢𝗡𝗧 𝗨𝗡𝗗𝗘𝗥𝗦𝗧𝗔𝗡𝗗 𝗔𝗡𝗬𝗧𝗛𝗜𝗡𝗚 𝗔𝗦 𝗧𝗢 [𝗕𝗜𝗚 𝗕𝗥𝗢𝗧𝗛𝗘𝗥](https://t.me/mr_agora)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗕𝗥𝗢𝗧𝗛𝗘𝗥𝗦 𝗖𝗟𝗨𝗕", url=f"https://t.me/BROTHERS_TERRITORY")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/45578a74150526197c5bb.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup
            [
                [
                    InlineKeyboardButton(
                        "𝙍𝙚𝙥𝙤", url=f"https://t.me/wtf-toxicop")
                ]
            ]
        ),
    )
