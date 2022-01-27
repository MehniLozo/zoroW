import disnake ,youtube_dl

from disnake import Embed,VoiceClient
from disnake.ext import commands

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
class Music(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command( 
            name = "join"
            )
    async def join(self,ctx,*,channel:disnake.VoiceChannel):
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
        await channel.connect()

    @commands.command(
            name = "play"
            )
    async def play(self,ctx,*,query):
        try:
            print("****ENTERED PLAY****")
            await self.ensure_voice(ctx)
            source = disnake.PCMVolumeTransformer(disnake.FFmpegPCMAudio(query))
            ctx.voice_client.play(source,after = lambda e: print(f"Play error: {e}"))

            await ctx.send(f"Now Playing : {query}")
        except Exception as e:
            print("**********Play Error*********")
            print(e)
    @commands.command(
            name = "stop"
            )
    async def stop(self,ctx):
        try:
            #print(dir(ctx))
            await ctx.voice_client.disconnect()
        except Exception as e:
            print("***********Stop Error*********")
            print(e)

    async def  ensure_voice(self,ctx):
        print("***ENTERED ENSURE****")
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to voice channel")
                raise commands.CommandError("Author not connected to voice")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()
def setup(bot):
    bot.add_cog(Music(bot))
