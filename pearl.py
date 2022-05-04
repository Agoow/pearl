import os
import discord
from discord.ext import commands
import random
import json
import requests
#import urlparse, os
from os.path import splitext
from urllib.parse import urlparse
#from discord.ext.commands import Bot
from discord.ext.commands import has_permissions, MissingPermissions
import datetime
# import asyncio
# import urllib
# import opengraph
from dotenv import load_dotenv
import youtube_dl
import unicodedata
import re
load_dotenv()

client = commands.Bot(command_prefix='*')  # , description="Bot polyvalent(vraiment pas)")

# Fonction pour convertir en nom de fichier
def slugify(value, allow_unicode=False):
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')

# Commande Chien Random
@client.command()
async def dog(ctx):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    if(response.status_code == 200):
        response = response.json()
        if(response['message']):
            await ctx.send(response['message'])
    else :
        await ctx.send("Soit autonome, va chercher toi-même !")

# Commande Is Gay
@client.command()
async def gay(ctx, member: discord.Member):
    if(random.random() < 0.3):
        await ctx.send(f"{member.name} est clairement gay")
    else:
        await ctx.send(f"{member.name} n'est clairement pas gay")

# Commande Faim
@client.command()
async def faim(ctx):
    response = requests.get("https://foodish-api.herokuapp.com/api/")
    if(response.status_code == 200):
        response = response.json()
        if(response['image']):
            await ctx.send(response['image'])
    else :
        await ctx.send("Soit autonome, va chercher toi-même !")

# Commande pour DL mp3 depuis YTB
@client.command()
async def ymp3(ctx, video_url: str):
    # Est-ce que l'url est bien une URL youtube ?
    if ("youtube" in video_url) or ("youtu.be" in video_url) :
        await ctx.send("Ok, je m'en charge, veuillez patienter...")
        video_info = youtube_dl.YoutubeDL().extract_info(
            url = video_url,download=False
        )
        filename = f"{slugify(video_info['title'])}.mp3"
        filepath = f"/tmp/{filename}"
        options={
            'format'    :    'bestaudio/best',
            'keepvideo' :    False,
            'outtmpl'   :    filepath,
        }

        print("Téléchargement en cours ...")

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        await ctx.send(f"Téléchargement terminé : {format(filename)}")
        await ctx.send(file=discord.File(r'/tmp/%s' % filename))
    else:
        await ctx.send("Je ne fonctionne qu'avec les liens \"youtube.com\" / \"youtu.be\"")

# Commande Kick
@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):  # , *, reason=None
    await member.kick()  # reason=reason
    await ctx.send(f"{member} n'était pas assez bourré, il a donc été expulsé")

# Commande Ban
@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member):  # , *, reason=None
    await member.ban()  # reason=reason
    await ctx.send(f"{member} devenait vraiment trop gênant , il a donc été BANNI")

# Ajout des addons
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
