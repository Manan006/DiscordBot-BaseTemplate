from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN") # the discord bot token
GUILD_ID = os.getenv("GUILD_ID") # the id of your guild
DEBUG_LOG = os.getenv("DEBUG_LOG") # 0 means log level is WARNING and 1 means log level is DEBUG