import discord

class functions:
  async def punish(ctx, member):
    try:
      await ctx.delete()
    except:
      pass
    else:
      pass
    await ctx.channel.send("Woah buddy! Don't say that!", delete_after=5)
    if isinstance(ctx.channel, discord.channel.DMChannel):
      pass
    else:
      await ctx.author.send(f"Woah! You can't be saying those things! Consider this a warning!", delete_after=120)

  async def add(ctx, word=''):
    if word=="":
      print("No word added!")
    else:
      print("Adding", word)
      wordfile=open("data/ban.py", "w+")
      x=wordfile[:-1]
      y=f'{x}, "{word}"]'
      wordfile.write(y)
      wordfile.close()
      await ctx.channel.send(f'`Added!`')

      