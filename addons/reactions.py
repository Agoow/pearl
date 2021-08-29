import discord
from discord.ext import commands


class reactions(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Streaming(name="Pearl", url="https://www.twitch.tv/Imcatjam"))
        print('connecté au(x) serveur(s)')

    async def on_message(message):
        if message.author == client.user:
            return

        msg = message.content
        if msg.lower() == "cringe":
            await message.delete()
            await message.channel.send("https://tenor.com/view/dies-of-cringe-cringe-gif-20747133")  # ,delete_after=5

        if msg.lower() == "bonne nuit" or message.content.lower() == "a plus" or message.content.lower() == "au revoir" or message.content.lower() == "https://tenor.com/view/au-revoir-giscard-ciao-aplus-att-gif-4737220":
            await message.channel.send("https://tenor.com/view/au-revoir-giscard-ciao-aplus-att-gif-4737220")

        if msg.lower() == "you":
            await message.delete()
            await message.channel.send('https://cdn.discordapp.com/attachments/751532937094103132/847173219961405490'
                                       '/image0.gif')


def setup(client):
    client.add_cog(reactions(client))
