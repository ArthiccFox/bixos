import discord
from discord.ext import commands

class help_c(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help', aliases=["ajuda", "h"])
    async def help(self, ctx):
        embed = discord.Embed(title="comandos")
        embed.add_field(name="`?registrar`", value="registre sua conta pra usar o bot\n", inline = True)
        embed.add_field(name="`?caçar`", value="tenta pega os bixo ai doido\ncada bixo tem sua probabilidade de cair, entao tenta a sorte ai", inline = False)
        embed.add_field(name="`?info`", value="você pode saber as informações de sua conta, ou de outra pessoa usando o id dela", inline = False)
        embed.add_field(name="`?pfp`", value="troque a sua foto de perfil com um bixo de seu inventario!\n", inline = True)
        embed.add_field(name="`?shop`", value="catalogo de venda de armas\n para comprar uma arma digite `?buy <id da arma>`", inline = False)
        embed.add_field(name="`?vender`", value="No mercado negro, voce pode vender bixos\npara vender, use:`?vender (id do seu item)`", inline = False)
        embed.add_field(name="`?relatos`", value="ao caçar relatos, voce pode achar uma lenda, um bixo que nunca antes foi visto (ate mesmo pela clinica)\npara caçar use: `?relatos caçar` (700 Mangos)", inline = False)
        embed.add_field(name="`Ajuda?`", value="Caso precise de alguma ajuda/deseja reportar algum bug, entre em contato comigo!\n`Jorney#6902`", inline = False)
        embed.set_footer(text="github.com/ArthiccFox/bixos")
        channel = ctx.channel
        await channel.send(embed=embed)



def setup(bot):
    bot.add_cog(help_c(bot))