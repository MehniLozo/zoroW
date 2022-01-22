import disnake,asyncio

from disnake import Embed
from disnake.ext import commands
from disnake.ext.commands import Context
class Normal(commands.Cog,name = "Normal-command"):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(
            name='info'
            )
    async def info(self,context:Context):
        embed = Embed(
                title = "Info Embed",
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
                text = f"invoked by {context.author}"
                )
        await context.send(embed=embed)
def setup(bot):
    bot.add_cog(Normal(bot))
