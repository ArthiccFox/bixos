import discord
from discord.ext import commands
import sqlite3
import json
import asyncio
class vender_c(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='vender')
    async def vender(self, ctx, item):
        author = ctx.message.author
        conn = sqlite3.connect(f"./users/p_users.db")
        c = conn.cursor()
        cfind = conn.cursor()
        c.execute(f"""SELECT * FROM tb_users WHERE U_ID='{author.id}'; """)
        reg = list(c.fetchone())

        if reg != None:
        
            if int(item) < 20:
                f = open("./bixos/bixos.json", encoding="utf8")
                data = json.load(f)
                filtroid = [user for user in data if user['id']==int(item)][0]
            elif int(item) > 100:
                f = open("./relatos/relatos.json", encoding="utf8")
                data = json.load(f)
                filtroid = [user for user in data if user['id']==int(item)][0]
            bixoval = filtroid["valor"]
            cfind.execute(f"""SELECT * FROM tb_users WHERE U_ID='{author.id}'; """)
            if reg[3] == int(item):
                c.execute(f"UPDATE tb_users SET U_MONEY='{reg[2] + int(bixoval)}' WHERE U_ID={author.id}")
                c.execute(f"UPDATE tb_users SET U_BIXOS1='0' WHERE U_ID={author.id}")
                await ctx.send("bixo vendido no mercado negro")
                conn.commit()
                return False
            elif reg[4] == int(item):
                c.execute(f"UPDATE tb_users SET U_MONEY='{reg[2] + int(bixoval)}' WHERE U_ID={author.id}")
                c.execute(f"UPDATE tb_users SET U_BIXOS2='0' WHERE U_ID={author.id}")
                await ctx.send("bixo vendido no mercado negro")
                conn.commit()
                return False
            elif reg[5] == int(item):
                c.execute(f"UPDATE tb_users SET U_MONEY='{reg[2] + int(bixoval)}' WHERE U_ID={author.id}")
                c.execute(f"UPDATE tb_users SET U_BIXOS3='0' WHERE U_ID={author.id}")
                await ctx.send("bixo vendido no mercado negro")
                conn.commit()
                return False
            else:
                await ctx.send("voce nao possui esse item")
        else:
            await ctx.send("voce nao tem conta, digite `?registrar`")




    @vender.error
    async def info_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(" ?vender <id do bixo>")

def setup(bot):
    bot.add_cog(vender_c(bot))