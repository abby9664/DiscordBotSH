import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print( 
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    question_keywords = ["?", "what", "when", "who", "where", "why", "how"]
    for word in question_keywords:
        if word in message.content.lower():
            await message.channel.send(f"Google it, {message.author.nick}!")
            break

@client.event
async def on_typing(channel):
    await channel.send('Hurry up.')

if __name__ == "__main__":
    client.run(TOKEN)