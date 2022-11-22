import nextcord
from nextcord.ext import commands
import requests
import re
import spoonacular as sp

API_KEY = "2ed60eabcea54060998a6dbf7304e33c"
TAG_RE = re.compile(r'<[^>]+>')
api = sp.API(API_KEY)


def removeTags(text):
    return TAG_RE.sub('', text)


class RandRecipeCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    guild_id = 1040237301814546462

    @nextcord.slash_command(name="randomrecipe", description="To fetch a random recipe", guild_ids=[guild_id])
    async def randomrecipe(self, ctx):
        response = requests.get(
            f'https://api.spoonacular.com/recipes/random?apiKey={API_KEY}').json()
        title = response['recipes'][0]['title']
        img_url = response['recipes'][0]['image']
        source_url = response['recipes'][0]['sourceUrl']
        summary = removeTags(response['recipes'][0]['summary'])
        embed = nextcord.Embed(title=title, color=0x14aaeb, url=source_url,
                               description=f"{response['recipes'][0]['id']} - {summary}")
        embed.add_field(name="Servings",
                        value=response['recipes'][0]['servings'], inline=True)
        embed.add_field(name="Ready in Minutes",
                        value=response['recipes'][0]['readyInMinutes'], inline=True)
        embed.set_image(url=img_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(RandRecipeCog(bot))
