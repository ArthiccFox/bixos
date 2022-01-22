from tkinter import W
from discord.ext import commands
import sqlite3
import json
import random
import discord
import asyncio

class relatos_c(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.cooldown(5, 600, commands.BucketType.user)
    async def relatos(self, ctx, ccr):
        author = ctx.message.author
        conn = sqlite3.connect(f"./users/p_users.db")
        co = conn.cursor()
        co.execute(f"""SELECT * FROM tb_users WHERE U_ID='{author.id}'; """)

        if co.fetchone() != None:
                if ccr == "caçar":
                    f = open("./relatos/relatos.json", encoding="utf8")
                    data = json.load(f)

                    co.execute(f"""SELECT * FROM tb_users WHERE U_ID='{author.id}'; """)
                    reg = list(co.fetchone())
                    money = reg[2]
                    arma = reg[6]
                    print(arma)
                    g = open(f"./armas/{arma}.json")
                    armadata = json.load(g)
                    armaprob = armadata['rprob']
                    caçarchoice = [1, 2]
                    caçar = random.choices(caçarchoice, weights=armaprob)[0]

                    if caçar == 1:
                        await ctx.send("infelizmente a equipe de caça especializada não conseguiu capturar o relato...")
                        co.execute(f"UPDATE tb_users SET U_MONEY='{money - 700}' WHERE U_ID={author.id}")
                        return conn.commit()
                    elif caçar == 2:
                        bixo = data[random.choice([1,2])]
                        name = bixo['nome']
                        desc = bixo['relato']
                        pngname = bixo['pngname']
                        idbixo = bixo['id']
                        valor = bixo['valor']
                        file = discord.File(f"./relatos/{pngname}.png", filename=f"{pngname}.png")
                        embed = discord.Embed(title=name)
                        embed.add_field(name="desc", value=desc, inline=False)
                        embed.add_field(name="id", value=idbixo, inline=True)
                        embed.add_field(name="valor", value=valor, inline=True)
                        embed.set_image(url=f"attachment://{pngname}.png")
                        await ctx.send(embed=embed, file=file)

                        co.execute(f"""SELECT * FROM tb_users WHERE U_ID='{author.id}'; """)
                        reg = list(co.fetchone())
                        ischeio = False

                        def checktb(message):
                            return message.author == author and message.content == f"caçar {idbixo}"

                        while True:
                            try:
                                await self.bot.wait_for('message', timeout=60, check=checktb)
                                if reg[3] == 0:
                                    ischeio = False
                                    regchave = "U_BIXOS1"
                                elif reg[4] == 0:
                                    ischeio = False
                                    regchave = "U_BIXOS2"
                                elif reg[5] == 0:
                                    ischeio = False
                                    regchave = "U_BIXOS3"
                                else:
                                    ischeio = True

                                if ischeio == False:
                                    co.execute(f"UPDATE tb_users SET {regchave}='{idbixo}' WHERE U_ID={author.id}")
                                    co.execute(f"UPDATE tb_users SET U_MONEY='{money - 700}' WHERE U_ID={author.id}")
                                    await ctx.send(f"o bixo {name} é teu!!!11!1!")
                                    return conn.commit()
                                else:
                                    co.execute(f"UPDATE tb_users SET U_MONEY='{money - 700}' WHERE U_ID={author.id}")
                                    await ctx.send("nao tem espaço")
                                    return conn.commit()
                            except asyncio.TimeoutError:
                                break
                    else:
                        print("a")
                    
                


            
        else:
            await ctx.send("voce nao tem conta, use ?registrar")
    @relatos.error
    async def info_error(self, ctx, error):
        print(error)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("os relatos são bixos lendarios que apenas são caçados com buscas especializadas\n para caçar um lendario, digite ?lendario caçar, porem isto custara 700 mangos")

def setup(bot):
    bot.add_cog(relatos_c(bot))