import nextcord
from nextcord.ext import commands
import requests

API_KEY = "2ed60eabcea54060998a6dbf7304e33c"


class RandTriviaCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    guild_id = 1040237301814546462

    @nextcord.slash_command(name="randomtrivia", description="To fetch a random food trivia", guild_ids=[guild_id])
    async def randomtrivia(self, interaction):
        response = requests.get(
            f"https://api.spoonacular.com/food/trivia/random?apiKey={API_KEY}").json()
        await interaction.send(response['text'])


def setup(bot):
    bot.add_cog(RandTriviaCog(bot))
