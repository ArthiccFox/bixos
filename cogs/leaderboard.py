import discord
from discord.ext import commands
import sqlite3

class buy_c(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["ranking"])
    async def leaderboard(self, ctx):
        conn = sqlite3.connect(f"./users/p_users.db")
        co = conn.cursor()
        co.execute(f"SELECT U_MONEY,U_NAME FROM tb_users;")
        reg = co.fetchall()
        reg.sort(reverse=True)

        champ1 = reg[0]
        champ2 = reg[1]
        champ3 = reg[2]

        embed = discord.Embed(title="Ranking", description="los melhores caçadores del 2002")
        embed.add_field(name=f"{champ1[1]}", value=f"\n{champ1[0]} Mangos", inline= False)
        embed.add_field(name=f"{champ2[1]}", value=f"{champ2[0]} Mangos", inline= False)
        embed.add_field(name=f"{champ3[1]}", value=f"{champ3[0]} Mangos", inline= False)


        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(buy_c(bot))