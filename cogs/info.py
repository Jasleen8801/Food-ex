import nextcord
from nextcord.ext import commands
import requests
import re

API_KEY = "2ed60eabcea54060998a6dbf7304e33c"
TAG_RE = re.compile(r'<[^>]+>')

def removeTags(text):
    return TAG_RE.sub('', text)

class InfoCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    guild_id = 1040237301814546462

    @nextcord.slash_command(name="info", description="To access the information of a particular recipe", guild_ids=[guild_id])
    async def info(self, interaction, id: int):
        response = requests.get(
            f"https://api.spoonacular.com/recipes/{id}/information?apiKey={API_KEY}").json()
        title = response['title']
        img_url = response['image']
        source_url = response['sourceUrl']
        summary = removeTags(response['summary'])
        embed = nextcord.Embed(title=title, color=0x14aaeb, url=source_url,
                            description=f"{response['id']} - {summary}")
        embed.add_field(name="Servings", value=response['servings'], inline=True)
        embed.add_field(name="Ready in Minutes",
                        value=response['readyInMinutes'], inline=True)
        embed.set_image(url=img_url)
        await interaction.send(embed=embed)


def setup(bot):
    bot.add_cog(InfoCog(bot))
