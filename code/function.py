import discord

class function:
  async def check(ctx, member):
    await ctx.delete()
    await ctx.channel.send("Woah buddy! Don't say that!", delete_after=5)
    await ctx.author.send(f"Woah! You can't be saying those things! Consider this a warning!", delete_after=120)