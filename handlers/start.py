import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAIajGLzo9lRiTKwZzwGySzHowRoIJzVAALyAgACVZ_QVA-wlVAQBb5LHgQ")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
ʜᴇʏ {message.from_user.mention()} !

        ᴛʜɪs ɪs [{bn}](t.me/{bu})🖤, 
                                    
๏ ᴀ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ᴠɪᴅᴇᴏᴄʜᴀᴛs...

๏ ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴀʙᴏᴜᴛ ᴍᴇ ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ](t.me/{me}) ʙᴀʙʏ...
━━━━━━━━━━━━━━━━━━**""",



reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        " ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ɢᴜʏs ", url=f"https://t.me/{bu}?startgroup=true"

                       ),

                  ],[

                    InlineKeyboardButton(

                        " ᴍᴀɪɴᴛᴇʀ ", url=f"https://t.me/{me}"

                    ),

                    InlineKeyboardButton(

                        " sᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/{SUPPORT_GROUP}"

                    )

                ],[

                    InlineKeyboardButton(

                        " ɪɴʟɪɴᴇ ", switch_inline_query_current_chat=""

                    ),

                    InlineKeyboardButton(

                        " sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ", url="https://t.me/musicxsupportmm"

                    )]

            ]

       ),

    )





    
