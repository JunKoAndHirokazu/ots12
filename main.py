import discord
from discord.ext import commands

class bcolors:
	END = '\033[0m'
	GREEN = '\033[92m'
	YELLOW = '\033[33m'
	RED = '\033[31m'
	BLUE = '\033[34m'
	CYAN = '\033[36m'



extension_list = {'Commande Fun': 'commands.fun', 'Commande Modérator': 'commands.moderator', 'Logs Serveur (Messages)': 'logs.logs_messages', 'Commande Musiques': 'music.music'}

intents = discord.Intents(messages=True, guilds=True)
intents.members = True
intents.reactions = True
intents.typing = True
intents.presences = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity= discord.Activity(name='$helping', type=discord.ActivityType.playing))
    print('Connecté en tant que:', bot.user.name)

@bot.listen()
async def on_message(message):
	if not message.author.bot:
		if (message.content == "hello" or message.content == "yo" or message.content == "salut" or message.content == "bonjour" or message.content == "bonsoir"):
			await message.add_reaction('\N{WAVING HAND SIGN}')

@bot.command()
async def serverInfo(ctx):
	server = ctx.guild
	numberOfTextChannels = len(server.text_channels)
	numberOfVoiceChannels = len(server.voice_channels)
	serverDesc = server.description
	numberOfMembers = server.member_count
	serverName = server.name
	message = f"Le serveur **{serverName}** contient actuellement {numberOfMembers} personnes. \n La description du serveur : **{serverDesc}**. \n Ce serveur possède {numberOfTextChannels} channels textuels ainsi que {numberOfVoiceChannels} channels vocal/vocaux."
	await ctx.send(message)

for extension in extension_list:
	bot.load_extension(extension_list[extension])
	print("{}[EXTENTION] {}Le fichier {} a été corréctement chargé{}".format(bcolors.GREEN, bcolors.YELLOW, extension, bcolors.END))


bot.run("token")
