# import discord 
# from discord.ext import commands
# import time

# client = commands.Bot(command_prefix = '.',intents=discord.Intents.default())

# @client.event
# async def on_ready():
# 	print('bot is ready')
# 	time.sleep(3)


# async def send_update(lst):
# 	embed = discord.Embed(title="Incoming Message", description="Welcome to NLP test", color=discord.Color.random())
# 	embed.add_field(name="First Name", value=lst[0])
# 	embed.add_field(name="Last Name", value=lst[1])
# 	embed.add_field(name="City", value=lst[2])
# 	embed.add_field(name="Message ", value=lst[3])


# client.run('Nzk5NTM2MDU0ODE3OTE0OTUw.GneH86.7Pn2naCMD7LuNKXwaWzOEqX8hWCxyvx8nAgGu0')

from discord import Webhook
import aiohttp

async def foo():
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url('https://discordapp.com/api/webhooks/1080312781141725194/7PohXsZ3qrmR87L56XVFRovRpOFMBKmASFbkREYOAYclslae1gZ8DbPO2cLHkOCQ34xn', session=session)
        await webhook.send('Hello World', username='Foo')
foo()