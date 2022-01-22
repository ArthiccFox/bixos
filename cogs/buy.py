import discord
from discord.ext import commands
import sqlite3
import json
class buy_c(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def buy(self, ctx, bid):
        author = ctx.message.author
        conn = sqlite3.connect(f"./users/p_users.db")
        co = conn.cursor()
        cfind = conn.cursor()
        f = open(f"./armas/{bid}.json", "r")
        dataarma = json.load(f)
        valuearma = dataarma["valor"]
        co.execute(f"""SELECT * FROM tb_users WHERE U_ID='{author.id}'; """)

        if co.fetchone() != None:
            
            cfind.execute(f"""SELECT * FROM tb_users WHERE U_ID='{author.id}'; """)
            reg = list(cfind.fetchone())
            print(valuearma)
            if reg[2] > 0:
                if reg[2] < int(valuearma):
                    await ctx.send("voce e pobre nao pode compra essa arma")
                else:
                    co.execute(f"UPDATE tb_users SET U_MONEY='{reg[2] - int(valuearma)}' WHERE U_ID={author.id}")
                    co.execute(f"UPDATE tb_users SET U_ARMA='{bid}' WHERE U_ID={author.id}")
                    await ctx.send("arma comprada")
                    return conn.commit()
            else:
                await ctx.send("voce é MUITO pobre kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")


        else:
            await ctx.send("voce nao tem conta, digite `?registrar`")


def setup(bot):
    bot.add_cog(buy_c(bot))