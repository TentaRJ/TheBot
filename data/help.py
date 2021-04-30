import discord

helptxt=discord.Embed(title="Hello", description=f"I am a bot that manages a server!\nI was built in Python!\nIf you have the staff role, type `helpadmin` when writing a command!", colour=discord.Color.magenta())
helptxt.set_footer(text="A simple bot made in Python!")

helptxtadmin=discord.Embed(title="Hello", description=f"I am a bot that manages a server!\nI was built in Python!", colour=discord.Color.gold())
helptxtadmin.add_field(name="Add", value="`?add [word]`\nAdds a word to the ban list.", inline=True)
helptxtadmin.set_footer(text="A simple bot made in Python!")