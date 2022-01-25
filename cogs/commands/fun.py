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
            ############Audio stuff###########
    @commands.command(
            name="play"
            )
    async def play(self,context:Context):
        youtube_dl.utils.bug_reports_message = lambda: ""

        ytdl_format_options = {
            "format": "bestaudio/best",
            "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
            "restrictfilenames": True,
            "noplaylist": True,
            "nocheckcertificate": True,
            "ignoreerrors": False,
            "logtostderr": False,
            "quiet": True,
            "no_warnings": True,
            "default_search": "auto",
            "source_address": "0.0.0.0",  # bind to ipv4 since ipv6 addresses cause issues sometimes
        }
        ffmpeg_options = {"options":"-vn"}
        ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


        class YTDLSource(disnake.PCMVolumeTransformer):
            def __init__(self, source, *, data, volume=0.5):
                super().__init__(source, volume)

                self.data = data

                self.title = data.get("title")
                self.url = data.get("url")

            @classmethod
            async def from_url(cls, url, *, loop=None, stream=False):
                loop = loop or asyncio.get_event_loop()
                data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
                assert data

                if "entries" in data:
                    # take first item from a playlist
                    data = data["entries"][0]

                filename = data["url"] if stream else ytdl.prepare_filename(data)
                assert filename

                return cls(disnake.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)



        
def setup(bot):
    bot.add_cog(Fun(bot))
