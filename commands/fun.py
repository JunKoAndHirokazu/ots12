import discord
from discord.ext import commands
from random import randrange

hug_img = [
    
    "https://images-ext-1.discordapp.net/external/wRVaR9oxLxb_x8dfBSAfcFjCZVWOtjzWnUGzKdjPHhc/https/i.pinimg.com/originals/85/72/a1/8572a1d1ebaa45fae290e6760b59caac.gif",
    "https://i.imgur.com/r9aU2xv.gif?noredirect",
    "https://acegif.com/wp-content/uploads/anime-hug.gif",
    "https://media1.giphy.com/media/lrr9rHuoJOE0w/giphy.gif",
    "https://64.media.tumblr.com/f2a878657add13aa09a5e089378ec43d/tumblr_n5uovjOi931tp7433o1_500.gif",
    "https://media1.tenor.com/images/1d94b18b89f600cbb420cce85558b493/tenor.gif?itemid=15942846",
    "https://acegif.com/wp-content/gif/anime-hug-49.gif",
    "https://media3.giphy.com/media/od5H3PmEG5EVq/200.gif",
    "https://i.imgur.com/ntqYLGl.gif",
    "https://i.imgur.com/39NB7bF.gif",
    "https://i.kym-cdn.com/photos/images/original/001/094/799/80e.gif",
    "http://cdn.lowgif.com/small/86fdce8550402b45-.gif",
    "https://media1.tenor.com/images/5a273335be361bddb8fe464bf3b5bf05/tenor.gif?itemid=12668698",
    "https://media3.giphy.com/media/sUIZWMnfd4Mb6/giphy.gif",
    "https://i.gifer.com/2QEa.gif",
    "https://img.wattpad.com/bd7df5121f2a66747130636a83e51788050441c4/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f354559506c6f6e4f5750526439673d3d2d3932383032323430352e313632356663376363376138363739623236373238343230323237372e676966",
    "https://media.tenor.com/images/0abe1090ab9874c62c4baaac18f0994d/tenor.gif",
    "https://acegif.com/wp-content/gif/anime-hug-17.gif",
    "https://data.whicdn.com/images/219995514/original.gif",
    "https://i.pinimg.com/originals/f9/e9/34/f9e934cddfd6fefe0079ab559ef32ab4.gif",
    "https://i.imgur.com/yEled8h.gif",
    "https://thumbs.gfycat.com/FemaleUnrulyBluebird-small.gif",
    "http://cdn.lowgif.com/small/66af32a828a3fa7d-.gif",
    "https://media.giphy.com/media/l97JVFR42GLWE/giphy.gif",
    "https://i.imgur.com/oltglhh.gif",
    "https://media0.giphy.com/media/qscdhWs5o3yb6/200.gif",
    "https://i.gifer.com/ZMzD.gif",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3mySS0mvtoRtZMRZ8VrXykekHqEeS_TOmKw&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR21dNdOre6XtexZHRS2DEGorBGAxBgtbdLTA&usqp=CAU",
    "https://66.media.tumblr.com/66d391d120dc735a342843bc06aa87ce/tumblr_o30ir8HJkY1uapp8co1_400.gifv"

    ]

kiss_img = [

    "https://media2.giphy.com/media/bGm9FuBCGg4SY/giphy.gif",
    "https://thumbs.gfycat.com/HopefulFabulousKouprey-max-1mb.gif",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2ETuaBSXzo2mfARoJXNh8-PkwVTEzfcte9g&usqp=CAU",
    "https://media1.tenor.com/images/fbc74874ee87628899fb77e77a59efcc/tenor.gif?itemid=138208620",
    "https://i.pinimg.com/originals/22/5d/7e/225d7e533b3ab85d29e92c0ad54c089e.gif",
    "https://d.wattpad.com/story_parts/324/images/1462b50fb380f780689293669071.gif",
    "https://i.pinimg.com/originals/00/62/e0/0062e0db9a92c7055fd58542472bcf8e.gif",
    "https://www.icegif.com/wp-content/uploads/anime-kiss-icegif.gif",
    "https://media.giphy.com/media/FqBTvSNjNzeZG/giphy.gif",
    "https://acegif.com/wp-content/uploads/anime-kissin-15.gif",
    "https://i1.wp.com/nileease.com/wp-content/uploads/2020/08/1a124a8291930684139a85f22158ce54.gif?fit=498%2C275&ssl=1",
    "https://img.wattpad.com/c79f6f4d9cd697da08e71022623df48afb244ea5/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f2d34506c3674775a4a5f35725a513d3d2d3737333034313336312e313562623931613830363634363832643733323130383337383630332e676966",
    "https://64.media.tumblr.com/7bbfd33feb6d790bb656779a05ee99da/tumblr_mtigwpZmhh1si4l9vo1_500.gif",
    "https://i.imgur.com/So3TIVK.gif",
    "https://i.pinimg.com/originals/f1/5c/77/f15c774e5c58a9f210c7f7647da796f1.gif",
    "https://media1.giphy.com/media/bm2O3nXTcKJeU/giphy.gif",
    "https://acegif.com/wp-content/uploads/anime-kiss-22.gif",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4rExaraP6XemQTH56vO-xL4oPOyCNziisxQ&usqp=CAU",
    "http://cdn.lowgif.com/full/116e54dd62085b43-anime-kiss-gifs-page-11-wifflegif.gif",
    "https://data.whicdn.com/images/67193990/original.gif",
    "https://media0.giphy.com/media/G3va31oEEnIkM/200.gif",
    "https://data.whicdn.com/images/144335846/original.gif",
    "https://i0.wp.com/nileease.com/wp-content/uploads/2020/05/e858678426357728038c277598871d6d.gif?fit=498%2C278&ssl=1",
    "https://acegif.com/wp-content/uploads/anime-kissin-8.gif",
    "https://i.pinimg.com/originals/2f/23/c5/2f23c53755a5c3494a7f54bbcf04d1cc.gif",
    "https://steamuserimages-a.akamaihd.net/ugc/933803303914187860/33C5555A58C2B4B507350C6D40E916923B462CC9/",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMtykSpBIWRNfNqkvI_4y6nS58BWsv3_eQTw&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSJmk3UQAU4quIRd1h6_rsmHeZuoGWJ5iBaw&usqp=CAU",
    "https://media1.giphy.com/media/w62BhkdkxaCwE/200.gif",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSN_hRWr_QBzhVdknhlrH1TttLo6iyEQ8S3yQ&usqp=CAU"

]

punch_img = [

    "https://images.app.goo.gl/eBjqaZrdYxhxqVm76",
    "https://images.app.goo.gl/YQB5hvgXVuf87nNM9",
    "https://images.app.goo.gl/ZYgdikjtyviBCrrT7",
    "https://images.app.goo.gl/rkWukCRg6yswQ6GNA",
    "https://images.app.goo.gl/jVhGARndf3bZVRS66",
    "https://images.app.goo.gl/AC4xHSkwTEokkisJ7",
    "https://images.app.goo.gl/dXY7xrEqexdfKobN9",
    "https://images.app.goo.gl/UKe3gnRyEhbXCxyw7",
    "https://images.app.goo.gl/rz6W9sDwScaPDXSz8",
    "https://images.app.goo.gl/bMkACXb4o6VXtL1p7",
    "https://images.app.goo.gl/e7qMmNYm2kzypbL27",
    "https://images.app.goo.gl/eRTPxr6Qq1hj11D2A",
    "https://images.app.goo.gl/DZWVnm2ZzBYwAgfq9",
    "https://images.app.goo.gl/oeEu2Tw7dhryvxfC9",
    "https://images.app.goo.gl/8XCzCAQHpfjryeTD8",
    "https://images.app.goo.gl/gF8mX5wZkuzA832NA",
    "https://images.app.goo.gl/mVzEK6ZEcBaE7jNHA",
    "https://images.app.goo.gl/rDG4yYnCYnA7TFN6A",
    "https://images.app.goo.gl/7GXPcC6bo3ZYYZvT7",
    "https://images.app.goo.gl/5F3y8eCzTYmm2NBd7",
    "https://images.app.goo.gl/GmFxZT76ZpcQb15EA",
    "https://images.app.goo.gl/xrLHC1ba5KmX9HyKA",
    "https://images.app.goo.gl/AMU9YR3W8wKTvgzA6",
    "https://images.app.goo.gl/atxQyaPaMGRxetkR7",
    "https://images.app.goo.gl/YmGDeQzEMqjYEuLC6",
    "https://images.app.goo.gl/rUzBiBXUQrQ393Uv5",
    "https://images.app.goo.gl/gwJRzCheTXmzATUv5",
    "https://images.app.goo.gl/z3mhjDXqQscsUideA",
    "https://images.app.goo.gl/VQoHQ23K6B6U88EZ8",
    "https://images.app.goo.gl/Hzd4cPXtRFuTYGqN9"

]

poke_img = []

class Fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@commands.command(pass_context=True)
	async def avatar(self, ctx, member:discord.Member=None):
		await ctx.send(ctx.message.author.avatar_url)


	@commands.command(pass_context=True)
	async def hug(self, ctx, member: discord.Member=None):
	    if not member:
	        embed=discord.Embed(title="Huggies!", description="**{1}** hugs **{0}**!".format(self.bot.user, ctx.message.author.mention), color=0x176cd5)
	        embed.set_image(url="{}".format(hug_img[randrange(30)]))
	        await ctx.send(embed=embed)
	    else:
	        embed=discord.Embed(title="Huggies!", description="**{1}** hugs **{0}**!".format(member.mention, ctx.message.author.mention), color=0x176cd5)
	        embed.set_image(url="{}".format(hug_img[randrange(30)]))
	        await ctx.send(embed=embed)

	@commands.command(pass_context=True)
	async def kiss(self, ctx):
	    await ctx.send("{}".format(kiss_img[randrange(30)]))

	@commands.command(pass_context=True)
	async def punch(self, ctx):
	    await ctx.send("{}".format(punch_img[randrange(30)]))

def setup(bot):
	bot.add_cog(Fun(bot))