import discord
from discord.ext import commands
import youtube_dl
import os

youtube_dl.utils.bug_reports_message = lambda: ''

class Music(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def play(self, ctx, url : str):
		song_there = os.path.isfile("song.mp3")
		try:
			if song_there:
				os.remove("song.mp3")
		except PermissionError:
			await ctx.send("Wait for the current playing music to end or use the 'stop' command")
			return

		voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Général')
		await voiceChannel.connect()
		voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

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

def setup(bot):
	bot.add_cog(Music(bot))