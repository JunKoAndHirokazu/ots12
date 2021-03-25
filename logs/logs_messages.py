import discord
from discord.ext import commands

welcomechannel = 731260102610387075
logchannel = 822891990500638740

class Logs(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_member_join(self, member):
		embed=discord.Embed(title="Logs - Rejoindre le serveur", color=0x1f9bf8)
		embed.set_author(name="GreedBot", icon_url="https://media.discordapp.net/attachments/797587918306279435/798659960837373972/discord_logo_png_395279.png")
		embed.set_thumbnail(url=member.avatar_url)
		embed.add_field(name="name", value="{} a rejoins le serveur".format(member.mention), inline=False)
		embed.set_footer(text="ID : {}".format(member.id))
		channel=self.bot.get_channel(logchannel)
		await channel.send(embed=embed)
	        
		embed=discord.Embed(title="Bienvenue !", color=0x1f9bf8)
		embed.set_author(name="GreedBot", icon_url="https://media.discordapp.net/attachments/797587918306279435/798659960837373972/discord_logo_png_395279.png")
		embed.set_thumbnail(url=member.avatar_url)
		embed.add_field(name="Bienvenue a toi sur le serveur", value="{} a rejoins le serveur".format(member.mention), inline=False)
		embed.set_footer(text="ID : {}".format(member.id))
		channel=self.bot.get_channel(welcome)
		await channel.send(embed=embed)

	@commands.Cog.listener()
	async def on_member_remove(self, member):
		embed=discord.Embed(title="Logs - Quitte le serveur", color=0x1f9bf8)
		embed.set_author(name="GreedBot", icon_url="https://media.discordapp.net/attachments/797587918306279435/798659960837373972/discord_logo_png_395279.png")
		embed.set_thumbnail(url=member.avatar_url)
		embed.add_field(name="name", value="{} nous a quitté".format(member.mention), inline=False)
		embed.set_footer(text="ID : {}".format(member.id))
		channel=self.bot.get_channel(logchannel)
		await channel.send(embed=embed)

	@commands.Cog.listener()
	async def on_message_edit(self, before, after):
		if not after.author.bot:
			if before.content != after.content:
				embed=discord.Embed(title="Logs - Message", color=0x1f9bf8)
				embed.set_author(name="GreedBot", icon_url="https://media.discordapp.net/attachments/797587918306279435/798659960837373972/discord_logo_png_395279.png")
				embed.set_thumbnail(url=after.author.avatar_url)
				embed.add_field(name="Avant", value=before.content, inline=False)
				embed.add_field(name="Après", value=after.content, inline=False)
				embed.set_footer(text="ID : {}".format(after.author.id))
				channel=self.bot.get_channel(logchannel)
				await channel.send(embed=embed)

	@commands.Cog.listener()
	async def on_message_delete(self, message):
		if not message.author.bot:
			embed=discord.Embed(title="Logs - Message", color=0x1f9bf8)
			embed.set_author(name="GreedBot", icon_url="https://media.discordapp.net/attachments/797587918306279435/798659960837373972/discord_logo_png_395279.png")
			embed.set_thumbnail(url=message.author.avatar_url)
			embed.add_field(name="Message supprimé", value=message.content, inline=True)
			embed.set_footer(text="ID : {}".format(message.author.id))
			channel=self.bot.get_channel(logchannel)
			await channel.send(embed=embed)
	
	@commands.Cog.listener()
	async def on_user_update(self, before, after):
		if before.name != after.name:
			embed=discord.Embed(title="Logs - Changement de Pseudo", color=0x1f9bf8)
			embed.set_author(name="GreedBot", icon_url="https://media.discordapp.net/attachments/797587918306279435/798659960837373972/discord_logo_png_395279.png")
			embed.set_thumbnail(url=after.avatar_url)
			embed.add_field(name="Avant", value=before.name, inline=False)
			embed.add_field(name="Après", value=after.name, inline=False)
			embed.set_footer(text="ID : {}".format(after.id))
			channel=self.bot.get_channel(logchannel)
			await channel.send(embed=embed)
		if before.discriminator != after.discriminator:
			embed=discord.Embed(title="Logs - Changement de Tag", color=0x1f9bf8)
			embed.set_author(name="GreedBot", icon_url="https://media.discordapp.net/attachments/797587918306279435/798659960837373972/discord_logo_png_395279.png")
			embed.set_thumbnail(url=after.avatar_url)
			embed.add_field(name="Avant", value=before.discriminator, inline=False)
			embed.add_field(name="Après", value=after.discriminator, inline=False)
			embed.set_footer(text="ID : {}".format(after.id))
			channel=self.bot.get_channel(logchannel)
			await channel.send(embed=embed)
		if before.avatar_url != after.avatar_url:
			embed=discord.Embed(title="Logs - Changement de Photo de profil", color=0x1f9bf8)
			embed.set_author(name="GreedBot", icon_url="https://media.discordapp.net/attachments/797587918306279435/798659960837373972/discord_logo_png_395279.png")
			embed.set_thumbnail(url=before.avatar_url)
			embed.set_image(url=after.avatar_url)
			embed.set_footer(text="ID : {}".format(after.id))
			channel=self.bot.get_channel(logchannel)
			await channel.send(embed=embed)

	@commands.Cog.listener()
	async def on_member_update(self, before, after):
		if before.display_name != after.display_name:
			embed=discord.Embed(title="Logs - Changement de Nickname", color=0x1f9bf8)
			embed.set_author(name="GreedBot", icon_url="https://media.discordapp.net/attachments/797587918306279435/798659960837373972/discord_logo_png_395279.png")
			embed.set_thumbnail(url=after.avatar_url)
			embed.add_field(name="Avant", value=before.display_name, inline=False)
			embed.add_field(name="Après", value=after.display_name, inline=False)
			embed.set_footer(text="ID : {}".format(after.id))
			channel=self.bot.get_channel(logchannel)
			await channel.send(embed=embed)
		if before.roles != after.roles:
			embed=discord.Embed(title="Logs - Changement de Rôles", color=0x1f9bf8)
			embed.set_thumbnail(url=after.avatar_url)
			embed.set_author(name="GreedBot", icon_url="https://media.discordapp.net/attachments/797587918306279435/798659960837373972/discord_logo_png_395279.png")
			embed.set_footer(text="ID : {}".format(after.id))

			fields = [("Before", ", ".join([r.mention for r in before.roles]), False),
			("After", ", ".join([r.mention for r in after.roles]), False)]
			for name, value, inline in fields:
				embed.add_field(name=name, value=value, inline=inline)
			channel=self.bot.get_channel(logchannel)
			await channel.send(embed=embed)


def setup(bot):
	bot.add_cog(Logs(bot))