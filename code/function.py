import asyncio

class function:
  async def check(ctx):
    await ctx.channel.send("Woah buddy! Don't say that!", delete_after=10)