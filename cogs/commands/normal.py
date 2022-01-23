import disnake,asyncio

from disnake import Embed
from disnake.ext import commands
from disnake.ext.commands import Context

from .trans import translate

class Normal(commands.Cog,name = "Normal-command"):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(
            name='info'
            )
    async def info(self,context:Context):
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
                text = f"invoked by {context.author}"
                )
        await context.send(embed=embed)
    @commands.command(
                name='sinfo'
                )
    async def sinfo(self,context:Context):
        try:
 
            embed = Embed(
                    title = "Server info",
                    description = "interesting infos about the server",
                    color= 0x9C84EF
                    )
            embed.set_thumbnail(
                url= context.guild.icon.url
            )
            embed.add_field( 
                    name = "Name",
                    value = context.guild.name)
            embed.add_field( 
                    name = "Member Count",
                    value = context.guild.member_count)
            embed.add_field( 
                    name = "CreatedAt",
                    value = context.guild.created_at)
            embed.add_field( 
                    name = "Region",
                    value = context.guild.region)
            await context.send(embed=embed)
        except AttributeError as nt:
            print(f"Couldn't find icon for {context.guild.name}")

        finally:
            
            embed = Embed(
                    title = "Server info",
                    description = "interesting infos about the server",
                    color= 0x9C84EF
                )

            embed.add_field( 
                    name = "Name",
                    value = context.guild.name)
            embed.add_field( 
                    name = "Member Count",
                    value = context.guild.member_count)
            embed.add_field( 
                    name = "CreatedAt",
                    value = context.guild.created_at)
            embed.add_field( 
                    name = "Region",
                    value = context.guild.region)
            await context.send(embed=embed)
    @commands.command( 
            name = "tr",
            description = "translate my word pal"
            )
    async def tr(self,context:Context):
        try:
            word= context.message.content.split('!tr')[1] 
            wtype,syn = translate(word)

            embed = Embed(
                    title = "word-time",
                    color = 0x9C84EF
                    )
            embed.add_field( 
                    name = "word",
                    value = word
                    )
            embed.add_field( 
                    name = "meaning",
                    value = syn[0]
                    )
            embed.set_footer ( 
                    text = f"invoked by {context.author}"
                    )
            await context.send(embed= embed)
        except Exception as e:
            print("Something wrong with translation")
            print(e)


def setup(bot):
    bot.add_cog(Normal(bot))
