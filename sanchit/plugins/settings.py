#(©) 𝚂𝙰𝙽𝙲𝙷𝙸𝚃 ♛⛧
from pyrogram import filters as  Filters

from ..screenshotbot import ScreenShotBot
from ..utils import Utilities

@Client.on_message(Filters.private & Filters.command("settings"))
async def start(client: Client, message: Message):

    await Utilities.display_settings(client, message)
