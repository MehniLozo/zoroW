import os
import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction

class Normal(commands.Cog,name = "Normal-slash"):
    def __init__(self,bot):
        self.bot = bot
    @commands.slash_command( 
            name='this'
            )
    async def this(self,interaction = ApplicationCommandInteraction):
        embed = Embed(
                title = "zoroW info",
                description = "zoroW your savior from ..",
                color= 0x9C84EF
                )
        embed.set_author( 
                name = 'Lozo is my zorrow'
                )
        embed.add_field(
                name = "Name",
                value = "zoroW"
                )
        embed.add_field( 
                name = "prefix",
                value = "!",
                inline = True
                )
        embed.add_field( 
                name = "support server",
                value = "https://discord.gg/rqeNChPc"
                )
        embed.add_field( 
                name = "Help",
                value = "!help"
                )
        embed.set_footer( 
                text = f"invoked by {interaction.author}"
                )
        await interaction.send(embed=embed)
 
def setup(bot):
    bot.add_cog(Normal(bot))
