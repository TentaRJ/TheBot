import asyncio
import discord
import json
import os
import sys
import time
from code.function import *
from code.keepalive import *
from data.ban import banlist
from discord.ext import commands

client = commands.Bot(command_prefix="?")
client.botid = "798286010944585759"

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game(name=f"Connected! Using this bot as a test!!"))
  print(f"Ready!\nDiscord.py Version {discord.__version__}\nPython Version {sys.version}")

@client.event
async def on_message(ctx):
  print(f'{ctx.author.id} {ctx.content.lower()}')
  if ''.join([str(x) for x in banlist])  in ctx.content.lower():
    await function.check(ctx, ctx.author.id)

try:
  from code.token import token
  client.run(token['token'])
except:
  print(f"Uh oh! Something happened!\n\nThere was a token error!\n\nCheck code.token.token!")
  time.sleep(3)
  exit()

keepalive()