

import asyncio
import random

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message


from nexichat import nexichat
from nexichat.database.chats import add_served_chat
from nexichat.database.users import add_served_user
from nexichat.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    SOURCE_READ,
    START,
)


#----------------IMG-------------#



# Random Start Images
IMG = [
    "https://graph.org/file/43a5426c1d658e4c20974.jpg",
    "https://graph.org/file/cdead2380a39f7f06361a.jpg",
    "https://graph.org/file/6ac152164dadffe7520dc.jpg",
    "https://graph.org/file/13348ef13c7fdad4a508d.jpg",
    "https://graph.org/file/4be7e2c8a576471bffc63.jpg",
    "https://graph.org/file/c59d9903eb1be3e754197.jpg",
    "https://graph.org/file/f8698e1128feca60789c1.jpg",
    "https://graph.org/file/5b8220a5596d30aa66819.jpg",
    "https://graph.org/file/da2c80fe08b1247377939.jpg",
    "https://graph.org/file/b058022ec750ec3f12171.jpg",
    "https://graph.org/file/38ab828a1603f12e08dfb.jpg",
    "https://graph.org/file/4c0d723e9cf18437696cc.jpg",
    "https://graph.org/file/183acc250f718121b9367.jpg",
    "https://graph.org/file/0d4ad1c1c45e11a8381f5.jpg",
]


#----------------IMG-------------#


#---------------STICKERS---------------#

# Random Stickers
STICKER = [
    "CAACAgQAAxkBAAIB2GWwPEcf3R04dxaTQJzsfpuPeYNHAAIWAgAC4g3cJfv_Ze4DaXc2HgQ",
    "CAACAgQAAxkBAAIB3GWwPF6OkUxEtqm0E0i_GAZk_1lOAAJrAgAC4g3cJStJo1WeIBCYHgQ",
    "CAACAgQAAxkBAAIB3WWwPGBv89W7AVoFZFv53x-OYDMYAAJsAgAC4g3cJatDhZjYJhMmHgQ",
]

#---------------STICKERS---------------#


#---------------EMOJIOS---------------#

EMOJIOS = [
    "💣",
    "💥",
    "🪄",
    "🧨",
    "⚡",
    "🤡",
    "👻",
    "🎃",
    "🎩",
    "🕊",
]


#---------------EMOJIOS---------------#

@nexichat.on_cmd(["start", "aistart"])
async def start(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        accha = await m.reply_text(
            text=random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ︎ ѕтαятιиg..__")
        await asyncio.sleep(0.2)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ sтαятιиg.....__")
        await asyncio.sleep(0.2)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ︎ sтαятιиg..__")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await umm.delete()
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=f"""**๏ ʜᴇʏ, ɪ ᴀᴍ {nexichat.name}**\n**➻ ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ.**\n**──────────────**\n**➻ ᴜsᴀɢᴇ /chatbot [ᴏɴ/ᴏғғ]**\n<b>||๏ ʜɪᴛ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ʜᴇʟᴘ||</b>""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=START,
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await add_served_chat(m.chat.id)


@nexichat.on_cmd("help")
async def help(client: nexichat, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        hmm = await m.reply_photo(
            photo=random.choice(IMG),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption="**ʜᴇʏ, ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs!**",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_chat(m.chat.id)


@nexichat.on_cmd("repo")
async def repo(_, m: Message):
    await m.reply_text(
        text=SOURCE_READ,
        reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
        disable_web_page_preview=True,
    )


@nexichat.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
    for member in m.new_chat_members:
        await m.reply_photo(photo=random.choice(IMG), caption=START)
