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
        caption=f"""**𝙔𝙚 𝘿𝙖𝙣𝙜𝙚𝙧𝙤𝙪𝙨 𝙠𝙖 𝙗𝙚𝙨𝙩💕𝙢𝙪𝙨𝙞𝙘 𝙗𝙤𝙩 𝙝𝙖𝙞💔 = [𝙏𝙤𝙭𝙞𝙘](https://t.me/wtf-toxicop)

𝘾𝙧𝙚𝙖𝙩𝙤𝙧 :- [𝙏𝙤𝙭𝙞𝙘](https://t.me/wtf_toxicop
𝙁𝙞𝙜𝙝𝙩𝙞𝙣𝙜 :- [𝙂𝙧𝙤𝙪𝙥](https://t.me/Dangerousfighters)
𝙪𝙥𝙙𝙖𝙩𝙚𝙨 :- [𝘿𝙖𝙣𝙜𝙚𝙧𝙤𝙪𝙨](https://t.me/DANGEROUSFIGHTER)

💞𝘼𝙜𝙖𝙧 𝙖𝙥𝙠𝙤 𝙠𝙤𝙞 𝙨𝙖𝙢𝙖𝙨𝙮𝙖 𝙝𝙤 𝙩𝙤𝙝 𝙤𝙬𝙣𝙚𝙧 𝙨𝙚😈𝙘𝙤𝙣𝙩𝙖𝙘𝙩 𝙠𝙖𝙧𝙤💘 = [𝙏𝙤𝙭𝙞𝙘](https://t.me/wtf-toxicop)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝘼𝙥𝙣𝙖 𝙜𝙝𝙖𝙧", url=f"https://t.me/Dangerousfighters")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/45578a74150526197c5bb.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙍𝙚𝙥𝙤", url=f"https://t.me/wtf-toxicop")
                ]
            ]
        ),
    )
