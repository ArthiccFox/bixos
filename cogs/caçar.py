import discord
from discord.ext import commands
import asyncio
import json
import sqlite3
import random


ba = open("./bixos/bixos.json", encoding="utf8")
bixosdata = json.load(ba)
Comum = (bixosdata[0], bixosdata[1],bixosdata[2],bixosdata[3],bixosdata[4],bixosdata[5])
Medio = (bixosdata[6], bixosdata[7],bixosdata[8],bixosdata[9],bixosdata[10],bixosdata[11])
Raro = (bixosdata[12], bixosdata[13],bixosdata[14],bixosdata[15],bixosdata[16],bixosdata[17])
bixos = (Comum, Medio, Raro)



class caçar_c(commands.Cog):

    def __init__(self, bot):
        self.bot = bot



      


    
    @commands.command(name='caçar')
    @commands.cooldown(5, 600, commands.BucketType.user)
    async def caçar(self, ctx):

        author = ctx.message.author
        conn = sqlite3.connect(f"./users/p_users.db")
        c = conn.cursor()
        cfind = conn.cursor()
        c.execute(f"""SELECT * FROM tb_users WHERE U_ID='{author.id}'; """)

        

        if c.fetchone() == None:
            await ctx.send("voce nao tem conta, digita `?registrar`")
        else:
            c.execute(f"""SELECT * FROM tb_users WHERE U_ID='{author.id}'; """)
            reg = list(c.fetchone())
            f = open(f"./armas/{reg[6]}.json", "r")
            dataarma = json.load(f)
            armaprov = dataarma["provabilidade"]
            bixoprob = random.choices(bixos, weights=armaprov)[0]
            bixo = random.choice(bixoprob)

            nome = bixo["nome"]
            pngname = bixo["pngname"]
            desc = bixo["desc"]
            raridade = bixo["raridade"]
            bixoid = bixo["id"]
            mvalor = bixo["valor"]



            file = discord.File(f"./bixos/{pngname}.png", filename=f"{pngname}.png")
            embed = discord.Embed(title=nome)
            embed.add_field(name='descrição', value=desc, inline = False)
            embed.add_field(name='valor', value=mvalor, inline = False)
            embed.add_field(name='id', value=bixoid, inline=True)
            embed.add_field(name='raridade', value=raridade, inline=True)
            embed.set_image(url=f"attachment://{pngname}.png")
            embed.set_footer(text=f"pra caçar apenas digite 'caçar {bixoid}'")

            channel = ctx.channel
            await channel.send(file=file, embed=embed)
            def checktb(message):
                return message.author == author and message.content == f"caçar {bixoid}"
            while True:
                try:
                    await self.bot.wait_for('message', timeout=60, check=checktb)
                    cfind.execute(f"""SELECT * FROM tb_users WHERE U_ID='{author.id}'; """)
                    reg = list(cfind.fetchone())
                
                    if reg[3] == 0:
                        c.execute(f"UPDATE tb_users SET U_BIXOS1='{bixoid}' WHERE U_ID={author.id}")
                        await ctx.send(f"o bixo {nome} é teu!!!11!1!")
                        conn.commit()
                        return False
                    elif reg[4] == 0:
                        c.execute(f"UPDATE tb_users SET U_BIXOS2='{bixoid}' WHERE U_ID={author.id}")
                        await ctx.send(f"o bixo {nome} é teu!!!11!1!")
                        conn.commit()
                        return False
                    elif reg[5] == 0:
                        c.execute(f"UPDATE tb_users SET U_BIXOS3='{bixoid}' WHERE U_ID={author.id}")
                        await ctx.send(f"o bixo {nome} é teu!!!11!1!")
                        conn.commit()
                        return False
                    else:
                        await ctx.send("seu inventario esta cheio")
                    
                except asyncio.TimeoutError:
                    break

    @caçar.error
    async def roll_error(self, ctx, error):
        print(error)
        if isinstance(error, discord.ext.commands.errors.CommandOnCooldown):
            await ctx.send("voce ta em cooldown esper 10 minuto ")


def setup(bot):
    bot.add_cog(caçar_c(bot))
