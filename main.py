import discord
from discord.ext import commands

from cogs.simple import SimpleCommands

from internal.logger import Logger

class UwUBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.logger = Logger()

    async def setup_hook(self):
        """
        Initializes the bot, such as adding cogs.
        """
        await self.add_cog(SimpleCommands(self))
        self.logger.info("Simple commands loaded!")

    async def on_ready(self):
        """
        Called when the bot is ready.
        """
        self.logger.info(f"Logged in as {self.user}")
        self.logger.success("UwU bot is ready!")

    async def on_command_error(self, ctx, error):
        """
        Handles command errors gracefully.
        """
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You missed a required argument! 😿")
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send("Command not found! 🌸")
        else:
            await ctx.send("An error occurred! 🥺")
            raise error # Reraise the error for debugging if needed

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

if __name__ == "__main__":
    bot = UwUBot(command_prefix = "/", intents=intents)
    bot.run("BOT_TOKEN_GOES_HERE")
