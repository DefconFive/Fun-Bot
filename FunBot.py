import discord
import random
import asyncio
import sys
import http
import aiohttp
import os
import json
client = discord.Client()
#bot setup for dual testing
#Uncomment depending on who you are.
#Blake's Setup
Token = 'MjIzMjQ5NTQzNTc4MjU1MzYw.Cu2Dpg.1US_ESdFGSVWMLbnWJIHQd1QnQU'
# this is the bot command prefix
cmd = '-'
#Zach's Setup
#Token = 'MjI0NzE5NjI1OTIzODU0MzM2.Cremqw.tKWTMcD9SqF_nThAjJ3krj9uXWw'
# this is the bot command prefix
#cmd = '--'



@client.event
async def on_message(message):
	# we do not want the bot to reply to itself
	if message.author == client.user:
		return
	#Ping command. 
	if message.content.startswith('{}help'.format(cmd)):
		await client.send_message(message.channel,'help?')
	#Ping command. 
	elif message.content.startswith('{}ping'.format(cmd)):
		if message.author.id == '129437909131591680':
			msg = 'Bang, Bang! {0.author.mention}'.format(message)
			await client.send_message(message.channel, msg)
		elif message.author.id == '183790956754108416':
			msg = 'Hello Master! :wave: {0.author.mention}'.format(message)
			await client.send_message(message.channel, msg)
		elif message.author.id == '129439119737749505':
			msg  = ':middle_finger: {0.author,mention}'.format(message)
			await client.send_message(message.channel, msg)
		else:
			msg = 'PONG! {0.author.mention}'.format(message)
			await client.send_message(message.channel, msg)
	# cat command
	elif message.content.startswith('{}cat'.format(cmd)):
		async with aiohttp.get('http://random.cat/meow') as r:
			if r.status == 200:
				js = await r.json()
				await client.send_message(message.channel,js['file'])

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(Token)