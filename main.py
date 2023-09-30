import os
import discord

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
  print(f"Logged in as [{client.user}]")


@client.event
async def on_message(message):
  if message.author == client.user:  #No messages when the bot is the author
    return

  if message.content.upper().startswith('!HELLO'):
    await message.channel.send("Hello !")
  else:
    print(f"No response to send: Message was ==> {message.content}")
    await message.channel.send("No Hello !")


client.run(os.environ['BOT_TOKEN'])  #Connexion to the Discord Server
