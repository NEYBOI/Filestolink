

from pyrogram import filters, emoji
from Adarsh.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command(['start']))
async def start(_, m: Message):
    await m.reply(f'Hi {m.from_user.mention(style="md")}, Send me a file to get Download stream link. \n\nIf You Want Help Press /help',
                
                  )
    return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://graph.org/file/ce0b11356141116fd8117.jpg",
                caption="<i>𝙹𝙾𝙸𝙽 CHANNEL 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴🔐</i>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jᴏɪɴ ɴᴏᴡ 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )

@StreamBot.on_message(filters.command(['help']))
async def help(_, m: Message):
    await m.reply(f'i can convert any file into Download Link or Online Streaming Link! \n2GB+ files Supported ✅ \n18+ Content Not Allowed ⚠️ \nLinks are Permanent 🍀 \n\nFor More Help Press /players',
    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Any Queries DM Here ✅', url='https://t.me/Link_Reporter_Bot')]])
                  
                  )
    
@StreamBot.on_message(filters.command(['about']))
async def about(_, m: Message):
    await m.reply(f'✯ ᴍʏ ɴᴀᴍᴇ: Flash \n✯ ᴍʏ ᴄʀᴇᴀᴛᴏʀ: Shubham \n✯ ᴘᴏᴡᴇʀᴇᴅ ʙʏ: [Moviesss4ers](https://t.me/Moviesss4ers) \n✯ ʟɪʙʀᴀʀʏ: Pyrogram \n✯ ʟᴀɴɢᴜᴀɢᴇ: Python \n✯ ᴅᴀᴛᴀʙᴀꜱᴇ: Free \n✯ ʙᴏᴛ ꜱᴇʀᴠᴇʀ: Koyeb',
    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('My Owner 😎', url='https://t.me/Nexus_Shubhu')]])
                  
                  )

@StreamBot.on_message(filters.command(['players']))
async def players(_, m: Message):
    await m.reply(f'Dear Users, \n\nTo Streaming Your File in Players Open Links Through 1st Botton (ꜱᴛʀᴇᴀᴍ ɪɴ ᴘʟᴀʏᴇʀꜱ ⚡️) \nOpen in Chrome. \n\nMake Sure You have Good Internet Speed For Streaming On Players')
