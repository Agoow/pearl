import os
import discord
import psycopg2
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

# Connexion DB PostgreSQL
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('😨 Connecting to the PostgreSQL database...')
        conn = psycopg2.connect( 
            host=os.getenv("db_host"),
            database=os.getenv("db_name"),
            user=os.getenv("db_user"),
            password=os.getenv("db_password"))
		
        # create a cursor
        cur = conn.cursor()
        
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print('📖 PostgreSQL database connected [', db_version, ']')
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('📕 Database connection closed.')
connect()

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
# channel IMAJMEME :    190815749328207872,
# channel COMMANDES:    398284500670611466
# channel BISTRO:       138323612091285504
####################################################################################################
#load  cog :
#@client.commmand()
#async def load(ctx, extension):
#    client.load_extension(f'plugins.{extension}')
####################################################################################################
