import os
import discord
from datetime import datetime
import pytz
import asyncio
import pytest

client = discord.Client(intents=discord.Intents.all())

strIdentifiantNumMessage = "/"  #Char qui sépare le numero des différentes itérations des demandes d'informations du bot


@client.event
async def on_ready():
  print(f"Logged in as [{client.user}]")


@client.event
async def on_message(message):
  if message.author == client.user:  #No messages when the bot is the author
    return

  if message.content.upper().startswith('!HELLO'):
    await message.channel.send("Hello !")


############ Gestion des parties
###### Traitement des messages précédents si c'est en DM et s'ils existent
  if isinstance(message.channel,
                discord.channel.DMChannel):  #Si le message provient d'une DM
    message.channel.typing()
    await asyncio.sleep(1)
    lastMsg = await discord.utils.find(lambda m: m.author == client.user,
                                       message.channel.history())
    if lastMsg is not None:  #Si on a bien trouvé un message
      ###### Traitement du premier message: Gestion de la date
      if lastMsg.content.startswith("# 1" + strIdentifiantNumMessage):
        lastMsg = await discord.utils.find(
            lambda m: m.author == message.author, message.channel.history())
        print("Last Message =" + lastMsg.content)
        date_partie = None
        for format in ("%-d %-m %-Hh%-M", "%-d %-m %-Y"):
          print(format)
          try:
            date_partie = datetime.strptime(lastMsg.content, format)
          except ValueError:
            pass
          if date_partie is not None:
            break
        if date_partie is None:
          await message.author.send(
              "# 1" + strIdentifiantNumMessage +
              " ERREUR dans l'interpretation de la date fournie" + os.linesep +
              "## Réponse obtenue:" + os.linesep + lastMsg.content +
              2 * os.linesep + "# Veuillez réessayer" + os.linesep +
              "## Réponse attendue:" + os.linesep + "Jour Mois Heure:Minute" +
              2 * os.linesep + "### Exemple pour maintenant:" + os.linesep +
              datetime.now(pytz.timezone('Europe/Paris')).strftime(
                  "%-d %-m %-Hh%-M") + os.linesep + "### Autres exemples" +
              os.linesep + "1er Janvier à 8h ==> [1 1 8] ou [01 1 8h00]")
        else:
          await message.author.send("# 2" + strIdentifiantNumMessage +
                                    " Date du match" + os.linesep +
                                    "## Réponse obtenue:" + os.linesep +
                                    date_partie.strftime("%Y-%m-%d %H:%M") +
                                    2 * os.linesep + "# Selection du lieu" +
                                    2 * os.linesep + "## Réponse attendue:" +
                                    os.linesep + "4Padel Creteil")

  #  if message.content.upper().startswith("!PARTIE"):
  if message.content.upper().startswith("P"):
    message.channel.typing()  #N'a pas l'air de marcher
    #await asyncio.sleep(10)
    await message.author.send("# 1" + strIdentifiantNumMessage +
                              " Quel est le jour et l'heure de la partie ?" +
                              os.linesep +
                              "## Réponse attendue: Jour Mois Heure:Minute" +
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
