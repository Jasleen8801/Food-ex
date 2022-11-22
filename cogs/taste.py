import nextcord
from nextcord.ext import commands
import requests

API_KEY = "2ed60eabcea54060998a6dbf7304e33c"


class TasteCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    guild_id = 1040237301814546462

    @nextcord.slash_command(name="taste", description="To access the taste of a particular recipe", guild_ids=[guild_id])
    async def taste(self, interaction, id: int):
        response = requests.get(
            f"https://api.spoonacular.com/recipes/{id}/tasteWidget.json?apiKey={API_KEY}").json()
        embed = nextcord.Embed(title=f"Taste for {id}", color=0x14aaeb)
        embed.add_field(name="Sweetness", value=response['sweetness'])
        embed.add_field(name="Saltiness", value=response['saltiness'])
        embed.add_field(name="Sourness", value=response['sourness'])
        embed.add_field(name="Bitterness", value=response['bitterness'])
        embed.add_field(name="Savoriness", value=response['savoriness'])
        embed.add_field(name="Fattiness", value=response['fattiness'])
        embed.add_field(name="Spiciness", value=response['spiciness'])
        embed.set_footer(text="Use the command '$help' if you're stuck!!")
        await interaction.send(embed=embed)


def setup(bot):
    bot.add_cog(TasteCog(bot))
