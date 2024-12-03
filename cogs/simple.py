import discord, re
from discord.ext import commands

class SimpleCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @staticmethod
    def to_uwu(text: str) -> str:
        """
        Converts text to 'UwU' speak.
        """
        replacements = {
            r"[rl]": "w",
            r"[RL]": "W",
            r"\bno\b": "nyo",
            r"\bmo\b": "mowo",
            r"\bna\b": "nya",
            r"\bne\b": "nye",
            r"ove": "uv",
            r"\bvery\b": "vewy",
            r"\bhappy\b": "happi",
        }
        for pattern, repl in replacements.items():
            text = re.sub(pattern, repl, text)
        return text + " UwU"

    @commands.command()
    async def uwuify(self, ctx, *, text: str):
        """
        Converts the input text to 'UwU' speak and sends it back.
        """
        uwu_text = self.to_uwu(text)
        await ctx.send(uwu_text)

    @commands.command()
    async def hug(self, ctx, *, member: discord.Member = None):
        """
        Sends a virtual hug to a specified member or everyone.
        """
        await ctx.send(f"{ctx.author.mention} gives evewyone a big hug! 💞✨" if not member \
            else f"{ctx.author.mention} sends {member.mention} huggie wuggies 💖" if member != ctx.author \
            else f"{ctx.author.mention} gives themselves a big hug! 💞✨")
