# bot.py
from auth import *
from plex import *
import discord
from discord import app_commands
from discord.ext import commands

TOKEN = DISCORD_TOKEN

serverOfflineMessage = "The Server is currently offline"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "hello", description = "My first application Command",) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@tree.command(name = "relaodmovies", description = "Scan library for new movies",) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
    if isServeronline():
        addmovies()
    else:
        await interaction.response.send_message(serverOfflineMessage)
    
@tree.command(name = "relaodseries", description = "Scan library for new show",) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
    if isServeronline():
        addshows()
    else:
        await interaction.response.send_message(serverOfflineMessage)

@tree.command(name = "reloadguide", description = "Reload the live tv Guide",) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
    if isServeronline():
        reloadguide()
        await interaction.response.send_message("Live TV Guide reloaded!")
    else:
        await interaction.response.send_message(serverOfflineMessage)

@client.event
async def on_ready():
    await tree.sync()
    print("Ready!")

def test():
    if isServeronline():
        addmovies()
        print("Added Movies")
    else:
        print(serverOfflineMessage)

def isServeronline():
    import requests
    page = requests.get(serverURL)
    return True


# client.run(TOKEN)
# client.run()
