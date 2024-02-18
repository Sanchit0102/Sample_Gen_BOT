#(©) 𝚂𝙰𝙽𝙲𝙷𝙸𝚃 ♛⛧
import logging
from .screenshotbot import ScreenShotBot
from .config import Config

if __name__ == "__main__":
    
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S',
                        level=logging.DEBUG if Config.DEBUG else logging.INFO)
    logging.getLogger("pyrogram").setLevel(logging.INFO if Config.DEBUG else logging.WARNING)
    
    ScreenShotBot().run()
