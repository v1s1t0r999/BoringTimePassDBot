import discord
import requests as r
from discord.ext import commands
import random

class Waifu(commands.Cog, description="Some Weeb shit?!"):
    def __init__(self, bot):
        """
		Waifus Related Weeb Shit.
		Commands: 
		  `waifu`: Get a hot waifu.
		  `nwaifu`: Get a hot waifu, but clothless or smth..
		"""
        self.bot = bot

    # Waifu
    @commands.command(name="waifu", help="Sends an random SFW Waifu Image")
    async def waifu(self, ctx:commands.Context):
        site = r.get("https://api.waifu.im/sfw/waifu/")
        response = site.json()
        sfwmbed = discord.Embed(
            color=self.bot.color,
            url=F"https://waifu.im/preview/?image={response['images'][0]['file']}",
            title="Here is your SFW Waifu Image!!",
            timestamp=ctx.message.created_at
        )
        sfwmbed.set_image(url=response.get('images')[0].get('url'))
        sfwmbed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=sfwmbed)
    
    # NWaifu
    @commands.command(name="nwaifu", help="Sends an random NSFW Waifu Image", aliases=['nw'])
    @commands.is_nsfw()
    async def nwaifu(self, ctx:commands.Context,nsfw_type=None):
        ntypes = ['ass', 'ecchi', 'ero', 'hentai', 'maid', 'milf', 'oppai', 'oral', 'paizuri', 'selfies', 'uniform']
        if not nsfw_type:
            nsfw_type=random.choice(ntypes)
        elif not nsfw_type in ntypes:
            return await ctx.send(embed=discord.Embed(title="Tryna break me?? You British!?",description="NSFW type should be either of the following:\n"+", ".join(ntypes).title()),colour=0xFFC0CB)
        site = r.get(f"https://api.waifu.im/nsfw/{nsfw_type}/")
        response = site.json()
        nsfwmbed = discord.Embed(
            color=self.bot.color,
            url=F"https://waifu.im/preview/?image={response.get('images')[0].get('file')}",
            title="Here is your NSFW {0} Image".format(nsfw_type.title()),
            timestamp=ctx.message.created_at
        )
        nsfwmbed.set_image(url=response.get('images')[0].get('url'))
        nsfwmbed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=nsfwmbed)

def setup(bot):
    bot.add_cog(Waifu(bot))
