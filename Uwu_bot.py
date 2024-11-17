import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)

#the dictionary
def to_uwu(text):
    replacements = {
        "r": "w",
        "l": "w",
        "R": "W",
        "L": "W",
        "no": "nyo",
        "mo": "mowo",
        "na": "nya",
        "ne": "nye",
        "ove": "uv",
        "very": "vewy",
        "happy": "happi",     
    }
    for key, val in replacements.items():
        text = text.replace(key, val)
    text += " UwU "
    return text

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("UwU bot is ready!")

@bot.command()
async def uwuify(ctx, *, text: str):
    uwu_text = to_uwu(text)
    await ctx.send(uwu_text)

 #Hug command :3
@bot.command()
async def hug(ctx, *, member: discord.Member = None):
    """Send a virtual hug to someone."""
    if member:
        await ctx.send(f" {ctx.author.mention} sends {member.mention} huggie wuggies 💖")
    else:
        await ctx.send(f"{ctx.author.mention} gives evewyone a big hug! 💞✨")

#zi Token 
bot.run("PUT YOUR TOKEN HERE")

