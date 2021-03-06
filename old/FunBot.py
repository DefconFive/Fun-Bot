import discord
import random
import asyncio
import sys
import http
import aiohttp
import os
import json

from discord.ext import commands
from discord import utils
from discord.object import Object
from discord.enums import ChannelType
from discord.voice_client import VoiceClient
from discord.ext.commands.bot import _get_variable
#from discord.message import Message
#from discord.client import Client

client = discord.Client()



description = '''Funbot is a bot made for fun (obviously)! Written in Python by Blake with help from his good friend Zach.'''


bot = commands.Bot(command_prefix='--', description=description)




# @bot.command(description='Bot simply replies Pong! useful for knowing if its online or not')	
# async def ping():
# 	"""Bot replies Pong!"""
# 	print('ping1')
# 	msg = 'Hello {0.author.mention}'.format(message)
# 	await client.send_message(message.channel, msg)
# 	print(member)
# 	print('ping2')

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
	"""Chooses between multiple choices."""
	await bot.say(random.choice(choices))
	
@bot.command()
async def say(*, message: str):
	"""Makes the bot say something"""
	await bot.say(message)
	
@bot.command()
async def roll(dice : str):
	"""Rolls a dice in NdN format."""
	try:
		rolls, limit = map(int, dice.split('d'))
	except Exception:
		await bot.say('Format has to be in NdN!')
		return

	result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
	await bot.say(result)

@bot.command()
async def repeat(times : int, content='repeating...'):
	"""Repeats a message multiple times."""
	if times > 5:
		await bot.say('```ERROR: Cannot repeat more than 5 times!```', delete_after=20)
	else:	
		for i in range(times):
			await bot.say(content, delete_after=20)

@bot.command()
async def cat():
	"""Posts a random cat picture"""
	async with aiohttp.get('http://random.cat/meow') as r:
		if r.status == 200:
			js = await r.json()
			await bot.say(js['file'], delete_after=20)

@bot.command()
async def restart():
	"""restarts bot"""
	await bot.say('```Restarting!!```')
	os.execl(sys.executable, sys.executable, *sys.argv)

@bot.event
async def on_message(message):
	# we do not want the bot to reply to itself
	if message.author == bot.user:
		return

	if message.content.startswith('-guess'):
		await bot.send_message(message.channel, 'Guess a number between 1 to 10')

		def guess_check(m):
			return m.content.isdigit()

		guess = await bot.wait_for_message(timeout=5.0, author=message.author, check=guess_check)
		answer = random.randint(1, 10)
		if guess is None:
			fmt = 'Sorry, you took too long. It was {}.'
			await bot.send_message(message.channel, fmt.format(answer))
			return
		if int(guess.content) == answer:
			await bot.send_message(message.channel, 'You are right!')
		else:
			await bot.send_message(message.channel, 'Sorry. It is actually {}.'.format(answer))

	await bot.process_commands(message)

	if message.content.startswith('--ping'):
		msg = 'PONG {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)


@bot.event			
async def on_ready():

	print('Logged in as:')
	print('Name:'  + bot.user.name)
	print('id:'  + bot.user.id)
	print('------')

#Blake's Token
#bot.run('MjIzMjQ5NTQzNTc4MjU1MzYw.Cu2Dpg.1US_ESdFGSVWMLbnWJIHQd1QnQU')
#Zach's Token
bot.run('MjI0NzE5NjI1OTIzODU0MzM2.Cremqw.tKWTMcD9SqF_nThAjJ3krj9uXWw')