import nextcord
from nextcord.ext import commands
import spoonacular as sp

API_KEY = "2ed60eabcea54060998a6dbf7304e33c"
api = sp.API(API_KEY)



class RandJokeCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    guild_id = 1040237301814546462

    @nextcord.slash_command(name="randomjoke", description="To fetch a random joke", guild_ids=[guild_id])
    async def randomjoke(self, interaction):
        response = api.get_a_random_food_joke()
        data = response.json()
        description = data['text']
        embed = nextcord.Embed(title="Here's a Food Joke",
                               color=0x14aaeb, description=description)
        await interaction.send(embed=embed)


def setup(bot):
    bot.add_cog(RandJokeCog(bot))
