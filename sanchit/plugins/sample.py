#(©) 𝚂𝙰𝙽𝙲𝙷𝙸𝚃 ♛⛧
from pyrogram import filters as  Filters

from ..utils import Utilities
from ..screenshotbot import ScreenShotBot
from ..config import Config


@ScreenShotBot.on_callback_query(Filters.create(lambda _, __, query: query.data.startswith('smpl')))
async def _(c: Client, m: CallbackQuery):
    await Utilities().sample_fn(c, m)
