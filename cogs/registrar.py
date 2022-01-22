import discord
from discord.ext import commands
import sqlite3
from sqlite3 import Error


def banconnect():
    path = f"./users/p_users.db"
    con = None
    try:
        con = sqlite3.connect(path)
    except Error as ex:
        print(ex)
    return con
vcon = banconnect()


class reg_c(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='registrar')
    async def registrar(self, ctx):
        author = ctx.message.author
        vsql=f"""INSERT INTO tb_users 
                (U_id, U_NAME)
            VALUES('{author.id}','{author.name}')"""
        def insert(conexao, sql):
            try:
                c=conexao.cursor()
                c.execute(sql)
                conexao.commit()
                print('registro inserido')
            except Error as ex:
                print(ex)
                
        insert(vcon, vsql)
        await ctx.send('voce registrou')
    
def setup(bot):
    bot.add_cog(reg_c(bot))