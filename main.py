import os,json,asyncio,random,sys
import disnake
import pymongo

from cogs.commands import *
#from cogs.commands import fun

from disnake.ext.commands import Bot
from disnake.ext import tasks

if "config.json" not in os.listdir():
    sys.exit("you gotta have your configuration file set and ready first")
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
    status.start()
##DB STUFF
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["zorrow"]
    servers = mydb["servers"]
    #x = servers.delete_many({})
#Search for all the guilds that the bot is inside
    for guild in bot.guilds:
        try: 
            res = servers.find_one({"gId":guild.id})
            if res is None:
                servers.insert_one({"name":guild.name,"gId":guild.id,"ownId":guild.owner_id,
                    "region":guild.region,"created_at":guild.created_at,"member_count":guild.member_count,"icon":guild.icon.url if guild.icon else "none"})
                print(f"{guild.id} has been inserted ")
            else:
                print(f"{guild.id} already exists in the DB")
        except Exception as e:
            print("*****************Something wrong******************")
            print(e)
    ##Seeing my data
     
@bot.event
async def on_message(message: disnake.Message) -> None:

    if message.author.bot:
        return
    await bot.process_commands(message)
    '''if message == "Hello":
        print("Hello back from ZZZZORROW")
        await message.reply("Holllaaaaaa")
    if message.content == "Hello":
        await message.reply("Hollla from the cloud")
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
    '''

@tasks.loop(minutes = 1.0)
async def status():
    states = ["Playing","Fighting","Dancing"]
    #await bot.change_presence(random.choice(states))
    #choice = random.choice(states)
    await bot.change_presence(activity=disnake.Game(states[0]))
def load_commands(commands_type: str):
    for file in os.listdir('./cogs/commands'):
        if file.endswith('.py'):
            ext = file[:-3]
            try:
                bot.load_extension(f'cogs.{commands_type}.{ext}')
                print(f'loaded {ext} ')
            except Exception as e:
                print(e)
try:
    print("things work")
    load_commands("commands")
    bot.run(file["token"])
except RuntimeWarning as re:
    print("Problem with re")
except RuntimeError as re:
    print("run time error")

   
