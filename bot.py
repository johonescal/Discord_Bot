import discord
import os

import test_curry

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    anlys: int = test_curry.main(message.content)

    if anlys == 1:
        await message.delete()
        await message.channel.send(message.author.mention + ' カレーの話をしてないので、メッセージを削除しました。')

client.run(os.environ.get('discord_token'))
