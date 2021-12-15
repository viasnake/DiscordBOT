import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print("logged in as " + client.user.name)


@client.event
async def on_message(message):
    if message.author != client.user:
        msg = message.author.mention + " Hi."
        await message.channel.send("お呼びかな？")


client.run(os.environ["TOKEN"])
