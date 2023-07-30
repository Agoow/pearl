import asyncio
import datetime
import os
import random
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import requests
from dotenv import load_dotenv

load_dotenv()

discord_token = os.getenv("DISCORD_TOKEN")

# Variables
DOG_API_LINK = 'https://dog.ceo/api/breeds/image/random'

# Variables Unsplash
ID_UNSPLASH = 'S4Lem4GYBh0ULXVFbdAXWAOMDguJCDH3mBk2l3OQkrY'
URL_UNSPLASH = 'https://api.unsplash.com/search/photos'

# Les intents (j'ai bof compris pk ça existe cette merde)
intents = discord.Intents.default()
intents.message_content = True

# Le prefix
bot = commands.Bot(command_prefix='*', intents=intents)

#----------------------------------------------------- Events ------------------------------------------------------
@bot.event
async def on_ready():
    print(f"oui c'est bon")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Bing chilling"))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "salut" in message.content.lower():
        await message.channel.send('Bonjour :|')
        
    if message.content.lower() == 'feur':
        await message.channel.send("T'es vraiment qu'un sale chien")

    if ":ptdr:504329599468044319" in message.content.lower():
        await message.channel.send("<:PTDR:504329599468044319>")

    # Laisser ça pour qu'il puisse continuer à traiter les commandes
    await bot.process_commands(message)

#--------------------------------------------------- Fin events ----------------------------------------------------



#--------------------------------------------------- Commandes -----------------------------------------------------
# API qui renvoie une photo aléatoire de chien
@bot.command()
async def dog(ctx):
    response = requests.get(DOG_API_LINK)
    if response.status_code == 200:
        response = response.json()
        if(response['message']):
            await ctx.send(response['message'])
    else :
        await ctx.send("No doge today")

# Commande pour kick un utilisateur
@bot.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):  # , *, reason=None
    await member.kick()  # reason=reason
    await ctx.send(f"{member} n'était pas assez bourré, il a donc été expulsé")

# Commande pour ban un utilisateur
@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member):  # , *, reason=None
    await member.ban()  # reason=reason
    await ctx.send(f"{member} devenait vraiment trop gênant , il a donc été BANNI")


# L'image d'astronomie du jour 
@bot.command
async def schedule_daily_message():      
	while True:
		now = datetime.datetime.now()
		#then = now+datetime.timedelta(days=1)
		then = now.replace(hour=00, minute=20)
		wait_time = (then-now).total_seconds()
		await asyncio.sleep(wait_time)

		channel = discord.BotIntegration.get_channel(1018264148133552210)

		await channel.send("https://www.cidehom.com/apod.php")


# Sly veut une commande qui renvoie une image aléatoire de raton-laveur (Unsplash)
@bot.command()
async def raccoon(ctx):
    url = URL_UNSPLASH
    params = {
        "query": "raccoon",
        "per_page": 100,
        "client_id": ID_UNSPLASH # Lien pour l'ID : https://unsplash.com/oauth/applications "Access Key"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            # Choix aléatoire d'un raccoon random
            image_url = random.choice(data['results'])['urls']['regular']
            await ctx.send(image_url)
        else:
            await ctx.send("Sadge, no raccoon for you")

#------------------------------------------------ Fin commandes ----------------------------------------------------

# Lancement du bot
# Test pull
bot.run(discord_token)