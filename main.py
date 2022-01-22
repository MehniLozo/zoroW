import os,json,asyncio,random
import disnake

from disnake.ext.commands import Bot
from disnake.ext import tasks

if "config.json" not in os.listdir():
    print("you gotta have your configuration file set and ready first")
else:
    with open('config.json') as jfile:
        file = json.load(jfile)
 
bot = Bot(command_prefix=file["prefix"])
@bot.event
async def on_ready():
    print(f"{bot.user.name} is up and running")
    print(f"disnake version {disnake.__version__}")
    print(f"owner : {bot.owner} : {bot.owner_id}")
    print("Honorably member of ")
    print("\n".join([str(x) for x in bot.guilds]))
@bot.event
async def on_message(message: disnake.Message) -> None:

    if message.author.bot:
        print("Should i answer?")
        return
    '''if message == "Hello":
        print("Hello back from ZZZZORROW")
        await message.reply("Holllaaaaaa")
    '''
    if message.content == "Hello":
        message.reply("Hollla from the cloud")
    if message.content == "react me":
        try:
            emojList = ["👋","🤚","🖐","✋"]
            choice = random.choice(emojList)
            await message.add_reaction(choice)
            print(f"react to {message.author} with{choice} ")
        except disnake.InvalidArgument as ia:
            print("Invalid emoji")
        except disnake.HTTPException as he:
            print(he)

@tasks.loop(minutes = 1.0)
async def status():
    states = ["Playing","Fighting","Dancing"]
    await bot.change_presence(random.choice(states))


try:
    print("things work")
    
    bot.run(file["token"])
except RuntimeWarning as re:
    print("Problem with re")
except RuntimeError as re:
    print("run time error")


