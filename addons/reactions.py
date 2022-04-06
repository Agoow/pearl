import discord
import random
from discord.ext import commands
import asyncio


class reactions(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="des vidéos de chiens", url="https://www.youtube.com/watch?v=wl4m1Rqmq-Y"))
        print('🤖 Bot Discord connecté au(x) serveur(s)')

    @commands.Cog.listener("on_message")
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        msg = message.content.lower()

#########################################################REACTIONS PAR GIF###################################################################################################################

        if self.client.user.mentioned_in(message):
            if 'je code' in msg:
                await message.channel.send("https://media3.giphy.com/media/ihZE9sgAahmFIdc7v8/giphy.gif?cid=790b761153213dec39b72ed0fe35ee554c0298086dcab629")
            elif ('debout' in msg) or ('là' in msg) or ('eh' in msg):
                await message.channel.send("https://media0.giphy.com/media/1hMaFTOrK2MhgH6uhY/giphy.gif?cid=ecf05e47bmkm1fxl86drx7i5w4rapmouk5s4lsnm6noj08mz")
            elif ('pote' in msg) or ('mec' in msg) or ('gars' in msg):
                bot_message = "J'suis " + random.choice(['pas ', '']) +"ton " + random.choice(['mec', 'gars', 'pote']) + ", mon " + random.choice(['mec', 'gars', 'pote']) + " !"
                await message.channel.send(bot_message)
            else:
                bot_message = 'Je vais te boter le cul si tu me mentionnes encore, ' + message.author.name + ' !'
                await message.channel.send(bot_message)

        if msg == "*cringe":
            await message.delete()
            await message.channel.send("https://tenor.com/view/dies-of-cringe-cringe-gif-20747133")  # ,delete_after=5

        if msg == "bonne nuit" or msg == "a plus" or msg == "au revoir" or msg == "https://tenor.com/view/au-revoir-giscard-ciao-aplus-att-gif-4737220":
            await message.channel.send("https://tenor.com/view/au-revoir-giscard-ciao-aplus-att-gif-4737220")

        if msg == "you":
            await message.delete()
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/751532937094103132/847173219961405490/image0.gif')

        if msg == "tgm4":
            await message.channel.send("https://readmanganato.com/manga-hu985229/chapter-122")

################################################################MODULE FX + SAYD #######################################################################################################
        #
            #        if msg.startswith('https://twitter.com/'):
            #                await message.channel.send(msg.replace('twitter', 'fxtwitter', 1))
        #                        await message.delete()
        #
            #        if msg.startswith('*sayd'):
            #            await message.delete()
        #            await message.channel.send(msg.replace('*sayd', '', 1))
        #
###############################################################tarkov###################################################################################################################

        if msg == "woods":
            await message.channel.send("https://www.gamemaps.co.uk/game/tarkov/maps/glory4life_updated_feb_2021")

        if msg == "shoreline":
            await message.channel.send("https://www.gamemaps.co.uk/game/tarkov/maps/shoreline_3d_maksen")

        if msg == "customs":
            await message.channel.send("https://www.gamemaps.co.uk/game/tarkov/maps/customs_clean_monkimonkimonk")

        if msg == "twiki":
            await message.channel.send("https://escapefromtarkov.gamepedia.com/")

        if msg == "tierlist":
            await message.channel.send("https://docs.google.com/spreadsheets/d/e/2PACX-1vR3Exvsyc4wwDlck-Vaj5MznG8NgERJ-u-q4ZoVEaO6yxLF-pGZ7jouYkEMoR0HFqq2pzImNWnAwxKE/pubhtml")

        if msg.startswith('!p'):
            await message.delete()

        if 'lowest price' in msg.content:
           #print(type(message))
            #print(message.content)
            #await asyncio.sleep(5)
            message.delete()


###############################################################tarkov###################################################################################################################


def setup(client):
    client.add_cog(reactions(client))
