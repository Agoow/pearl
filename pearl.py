import os
import discord
from discord.ext import commands
#from discord.ext.commands import Bot
from discord.ext.commands import has_permissions, MissingPermissions
# import datetime
# import asyncio
# import re
# import urllib
# import opengraph
from dotenv import load_dotenv
load_dotenv()

client = commands.Bot(command_prefix='*')  # , description="Bot polyvalent(vraiment pas)")

@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):  # , *, reason=None
    await member.kick()  # reason=reason
    await ctx.send(f"{member} n'était pas assez bourré, il a donc été expulsé")

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member):  # , *, reason=None
    await member.ban()  # reason=reason
    await ctx.send(f"{member} devenait vraiment trop gênant , il a donc été BANNI")

for filename in os.listdir('./addons'):
    if filename.endswith(".py"):
        client.load_extension(f'addons.{filename[:-3]}')

client.run(os.getenv("pearltoken"))

####################################################################################################
# history = message.channel.history(limit=200) - 200 derniers messages sur le channel dans lequel est passé la commande
####################################################################################################
# command_name = message.content[len(prefix):]
#      await dispatch_commands(command_name, message)
#          async def dispatch_commands(command_name, message):
#    if command_name == 'te':
#       await message.channel.send('st')
####################################################################################################
# @client.event
# async def on_message(message):
#    if message.channel.id == 398284500670611466 and not message.author.bot:
# urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content)
# if urls:
# print(urls[0])
# message.channel.id == 398284500670611466 and message.content in message.channel.history():
####################################################################################################
# serveur BISTRO :      138323612091285504
#   channel IMAJMEME :    190815749328207872
#   channel COMMANDES:    398284500670611466
# serveur PEEPS :       223225472702480385
#   channel COMMANDES:    277141231484796929
####################################################################################################
#load  cog :
#@client.commmand()
#async def load(ctx, extension):
#    client.load_extension(f'plugins.{extension}')
####################################################################################################
