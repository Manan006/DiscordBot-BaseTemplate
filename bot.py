import discord
from discord.ext import commands
from env import GUILD_ID, PREFIX
from logs import log_config

GUILD = discord.Object(id=GUILD_ID)  # create a guild object for your guild


class Bot(commands.Bot):
    def __init__(self, intents: discord.Intents, *, command_prefix: str, log_config) -> None:
        self.log_config = log_config
        super().__init__(intents=intents,
                         command_prefix=command_prefix)

    async def close(self, *args, **kwargs) -> None:
        await super().close(*args, **kwargs)
        print("Bot was gracefully shutdown")

    async def setup_hook(self) -> None:
        self.tree.copy_global_to(guild=GUILD)
        await self.tree.sync(guild=GUILD)  # synchronise it ONLY to the guild

    def run(self, token: str,  *args, **kwargs):
        super().run(*args, **kwargs, token=token,
                    log_handler=self.log_config["handler"],
                    log_formatter=self.log_config["formatter"],
                    log_level=self.log_config["level"])


# since this is a private bot, there is no harm in enabling the intents
intents = discord.Intents.all()

bot = Bot(intents=intents, command_prefix=PREFIX, log_config=log_config)
