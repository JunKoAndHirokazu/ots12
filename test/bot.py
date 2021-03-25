import discord
from discord.ext import commands
import youtube_dl
import os

# import logging

# logging.basicConfig(level=logging.INFO)

# logger = logging.getLogger('discord')
# logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handler)

# intents = discord.Intents(messages=True, guilds=True)
bot = commands.Bot(command_prefix='$',
                   description="This is a Helper Bot")  #, intents=intents)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.listen()
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def hug(ctx, member: discord.Member = None):
    if not member:
        embed = discord.Embed(title="Huggies!",
                              description="**{1}** hugs **{0}**!".format(
                                  bot.user, ctx.message.author.mention),
                              color=0x176cd5)
        embed.set_image(
            url=
            "https://i.pinimg.com/originals/85/72/a1/8572a1d1ebaa45fae290e6760b59caac.gif"
        )
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Huggies!",
                              description="**{1}** hugs **{0}**!".format(
                                  member.mention, ctx.message.author.mention),
                              color=0x176cd5)
        embed.set_image(
            url=
            "https://i.pinimg.com/originals/85/72/a1/8572a1d1ebaa45fae290e6760b59caac.gif"
        )
        await ctx.send(embed=embed)


@bot.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Général')
    await voiceChannel.connect()
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

# @bot.command()
# async def hug(ctx):
#     embed=discord.Embed(title="Huggies!", description="**{1}** hugs **{0}**!".format(mention.bot, ctx.message.author.name), color=0x176cd5)
#     embed.set_image(url="https://i.pinimg.com/originals/85/72/a1/8572a1d1ebaa45fae290e6760b59caac.gif")
#     await bot.say(embed=embed)

#bot.run('NDY5MDg4ODc5MjA3NTE0MTMy.W08XEA.qpjNcEZB9vKMIC2f4oNwr8mXCy0')
bot.run('NjgwNDg5MTg0NjE1NzI3MjE3.XwjDPw.A9Td-rpYBOrX79mzgE9HXuSVzUE')