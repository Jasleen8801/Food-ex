import nextcord
from nextcord.ext import commands
import requests

API_KEY = "2ed60eabcea54060998a6dbf7304e33c"


class NutritionCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    guild_id = 1040237301814546462

    @nextcord.slash_command(name="nutrition", description="To access the nutritional value of a particular recipe", guild_ids=[guild_id])
    async def nutrition(self, interaction, id: int):
        response = requests.get(
            f"https://api.spoonacular.com/recipes/{id}/nutritionWidget.json?apiKey={API_KEY}").json()
        embed = nextcord.Embed(
            title=f"Nutritional Value for {id}", color=0x14aaeb)
        embed.add_field(name="Calories",
                        value=response['calories'], inline=True)
        embed.add_field(name="Carbs", value=response['carbs'], inline=True)
        embed.add_field(name="Fat", value=response['fat'], inline=True)
        embed.add_field(name="Protein", value=response['protein'], inline=True)
        embed.add_field(name="Expires", value=response['expires'], inline=True)
        # embed.add_field(name="isStale", value=response['isStale'], inline=True)
        await interaction.send(embed=embed)


def setup(bot):
    bot.add_cog(NutritionCog(bot))
