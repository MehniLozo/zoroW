import disnake,asyncio,json,os
import requests
import random
from disnake import Embed,VoiceClient
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
    @commands.command(
            name = "guess"
            )
    async def guess(self,context:Context):
        await context.send("Guess a number between 1 and 10")

        def is_correct(m):
            return m.author == context.author and m.content.isdigit()
        
        answer = random.randint(1,10)
        
        try:
            guess = await self.bot.wait_for("message",check=is_correct,timeout=5.0)
            if int(guess.content) == answer:
                await context.send("Bravo you got it mrrrr masster")
            else:
                await context.send(f"It was actually {answer}")
        except  asyncio.TimeoutError:
            await context.send(f"It was {answer}.")
        except Exception as e:
            print("*******General Error in guessing*******")
            print(e)




 
def setup(bot):
    bot.add_cog(Fun(bot))
