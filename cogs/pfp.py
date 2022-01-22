from discord.ext import commands
import json
import sqlite3

class pfp_c(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def pfp(self, ctx, bid):
        author = ctx.message.author
        conn = sqlite3.connect(f"./users/p_users.db")
        co = conn.cursor()
        co.execute(f"""SELECT * FROM tb_users WHERE U_ID='{author.id}'; """)

        if co.fetchone() != None:
            co.execute(f"""SELECT * FROM tb_users WHERE U_ID='{author.id}'; """)
            reg = list(co.fetchone())
            temobixo = False
            table = None
            if reg[3] == int(bid):
                temobixo = True
                table = "U_BIXOS1"
            elif reg[4] == int(bid):
                temobixo = True
                table = "U_BIXOS2"
            elif reg[5] == int(bid):
                temobixo = True
                table = "U_BIXOS3"
            else:
                await ctx.send("voce não tem o bixo")

            if temobixo == True:
                co.execute(f"UPDATE tb_users SET U_PFP='{int(bid)}' WHERE U_ID={author.id}")
                co.execute(f"UPDATE tb_users SET {table}='0' WHERE U_ID={author.id}")
                await ctx.send("sua foto de perfil foi atualizada")
                return conn.commit()

        else:
            await ctx.send("voce nao tem conta, digite `?registrar`")
    @pfp.error
    async def info_error(self, ctx, error):
        print(error)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("?pfp <id do bixo>")



def setup(bot):
    bot.add_cog(pfp_c(bot))