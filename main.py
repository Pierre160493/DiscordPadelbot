import os
import discord
from datetime import datetime
import pytz

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

  #lastBotMsg = await message.channel.history().find(
  #lambda m: m.author.id == client.user.id)
  #   lambda m: m.author == client.user)
  #channel = client.get_channel(message.channel.id)
  #print(channel.id)
  #lastBotMsg = channel.history(limit=1)
  #if lastBotMsg is not None:
  #  print(lastBotMsg.flatten())

  ############ Gestion des parties
  strIdentifiantNumMessage = "/"  #Char qui sépare le numero des différentes itérations des demandes d'informations
  #  if message.content.upper().startswith("!PARTIE"):
  if message.content.upper().startswith("P"):
    await message.author.send("# 1" + strIdentifiantNumMessage +
                              " Quel est le jour et l'heure de la partie ?" +
                              os.linesep + "## Réponse attendue:" +
                              os.linesep + "Jour Mois Heure:Minute" +
                              2 * os.linesep + "### Exemple pour maintenant:" +
                              os.linesep +
                              datetime.now(pytz.timezone('Europe/Paris')
                                           ).strftime("%-d %-m %-Hh%-M") +
                              os.linesep + "### Autres exemples" + os.linesep +
                              "1er Janvier à 8h ==> [1 1 8] ou [01 1 8h00]")
    return

  if message.content.startswith("# 1" + strIdentifiantNumMessage):
    await message.author.send("# Bienvenue dans le gestionnaire de parties" +
                              2 * os.linesep + "1" + strIdentifiantNumMessage +
                              " Quel est le jour et l'heure de la partie ?" +
                              os.linesep + "  Réponse attendue:" + os.linesep +
                              "Jour Mois Heure:Minute" + 2 * os.linesep +
                              "  Exemple pour maintenant:" + os.linesep +
                              datetime.now(pytz.timezone('Europe/Paris')).
                              strftime("%-d %-m %-Hh%-M") + 2 * os.linesep +
                              "  Autres exemples" + os.linesep +
                              "1er Janvier à 8h ==> [1 1 8] ou [01 1 8h00]")


client.run(os.environ['BOT_TOKEN'])  #Connexion to the Discord Server
