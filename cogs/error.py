import nextcord
from nextcord.ext import commands


class ErrorCog(commands.Cog, name="Error"):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, interaction, error):
        try:
            if hasattr(interaction.command, 'on_error'):
                return
            else:
                embed = nextcord.Embed(title=f"Error in {interaction.command}", description=f'`{interaction.command.qualified_name}` `{interaction.command.signature}` \n{error}')
                await interaction.send(embed=embed)
        except:
            embed = nextcord.Embed(title=f"Error in {interaction.command}", description=f'{error}')
            await interaction.send(embed=embed)


def setup(bot):
    bot.add_cog(ErrorCog(bot))
