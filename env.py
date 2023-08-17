from dotenv import load_dotenv
import os
import configparser

load_dotenv()

TOKEN = os.getenv("TOKEN")  # the discord bot token

config = configparser.ConfigParser()
config.read("config.ini")

# the id of your guild
GUILD_ID = config.get("bot", "GUILD_ID")
# 0 means log level is WARNING and 1 means log level is DEBUG
DEBUG_LOG = config.getboolean("logging", "DEBUG_LOG")
# the prefix of the bot (not the slash commands)
PREFIX = config.get("bot", "PREFIX")
