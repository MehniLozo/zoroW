import disnake,asyncio,json,os
import requests
import random
from disnake import Embed
from disnake.ext import commands
from disnake.ext.commands import Context
from pathlib import Path

class Fun(commands.Cog,name = "fun-command"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command( 
            name = "gif")
    async def gif(self,context:Context):
        content = context.message.content.split("!gif")[1]
        try:
            conf_dir = os.getcwd().split("cogs")[0] 
            conf_p = conf_dir + "/config.json"
            with open(conf_p) as cp:
                conf_file = json.load(cp)
            search_url = "https://g.tenor.com/v1/search?q=" + content  + "&key=" + conf_file["TENORKEY"] + "&limit=8"
            res = requests.get(search_url)
            clear_res = random.choice(res.json()['results'])['url']

            await context.send(clear_res)
        except Exception as e:
            print("*****************")
            print(e)
            print("*****************")
            await context.send("Sorry somthing in the cloud went wrong")

def setup(bot):
    bot.add_cog(Fun(bot))
