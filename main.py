from flask import Flask
from discord.ext import commands
from threading import Thread
import discord
import json

print('BrianYT Notifier')

app = Flask('')

@app.route('/')
def main():
  return "Bot is currently online!"

def run():
  app.run(host="0.0.0.0", port=8000)

def keep_alive():
  server = Thread(target=run)
  server.start()

configFile = open('config.json', 'r')
config = json.load(configFile)

client = commands.Bot(command_prefix="b!")

@client.event
async def on_message(message):
  if message.content.startswith(config['keyword']):
    print('Keyword found')
    if str(message.channel.id) != config['listenChannelID']:
      return
    url = message.content.replace(config['keyword'], '')
    msg = f'@everyone\nB_RIAN just uploaded!\nGo check it!\n{url}'
    for guild in client.guilds:
      for channel in guild.channels:
        if str(channel.id) == config['uploadChannelID']:
          await channel.send(msg)
    print(f'Notified {url}')

@client.event
async def on_ready():
  print('Bot online!')    

@client.command(name="cleardoxx")
async def cleardoxx(ctx):
  print('command called')
  async for message in ctx.channel.history(limit = 100):
        if 'dhruv' in message.content.lower():
          await message.delete()

client.run(config['token'])
client.add_command(cleardoxx)   
 
