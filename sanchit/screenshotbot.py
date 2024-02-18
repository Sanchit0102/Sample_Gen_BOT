#(©) 𝚂𝙰𝙽𝙲𝙷𝙸𝚃 ♛⛧
from pyrogram import Client
from pyrogram.types import Message

from .config import Config
from .database import Database

class ScreenShotBot(Client):

    def __init__(self):
        super().__init__(
            name=Config.BOT_NAME,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=20,
            plugins=dict(root="sanchit")
        )

        self.db = Database(Config.DATABASE_URL, Config.NAME)
        self.CURRENT_PROCESSES = {}
        self.CHAT_FLOOD = {}
        self.broadcast_ids = {}

    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"\n\nNew session started for {me.first_name}({me.username})")

    async def stop(self):
        await super().stop()
        print('Session stopped. Bye!!')

    async def on_message(self, message: Message):
        if message.chat.type == "private":
            await self.handle_private_message(message)
        elif message.chat.type in ["group", "supergroup", "channel"]:
            await self.handle_group_message(message)
