

import random
from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import OWNER_USERNAME
from nexichat import nexichat
from nexichat.database.chats import add_served_chat
from nexichat.database.users import add_served_user
from nexichat.modules.helpers import PNG_BTN


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



@nexichat.on_cmd("ping")
async def ping(_, message: Message):
    await message.reply_sticker(sticker=random.choice(STICKER))
    start = datetime.now()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="ᴘɪɴɢɪɴɢ...",
    )
    try:
        await message.delete()
    except:
        pass

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=f"нey вαву!!\n{nexichat.name} ιѕ alιve 🥀 αnd worĸιng ғιne wιтн a pιng oғ\n➥ `{ms}` ms\n\n<b>|| мαdє ωιтн ❣️ ву [MAHSOOM❣️](https://t.me/{OWNER_USERNAME}) ||</b>",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)
