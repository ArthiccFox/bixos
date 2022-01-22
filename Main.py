import discord
from discord.ext import commands
import os


TOKEN = ''
bot = commands.Bot(command_prefix='t?', help_command=None)

@bot.event
async def on_ready():
   print('online')
   print(bot.user.name)
   print(bot.user.id)
   await bot.change_presence(activity=discord.Game(name="caso algum problema me avise: Jorney#6902"))


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

#----------------------------#

@bot.event
async def on_message(message):
    client = f'<@!{bot.user.id}>'
    if message.content == client:
        await message.channel.send("`prefixo: '?'\n exemplo: ?help`")
    await bot.process_commands(message)

bot.run(TOKEN)