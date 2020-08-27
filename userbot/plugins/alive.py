"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "CrackBot"
PM_IMG = "https://telegra.ph/file/3feaa0629756e0e45a2b7.jpg"
pm_caption = "**ᴄʀᴀᴄᴋʙᴏᴛ ᴏғғɪᴄɪᴀʟ**\n\n"
pm_caption += "**🙃 Yus, Am Alive And Working Fine Bish Don't Be Rude Go And Fuq Off...**\n\n"
pm_caption += "✘ About My System ✘\n\n"
pm_caption += "➾Telethon Version : **6.0.9**\n➾Python : 3.7.4\n"
pm_caption += "➾DataBase : **Functioning**\n"
pm_caption += "➾Bot Creator : [Crackexy](https://t.me/Crackexy).\n"
pm_caption += "➾Crackbot Version : 1.00\n\n"
pm_caption += f"**➾My Master** : {DEFAULTUSER}\n"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
    
