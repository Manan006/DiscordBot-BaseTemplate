import discord
from discord import app_commands
from env import GUILD_ID as GUILD_ID


GUILD = discord.Object(id=GUILD_ID)  # create a guild object for your guild


class Bot(discord.Client):
    def __init__(self, *, intents: discord.Intents) -> None:
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        self.tree.copy_global_to(guild=GUILD)
        await self.tree.sync(guild=GUILD)  # synchronise it ONLY to the guild

    async def close(self, *args, **kwargs) -> None:
        await super().close(*args, **kwargs)


# since this is a private bot, there is no harm in enabling the intents
intents = discord.Intents.all()
bot = Bot(intents=intents)
