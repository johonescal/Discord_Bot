import discord
import analysis
import os

client = discord.Client()

@client.event
async def on_message(message):
    analys: int = 0
    #anlys: int = analysis.main(message.content)

    if anlys == 0:
        await message.delete()
        await client.send_message(message.channel, "モラルが守れていないメッセージを削除しました。")

client.run(os.environ.get("discord_token"))
