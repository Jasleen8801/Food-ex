import nextcord
from nextcord.ext import commands
from nextcord import ButtonStyle, Embed
from nextcord.ui import Button, View
import json

helpGuide = json.load(open("help.json"))


class HelpCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    def createHelpEmbed(self, pageNum=0, inline=False):
        pageNum = (pageNum) % len(list(helpGuide))
        pageTitle = list(helpGuide)[pageNum]
        embed = Embed(color=0x0080ff, title=pageTitle)
        for key, val in helpGuide[pageTitle].items():
            embed.add_field(name=self.bot.command_prefix+key, value=val, inline=inline)
            embed.set_footer(text=f"Page {pageNum+1} of {len(list(helpGuide))}")
        return embed

    @nextcord.slash_command(name="help", guild_ids=[1040237301814546462])
    async def Help(self, interaction):
        currentPage = 0

        async def next_callback(interaction):
            nonlocal currentPage, sent_msg
            currentPage += 1
            await sent_msg.edit(embed=self.createHelpEmbed(pageNum=currentPage), view=myview)

        async def previous_callback(interaction):
            nonlocal currentPage, sent_msg
            currentPage -= 1
            await sent_msg.edit(embed=self.createHelpEmbed(pageNum=currentPage), view=myview)

        previousButton = Button(label="<", style=ButtonStyle.blurple)
        nextButton = Button(label=">", style=ButtonStyle.blurple)
        previousButton.callback = previous_callback
        nextButton.callback = next_callback

        myview = View(timeout=180)
        myview.add_item(previousButton)
        myview.add_item(nextButton)

        sent_msg = await interaction.send(embed=self.createHelpEmbed(currentPage), view=myview)


def setup(bot):
    bot.add_cog(HelpCog(bot))
