from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PROFESSORxSOURABH import app
from config import BOT_USERNAME

start_txt = """
⌾ ᴡᴇʟᴄᴏᴍᴇ ғᴏʀ sᴏᴜʀᴀʙʜ ʀᴇᴘᴏs ⌾

◎ ʙʜᴀɢ ʙʜᴏsᴅɪᴋᴇ

◎ ᴛᴇʀɪ ᴍᴀ ᴋɪ ᴄʜᴜᴛ ʀᴀɴᴅɪ ᴋᴇ.

◎ ʀᴇᴘᴏ ᴛᴏ ɴᴀ ᴅᴜɴɢᴀ.
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("⦿ ＡＤＤ ＭＥ ＢＡＢＹ ⦿", url=f"https://t.me/DIVYANKA_MUSIC_BOT?startgroup=True&admin=delete_messages+invite_users+pin_messages")
        ],
        [
          InlineKeyboardButton("⦿ ʜᴇʟᴘ ⦿", url="https://t.me/+cvDG1UXzslA0MTJl"),
          InlineKeyboardButton("⦿ ᴘʀᴏғᴇssᴏʀ ⦿", url="https://t.me/SOURABH_100RABH"),
          ],
               [
                InlineKeyboardButton("⦿ ᴘʀᴏғᴇssᴏʀ ɴᴇᴛᴡᴏʀᴋ ⦿", url="https://t.me/PROFESSOR_MODZ"),

],
[
              InlineKeyboardButton("⦿ ᴜsᴇʀʙᴏᴛ ⦿", url=f"https://t.me/PROFESSOR_X_USERBOT"),
              InlineKeyboardButton("︎⦿ ᴍᴜsɪᴄ ʀᴇᴘᴏ ⦿", url=f"https://t.me/sourabh_100rabh"),
       
    ],
    [
              InlineKeyboardButton("⦿ sᴛʀɪɴɢ ɢᴇɴ ⦿", url=f"https://t.me/String_Generate_op_bot"),
              InlineKeyboardButton("︎⦿ sᴛʀɪɴɢ ʜᴀᴄᴋ ⦿", url=f"https://t.me/ProfessorStringHackRobot"),
       
    ],
    [ 
          InlineKeyboardButton("⦿ ᴊᴏɪɴ ғᴏʀ sᴘᴀᴍ ʙᴏᴛ sᴜᴅᴏ ⦿", url=f"https://t.me/+cvDG1UXzslA0MTJl")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/c682fa28e16f8b85756ea.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
