import discord
import os
from dotenv import load_dotenv

VERSION_NAME = "0.0.3"

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print( 
        f"{client.user} is connected to the following guild:\n"
        f"{guild.name}(id: {guild.id})"
    )
    game = discord.Game("endless debugging")
    await client.change_presence(status=discord.Status.dnd, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    question_keywords = ["?", "what", "when", "who", "where", "why", "how"]
    for word in question_keywords:
        if word in message.content.lower():
            await message.channel.send(f"Google it, {message.author.nick}!")
            break

    if message.content.startswith("!version"):
        await message.channel.send(f"Version {VERSION_NAME}")

    if message.content.startswith("!help"):
        embed = discord.Embed(title="Commands", color=10038562)
        embed.add_field(name="!version", value="Lists the version the bot is on", inline=False)
        embed.add_field(name="!info", value="Lists information about the bot", inline=False)
        embed.add_field(name="!iamdumb", value="Gives a statement of semi-apology for idiotic mistakes.", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("!info"):
        info = discord.Embed(title="TestDiscordBot", description="Shasta's little testing bot.", color=10038562)
        info.add_field(name="Current purpose:", value="Learning python, annoying people", inline=True)
        info.add_field(name="Version:", value="0.0.3", inline=True)
        await message.channel.send(embed=info)

    if message.content.startswith("!iamdumb"):
        await message.channel.send("I am dumb and I did a dumb. Ignore my dumbness.")

@client.event
async def on_typing(channel, message, time):
    await channel.send("Hurry up.")

@client.event
async def on_message_delete(message):
    await message.channel.send(message.author.nick + " **deleted a message that said** " + message.content)

if __name__ == "__main__":
    client.run(TOKEN)