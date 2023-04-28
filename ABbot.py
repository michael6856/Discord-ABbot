import discord
from discord.ext import commands
import youtube_dl

intents = discord.Intents.all()
bot = commands.Bot(intents=intents)
discord_token = "MTA2NTk4NzMxMDQ0Njk3Mjk2OA.GXe59H.RUN0VaWTKAmRvinyX6A6oT-m71EqOHd_czpOBo"

@bot.event
async def on_ready():
    print(bot.user.name + " is ready")


@bot.slash_command(name="test", description="test")
async def test(ctx):
    await ctx.respond("test")


@bot.slash_command(name="ping", description="ABbot's ping")
async def ping(ctx):
    await ctx.respond("延遲：" + str(round(bot.latency * 1000)) + "ms")

#Music Bot
@bot.slash_command(name="join", description="加入語音頻道")
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.respond("加入成功" + ":white_check_mark:")

@bot.slash_command(name="leave", description="離開語音頻道")
async def leave(ctx):
    await ctx.voice_client.disconnect()
    await ctx.respond("已離開" + ":white_check_mark:")


bot.run("MTA2NTk4NzMxMDQ0Njk3Mjk2OA.GXe59H.RUN0VaWTKAmRvinyX6A6oT-m71EqOHd_czpOBo")


