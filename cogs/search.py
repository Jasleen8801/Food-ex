import nextcord
from nextcord.ext import commands
import requests

API_KEY = "2ed60eabcea54060998a6dbf7304e33c"


class SearchCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    guild_id = 1040237301814546462

    @nextcord.slash_command(name="search", description="To search a particular recipe and get its ID", guild_ids=[guild_id])
    async def search(self, interaction, query: str):
        response = requests.get(
            f"https://api.spoonacular.com/recipes/complexSearch?apiKey={API_KEY}&query={query}").json()
        id = []
        title = []
        image_url = []
        for val in response['results']:
            id.append(val['id'])
            title.append(val['title'])
            image_url.append(val['image'])
        embed = nextcord.Embed(
            title=f"Results for {query} are",
            color=0x14aaeb
        )
        for i in range(len(id)):
            embed.add_field(name=title[i], value=id[i], inline=False)
        embed.set_footer(text="Use the command '$help' if you're stuck!!")
        await interaction.send(embed=embed)


def setup(bot):
    bot.add_cog(SearchCog(bot))
