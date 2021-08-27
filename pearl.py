import discord
from discord.ext import commands
# import datetime
# import asyncio
# import re
# import urllib
# import opengraph

# cog_files = ['commands.commands']


bot = commands.Bot(command_prefix='*', description="Bot polyvalent(vraiment pas)")
client = discord.Client()

# for cog_file in cog_files:
#    client.load_extension(cog_file)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="Pearl", url="https://www.twitch.tv/Imcatjam"))
    print('connecté au serveur(s)')


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    msg = message.content
    if msg.lower() == "cringe":
        await message.delete()
        await message.channel.send("https://tenor.com/view/dies-of-cringe-cringe-gif-20747133")  # ,delete_after=5

    if msg.lower() == "bonne nuit" or message.content.lower() == "adieu" or message.content.lower() == "a plus" or message.content.lower() == "au revoir"or \
            message.content.lower() =="https://tenor.com/view/au-revoir-giscard-ciao-aplus-att-gif-4737220":
        await message.channel.send("https://tenor.com/view/au-revoir-giscard-ciao-aplus-att-gif-4737220")

    if msg.lower() == "you":
        await message.delete()
        await message.channel.send("https://cdn.discordapp.com/attachments/751532937094103132/847173219961405490"
                                   "/image0.gif")


client.run("ODgwMDcxODkyNDQ5NTAxMjE0.YSY80g.vkrruEkpH0NJPpPgG0Z52AkF0Yg")


# history = message.channel.history(limit=200)  # 200 derniers messages sur le channel dans lequel est passé la commande
# if message.content in message.channel.history(limit=500).flatten():
#  await message.channel.send("repost")
####################################################################################################
# command_name = message.content[len(prefix):]
#      await dispatch_commands(command_name, message)
#          async def dispatch_commands(command_name, message):
#    if command_name == 'cr':
#       await message.channel.send('inge')
####################################################################################################

# @client.event
# async def on_message(message):
#    if message.channel.id == 398284500670611466 and not message.author.bot:
# urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content)
# if urls:
# print(urls[0])

# message.channel.id == 398284500670611466 and message.content in message.channel.history():
####################################################################################################
# channel IMAJMEME :    190815749328207872,
# channel COMMANDES:    398284500670611466
# channel BISTRO:       138323612091285504
####################################################################################################
