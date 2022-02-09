import disnake
from disnake.ext import commands
from pymongo import MongoClient

bundle= MongoClient("mongodb://localhost:27017/")
levels = bundle["levels"]["zorrow"]


class level(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self,ctx):
        #we're gonna check stats from DB everytime a guy writes a message
        stats = levels.find_one({"guildid":ctx.guild.id,"id":ctx.author.id})
        serverstats


