#(©) 𝚂𝙰𝙽𝙲𝙷𝙸𝚃 ♛⛧
from pyrogram import filters as  Filters
from pyrogram.types import ForceReply

from ..utils import Utilities
from ..screenshotbot import ScreenShotBot
from ..config import Config


@ScreenShotBot.on_message(Filters.private & (Filters.reply | Filters.command('trim')))
async def _(c, m):

    if not isinstance(m, Message):
        return

    if (
        not m.reply_to_message
        or not m.reply_to_message.reply_markup
        or not isinstance(m.reply_to_message.reply_markup, ForceReply)
    ):
        return

    if m.reply_to_message.text.startswith('#trim_video'):
        await Utilities().trim_fn(c, m)
    else:
        await Utilities().manual_screenshot_fn(c, m)
