import discord
from discord.ext import commands
from discord.utils import get

def createMutedRole(ctx):
	mutedRole = ctx.guild.create_role(name = "Muted", permissions = discord.Permissions( send_messages = False, speak = False))
	    

	for channel in ctx.guild.channels:
	   channel.set_permissions(mutedRole, send_messages = False, speak = False)
	return mutedRole
	    
def getMutedRole(ctx):
	roles = ctx.guild.roles
	for role in roles:
	    if role.name == "Muted":
	        return role
	return createMutedRole(ctx)

class Modération(commands.Cog):
	def __init__ (self, bot):
		self.bot = bot
	
	@commands.command(pass_context=True)
	async def mute(self, ctx, member : discord.Member, *, reason = "Aucune raison donnée"):
	    mutedRole = getMutedRole(ctx)
	    await member.add_roles(mutedRole, reason = reason)
	    await ctx.send(f"{member.mention} a bien été mute.")

	@commands.command(pass_context=True)
	async def unmute(self, ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
	    mutedRole = getMutedRole(ctx)
	    await member.remove_roles(mutedRole, reason = reason)
	    await ctx.send(f"{member.mention} a été unmute !")

	@commands.command(pass_context=True)
	@commands.has_permissions(ban_members = True)
	async def userBanned(self, ctx):
	    ids = []
	    bans = await ctx.guild.bans()
	    for i in bans:
	        ids.append(str(i.user.id))
	    await ctx.send("La liste des identifiants des utilisateurs bannis de ce serveur est :")
	    await ctx.send("\n".join(ids))

	@commands.command(pass_context=True)
	@commands.has_permissions(manage_messages = True)
	async def clear(self, ctx, nombre : int):
	    messages = await ctx.channel.history(limit = nombre + 1).flatten()
	    for message in messages:
	        await message.delete()

	@commands.command(pass_context=True)
	@commands.has_permissions(kick_members = True)
	async def kick(self, ctx, user : discord.User, *reason):
	    reason = " ".join(reason)
	    await ctx.guild.kick(user, reason = reason)
	    await ctx.send(f"{user} à été kick.")

	@commands.command(pass_context=True)
	@commands.has_permissions(ban_members = True)
	async def unban(self, ctx, id:int, *reason):
		reason = " ".join(reason)
		banlist = await ctx.guild.bans()
		for ban in banlist:
			print(ban.user.id)
			print(id)
			if ban.user.id == id:
				print(ban.user.id)
				await ctx.guild.unban(ban.user, reason = reason)
				await ctx.send(f"{ban.user} à été unban.")
				return
		await ctx.send(f"L'utilisateur {id} n'est pas dans la liste des bans")

	@commands.command(pass_context=True)
	@commands.has_permissions(ban_members = True)
	async def ban(self, ctx, user : discord.User, *reason):
		reason = " ".join(reason)
		await ctx.guild.ban(user, reason = reason)
		await ctx.send(f"{user} à été ban pour la raison suivante : {reason}.")

def setup(bot):
	bot.add_cog(Modération(bot))