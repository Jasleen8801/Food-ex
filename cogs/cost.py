import nextcord
from nextcord.ext import commands
import requests

API_KEY = "2ed60eabcea54060998a6dbf7304e33c"


class CostCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    guild_id = 1040237301814546462

    @nextcord.slash_command(name="cost", description="To access the cost value of a particular recipe", guild_ids=[guild_id])
    async def cost(self, interaction, id: int):
        response = requests.get(
            f"https://api.spoonacular.com/recipes/{id}/priceBreakdownWidget.json?apiKey={API_KEY}").json()
        embed = nextcord.Embed(title=f"Cost for {id}", color=0x14aaeb)
        embed.add_field(name="Total Cost",
                        value=response['totalCost'], inline=True)
        embed.add_field(name="Total Cost per Serving",
                        value=response['totalCostPerServing'])
        await interaction.send(embed=embed)


def setup(bot):
    bot.add_cog(CostCog(bot))
