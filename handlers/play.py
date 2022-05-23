import os
from os import path
from pyrogram import Client, filters
from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from callsmusic import callsmusic, queues
from callsmusic.callsmusic import client as USER
from helpers.admins import get_administrators
import requests
import aiohttp
from youtube_search import YoutubeSearch
import converter
from downloaders import youtube
from config import DURATION_LIMIT
from helpers.filters import command
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
import aiofiles
import ffmpeg
from PIL import Image, ImageFont, ImageDraw
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream


def transcode(filename):
    ffmpeg.input(filename).output("input.raw", format='s16le', acodec='pcm_s16le', ac=2, ar='48k').overwrite_output().run() 
    os.remove(filename)

# Convert seconds to mm:ss
def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


# Change image size
def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

async def generate_cover(requested_by, title, views, duration, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()


    image1 = Image.open("./background.png")
    image2 = Image.open("etc/foreground.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save("temp.png")
    img = Image.open("temp.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("etc/font.otf", 32)
    draw.text((190, 550), f"Title: {title}", (255, 255, 255), font=font)
    draw.text(
(190, 590), f"Duration: {duration}", (255, 255, 255), font=font
    )
    draw.text((190, 630), f"Views: {views}", (255, 255, 255), font=font)
    draw.text((190, 670),
 f"Added By: {requested_by}",
 (255, 255, 255),
 font=font,
    )
    img.save("final.png")
    os.remove("temp.png")
    os.remove("background.png")



@Client.on_message(
    command(["play"])
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def play(_, message: Message):
    global que
    global useer

    lel = await message.reply("🔎 **𝙎𝙤𝙣𝙜 𝙙𝙝𝙪𝙣𝙙𝙧𝙖 𝙝𝙪 𝙨𝙖𝙗𝙖𝙧 𝙧𝙖𝙠𝙝𝙤...**")

    administrators = await get_administrators(message.chat)
    chid = message.chat.id

    try:
        user = await USER.get_me()
    except:
        user.first_name = "Toxic_MusicX"
    usar = user
    wew = usar.id
    try:
        await _.get_chat_member(chid, wew)
    except:
        for administrator in administrators:
            if administrator == message.from_user.id:
                try:
                    invitelink = await _.export_chat_invite_link(chid)
                except:
                    await lel.edit(
                        "😒𝙥𝙚𝙝𝙡𝙚 𝙖𝙙𝙢𝙞𝙣 𝙩𝙤𝙝 𝙗𝙖𝙣𝙖𝙤 𝙮𝙧𝙡😞")
                    return

                try:
                    await USER.join_chat(invitelink)
                    await USER.send_message(
                        message.chat.id, "** 𝙃𝙪𝙢💞𝙖𝙜𝙮𝙚 𝙨𝙬𝙖𝙜𝙖𝙩💘𝙩𝙤𝙝 𝙠𝙖𝙧𝙤 𝙝𝙖𝙢𝙖𝙧𝙖💔**")

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    await lel.edit(
                        f"<b> 𝙁𝙡𝙤𝙤𝙙 𝙡𝙖𝙜𝙖 𝙝𝙖𝙞 /𝙀𝙧𝙧𝙤𝙧💋𝙗𝙝𝙞 𝙝𝙤𝙨𝙠𝙩𝙖 𝙮𝙖 𝙛𝙞𝙧 𝙖𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩💔𝙗𝙖𝙣 𝙝𝙤𝙜𝙖 𝙬𝙖𝙧𝙣𝙖 𝙤𝙬𝙣𝙚𝙧 𝙨𝙚 𝙘𝙤𝙣𝙩𝙖𝙘𝙩 𝙠𝙖𝙧𝙚💞 :- ✨ [Toxic](https://t.me/wtf_toxicop) ❤️🥀 :) ")
    try:
        await USER.get_chat(chid)
    except:
        await lel.edit(
            f"<i>Hey {user.first_name}, 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩💔 𝙘𝙝𝙖𝙩 𝙢𝙚𝙞𝙣 𝙣𝙞 𝙝𝙖𝙞 𝘼𝙙𝙢𝙞𝙣💘 𝙠𝙤 𝙗𝙤𝙡𝙤 /𝙥𝙡𝙖𝙮 𝙡𝙞𝙠𝙝𝙚 𝙮𝙖 𝙤𝙬𝙣𝙚𝙧 𝙨𝙚 𝙘𝙤𝙣𝙩𝙖𝙘𝙩 𝙠𝙖𝙧𝙚💞:- [Toxic](https://t.me/wtf_toxicop) ❤️🥀 </i>")
        return
    
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"**❰ ° 𝐒𝐨𝐧𝐠 🎸 ° ❱ 𝐋𝐨𝐧𝐠𝐞𝐫 𝐓𝐡𝐚𝐧 {DURATION_LIMIT} 𝐌𝐢𝐧𝐮𝐭𝐞'𝐒 𝐀𝐫𝐞𝐧'𝐭 𝐀𝐥𝐥𝐨𝐰𝐞𝐝 𝐓𝐨 𝐏𝐥𝐚𝐲 ▶ ❤️🥀**"
            )

        file_name = get_file_name(audio)
        title = file_name
        thumb_name = "https://telegra.ph/file/e57156ccc7571599a1c4f.jpg"
        thumbnail = thumb_name
        duration = round(audio.duration / 60)
        views = "Locally added"

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                            text="𝗨𝗣𝗗𝗔𝗧𝗘𝗦",
                            url=f"https://t.me/Brothers_territory")
               ],
               [
                    InlineKeyboardButton(
                            text="𝗕𝗜𝗚 𝗕𝗥𝗢𝗧𝗛𝗘𝗥",
                            url=f"https://t.me/mr_agora"),
                            
                    InlineKeyboardButton(
                            text="𝗕𝗥𝗢𝗧𝗛𝗘𝗥𝗦",
                            url=f"https://t.me/Brothers_territory")
               ],
               [
                        InlineKeyboardButton(
                            text="𝗦𝗨𝗣𝗣𝗢𝗥𝗧",
                            url=f"https://t.me/Brothers_territory")
                   
                ]
            ]
        )

        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name))
            else file_name
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

            keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                            text="𝙐𝙥𝙙𝙖𝙩𝙚𝙨",
                            url=f"https://t.me/DANGEROUSFIGHTER")
               ],
               [
                    InlineKeyboardButton(
                            text="𝘾𝙧𝙚𝙖𝙩𝙤𝙧",
                            url=f"https://t.me/wtf_toxicop"),
                            
                    InlineKeyboardButton(
                            text="𝙏𝙤𝙭𝙞𝙘𝙦𝙪𝙚𝙚𝙣",
                            url=f"https://t.me/wtf_toxicqueen")
               ],
               [
                        InlineKeyboardButton(
                            text="𝙎𝙪𝙥𝙥𝙤𝙧𝙩",
                            url=f"https://t.me/Dangerousfighters")
                   
                ]
            ]
        )

        except Exception as e:
            title = "NaN"
            thumb_name = "https://te.legra.ph/file/4d412495ab546f9062898.jpg"
            duration = "NaN"
            views = "NaN"
            keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                            text="𝙐𝙥𝙙𝙖𝙩𝙚𝙨",
                            url=f"https://t.me/DANGEROUSFIGHTER")
               ],
               [
                    InlineKeyboardButton(
                            text="𝘾𝙧𝙚𝙖𝙩𝙤𝙧",
                            url=f"https://t.me/wtf_toxicop"),
                            
                    InlineKeyboardButton(
                            text="𝙏𝙤𝙭𝙞𝙘𝙦𝙪𝙚𝙚𝙣",
                            url=f"https://t.me/wtf_toxicqueen")
               ],
               [
                        InlineKeyboardButton(
                            text="𝙎𝙪𝙥𝙥𝙤𝙧𝙩",
                            url=f"https://t.me/Dangerousfighters")
                   
                ]
            ]
        )

        if (dur / 60) > DURATION_LIMIT:
            await lel.edit(
                f"**❰ ° 𝐒𝐨𝐧𝐠 🎸 ° ❱ 𝐋𝐨𝐧𝐠𝐞𝐫 𝐓𝐡𝐚𝐧 {DURATION_LIMIT} 𝐌𝐢𝐧𝐮𝐭𝐞'𝐒 𝐀𝐫𝐞𝐧'𝐭 𝐀𝐥𝐥𝐨𝐰𝐞𝐝 𝐓𝐨 𝐏𝐥𝐚𝐲 ▶ ❤️🥀**"
            )
            return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(youtube.download(url))
    else:
        if len(message.command) < 2:
            return await lel.edit(
                "😜𝘼𝙖𝙥 𝙠𝙤𝙣𝙨𝙖 𝙨𝙤𝙣𝙜💔𝙗𝙖𝙟𝙖𝙣𝙖 𝙘𝙝𝙖𝙝𝙩𝙚 𝙝𝙤😍😍**"
            )
        await lel.edit("🔎")
        query = message.text.split(None, 1)[1]
        # print(query)
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            await lel.edit(
                "**🌸°💔 𝘼𝙥𝙣𝙚 𝙜𝙖𝙡𝙖𝙩 𝙨𝙤𝙣𝙜💞𝙣𝙖𝙢𝙚 𝙡𝙞𝙠𝙝𝙖 𝙝𝙖𝙞 𝙘𝙝𝙚𝙘𝙠 𝙠𝙖𝙧𝙣𝙖💔**"
            )
            print(str(e))
            return

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                            text="𝙐𝙥𝙙𝙖𝙩𝙚𝙨",
                            url=f"https://t.me/DANGEROUSFIGHTER")
               ],
               [
                    InlineKeyboardButton(
                            text="𝘾𝙧𝙚𝙖𝙩𝙤𝙧",
                            url=f"https://t.me/wtf_toxicop"),
                            
                    InlineKeyboardButton(
                            text="𝙏𝙤𝙭𝙞𝙘𝙦𝙪𝙚𝙚𝙣",
                            url=f"https://t.me/wtf_toxicqueen")
               ],
               [
                        InlineKeyboardButton(
                            text="𝙎𝙪𝙥𝙥𝙤𝙧𝙩",
                            url=f"https://t.me/Dangerousfighters")
                   
                ]
            ]
        )

        if (dur / 60) > DURATION_LIMIT:
            await lel.edit(
                f"**❰ ° 𝐒𝐨𝐧𝐠 🎸 ° ❱ 𝐋𝐨𝐧𝐠𝐞𝐫 𝐓𝐡𝐚𝐧 {DURATION_LIMIT} 𝐌𝐢𝐧𝐮𝐭𝐞'𝐒 𝐀𝐫𝐞𝐧'𝐭 𝐀𝐥𝐥𝐨𝐰𝐞𝐝 𝐓𝐨 𝐏𝐥𝐚𝐲 ▶ ❤️🥀**"
            )
            return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(youtube.download(url))
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) in ACTV_CALLS:
        position = await queues.put(chat_id, file=file_path)
        await message.reply_photo(
            photo="final.png",
            caption="****😘𝙏𝙤𝙭𝙞𝙘😘 𝙎𝙤𝙣𝙜'𝙨 𝙥𝙤𝙨𝙞𝙩𝙞𝙤𝙣 💫🤟** {}**".format(position),
            reply_markup=keyboard,
        )
    else:
        await callsmusic.pytgcalls.join_group_call(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )

        await message.reply_photo(
            photo="final.png",
            reply_markup=keyboard,
            caption="**😘𝙏𝙤𝙭𝙞𝙘😘 𝙎𝙤𝙣𝙜 𝙗𝙖𝙟𝙖𝙧𝙞 𝙝𝙪 𝙚𝙣𝙟𝙤𝙮 𝙠𝙖𝙧𝙚`{}`...**".format(
        message.chat.title
        ), )

    os.remove("final.png")
    return await lel.delete()
    
