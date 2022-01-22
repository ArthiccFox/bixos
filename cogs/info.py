import discord
from discord.ext import commands
import sqlite3
import json
class info_c(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='info', aliases=["profile", "p"])
    async def info(self, ctx, uid):
        conn = sqlite3.connect(f"./users/p_users.db")
        co = conn.cursor()
        co.execute(f"""SELECT * FROM tb_users WHERE U_ID='{int(uid)}'; """)

        if co.fetchone() == None:
            await ctx.send("este usuario nao tem conta")
        else:
            c = conn.cursor()
            c.execute(f"""SELECT * FROM tb_users WHERE U_ID='{int(uid)}'; """)
            reg = list(c.fetchone())
            f1 = open("./bixos/bixos.json", encoding="utf8")
            f2 = open("./relatos/relatos.json", encoding="utf8")
            data2 = json.load(f2)
            data1 = json.load(f1)


            if reg[3] != 0:
                print(reg[3])
                if reg[3] < 20:
                    filtroid = [bixo for bixo in data1 if bixo['id']==reg[3]][0]
                    nome1 = filtroid["nome"]
                    bixoid1 = filtroid["id"]
                elif reg[3] > 100:
                    filtroid = [bixo for bixo in data2 if bixo['id']==reg[3]][0]
                    nome1 = filtroid["nome"]
                    bixoid1 = filtroid["id"]
            else:
                nome1, bixoid1 = "--"
            if reg[4] != 0:
                if reg[4] < 20:
                    filtroid = [bixo for bixo in data1 if bixo['id']==reg[4]][0]
                    nome2 = filtroid["nome"]
                    bixoid2 = filtroid["id"]
                elif reg[4] > 100:
                    filtroid = [bixo for bixo in data2 if bixo['id']==reg[4]][0]
                    nome1 = filtroid["nome"]
                    bixoid1 = filtroid["id"]
            else:
                nome2, bixoid2 = "--"

            if reg[5] != 0:
                if reg[5] < 20:
                    filtroid = [bixo for bixo in data1 if bixo['id']==reg[5]][0]
                    nome3 = filtroid["nome"]
                    bixoid3 = filtroid["id"]
                elif reg[5] > 100:
                    filtroid = [bixo for bixo in data2 if bixo['id']==reg[5]][0]
                    nome1 = filtroid["nome"]
                    bixoid1 = filtroid["id"]
            else:
                nome3, bixoid3 = "--"

            f = open(f"./armas/{reg[6]}.json", "r")
            armadata = json.load(f)
            nomearma = armadata["nome"]
            rariarma = armadata["raridade"]
            forçaarma = armadata["forca"]

            embed = discord.Embed(title=reg[1])
            embed.add_field(name='carteira', value=reg[2], inline = False)
            embed.add_field(name='inventario', value=f"`{nome1}` `id: {bixoid1}`\n`{nome2}` `id: {bixoid2}`\n`{nome3}` `id: {bixoid3}`", inline = False)
            embed.add_field(name="arma", value=f"`{nomearma}\nraridade:{rariarma}\nforça:{forçaarma}`", inline = False)
            if reg[7] != None:
                if reg[7] < 20:
                        filtroid = [bixo for bixo in data1 if bixo['id']==reg[7]][0]
                        pngname = filtroid["pngname"]
                        nome = filtroid["nome"]
                        file = discord.File(f"./bixos/{pngname}.png", filename=f"{pngname}.png")
                if reg[7] > 100:
                    filtroid = [bixo for bixo in data2 if bixo['id']==reg[7]][0]
                    pngname = filtroid["pngname"]
                    nome = filtroid["nome"]
                    file = discord.File(f"./relatos/{pngname}.png", filename=f"{pngname}.png")
                embed.set_image(url=f"attachment://{pngname}.png")
                embed.set_footer(text=f"bixo na foto: {nome}")
                await ctx.send(embed=embed, file=file)
            else:
                await ctx.send(embed=embed)

    @info.error
    async def info_error(self, ctx, error):
        print(error)
        if isinstance(error, commands.MissingRequiredArgument):
            author = ctx.message.author
            conn = sqlite3.connect(f"./users/p_users.db")
            co = conn.cursor()
            co.execute(f"""SELECT * FROM tb_users WHERE U_ID='{author.id}'; """)

            if co.fetchone() == None:
                await ctx.send("voce nao tem conta, digite `?registrar`")
            else:
                c = conn.cursor()
                c.execute(f"""SELECT * FROM tb_users WHERE U_ID='{author.id}'; """)
                reg = list(c.fetchone())
                f1 = open("./bixos/bixos.json", encoding="utf8")
                f2 = open("./relatos/relatos.json", encoding="utf8")
                data2 = json.load(f2)
                data1 = json.load(f1)

                if reg[3] != 0:
                    if reg[3] < 20:
                        filtroid = [bixo for bixo in data1 if bixo['id']==reg[3]][0]
                        nome1 = filtroid["nome"]
                        bixoid1 = filtroid["id"]
                    elif reg[3] > 100:
                        filtroid = [bixo for bixo in data2 if bixo['id']==reg[3]][0]
                        nome1 = filtroid["nome"]
                        bixoid1 = filtroid["id"]
                else:
                    nome1, bixoid1 = "--"
                if reg[4] != 0:
                    if reg[4] < 20:
                        filtroid = [bixo for bixo in data1 if bixo['id']==reg[4]][0]
                        nome2 = filtroid["nome"]
                        bixoid2 = filtroid["id"]
                    elif reg[4] > 100:
                        filtroid = [bixo for bixo in data2 if bixo['id']==reg[4]][0]
                        nome2 = filtroid["nome"]
                        bixoid2 = filtroid["id"]
                else:
                    nome2, bixoid2 = "--"

                if reg[5] != 0:
                    if reg[5] < 20:
                        filtroid = [bixo for bixo in data1 if bixo['id']==reg[5]][0]
                        nome3 = filtroid["nome"]
                        bixoid3 = filtroid["id"]
                    elif reg[5] > 100:
                        filtroid = [bixo for bixo in data2 if bixo['id']==reg[5]][0]
                        nome3 = filtroid["nome"]
                        bixoid3 = filtroid["id"]
                else:
                    nome3, bixoid3 = "--"

                
                
                f = open(f"./armas/{reg[6]}.json", "r")
                armadata = json.load(f)
                nomearma = armadata["nome"]
                rariarma = armadata["raridade"]
                forçaarma = armadata["forca"]

                embed = discord.Embed(title=author.name)
                embed.add_field(name='carteira', value=reg[2], inline = False)
                embed.add_field(name='inventario', value=f"`{nome1}` `id: {bixoid1}`\n`{nome2}` `id: {bixoid2}`\n`{nome3}` `id: {bixoid3}`", inline = False)
                embed.add_field(name="arma", value=f"`{nomearma}\nraridade:{rariarma}\nforça:{forçaarma}`", inline = False)
                if reg[7] != None:
                    if reg[7] < 20:
                        filtroid = [bixo for bixo in data1 if bixo['id']==reg[7]][0]
                        pngname = filtroid["pngname"]
                        nome = filtroid["nome"]
                        file = discord.File(f"./bixos/{pngname}.png", filename=f"{pngname}.png")
                    if reg[7] > 100:
                        filtroid = [bixo for bixo in data2 if bixo['id']==reg[7]][0]
                        pngname = filtroid["pngname"]
                        nome = filtroid["nome"]
                        file = discord.File(f"./relatos/{pngname}.png", filename=f"{pngname}.png")
                    
                    embed.set_image(url=f"attachment://{pngname}.png")
                    embed.set_footer(text=f"bixo na foto: {nome}")
                    await ctx.send(embed=embed, file=file)
                else:
                    await ctx.send(embed=embed)
        else:
            print(error)

def setup(bot):
    bot.add_cog(info_c(bot))