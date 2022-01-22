import discord
from discord.ext import commands
import sqlite3


class shop_c(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def shop(self,ctx):
        author = ctx.message.author
        conn = sqlite3.connect(f"./users/p_users.db")
        co = conn.cursor()
        co.execute(f"""SELECT * FROM tb_users WHERE U_ID='{author.id}'; """)

        if co.fetchone() != None:
            embed = discord.Embed(title="Catalogo da loja")
            embed.add_field(name="38 enferrujada", value=f"`valor: 3500\nraridade: comum\n força: 4/10\n id: 2`")
            embed.set_footer(text=f"pra comprar uma arma, use o comando ?buy <id da arma>'")
            await ctx.send(embed=embed)
        else:
            await ctx.send("voce nao tem conta")
        

def setup(bot):
    bot.add_cog(shop_c(bot))