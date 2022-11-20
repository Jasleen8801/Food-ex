import nextcord
import os
from dotenv import load_dotenv
from nextcord.ext import commands
import asyncio
from pathlib import Path

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    print("online")
    return await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing, name='Multi Utility Foodie'))


def extensions():
    files = Path("cogs").rglob("*.py")
    for file in files:
        yield file.as_posix()[:-3].replace("/", ".")


for ext_file in extensions():
    try:
        bot.load_extension(ext_file)
        print(f"Loaded {ext_file}")
    except Exception as ex:
        print(f"Failed to load {ext_file}: {ex}")


async def main():
    await bot.start(DISCORD_TOKEN)

asyncio.run(main())

