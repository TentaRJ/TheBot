import asyncio
import discord
import json
import os
import sys
import time
from code.function import functions
from code.keepalive import *
from data.ban import banlist
from data.help import helptxt, helptxtadmin
from discord.ext import commands

cmdprefix="?"
client = commands.Bot(command_prefix=cmdprefix, intents=discord.Intents.all(), help_command=None)
botid = "798286010944585759"

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game(name=f"Connected! Using this bot as a test!!"))
  print(f"Ready!\nDiscord.py Version {discord.__version__}\nPython Version {sys.version}")

@client.event
async def on_message(ctx):
  print(f'{ctx.author.id} Name: {ctx.author.name}#{ctx.author.discriminator} {ctx.content.lower()}')
  if ''.join([str(x) for x in banlist])  in ctx.content.lower():
    await functions.punish(ctx, ctx.author.id)
  else:
    await client.process_commands(ctx)

@client.command(name="helpadmin")
@commands.has_any_role('admin', 'staff')
async def help(ctx):
  await ctx.channel.send(f"Sending you a DM {ctx.author.mention}!", delete_after=5)
  await ctx.author.send(embed=helptxtadmin)

@client.command(name="help")
async def help(ctx):
  if isinstance(ctx.channel, discord.channel.DMChannel):
    await ctx.channel.send(embed=helptxt)
  else:
    await ctx.channel.send(f"Sending you a DM {ctx.author.mention}!", delete_after=5)
    await ctx.author.send(embed=helptxt)

# @client.command(name="add")
# async def add(ctx, word=''):
#   await functions.add(ctx, word)

try:
  from code.token import token
  client.run(token['token'])
except:
  print(f"Uh oh! Something happened!\n\nThere was a token error!\n\nCheck code.token.token!")
  time.sleep(3)
  exit()

keepalive()