import discord
from discord.ext import commands

class github_c(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(name='github')
    async def github(self, ctx):
        await ctx.send('`github.com/ArthiccFox/bixos`')


def setup(bot):
    bot.add_cog(github_c(bot))