import discord
import os

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    anlys: int = analysis.main(message.content)

    if anlys == 0:
        await message.delete()
        await message.channel.send(message.author.mention + 'モラルが守れていないメッセージを削除しました。')
    else:
        pass

client.run(os.environ.get('discord_token'))
