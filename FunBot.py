import discord
import random
import asyncio
import sys
import http
import aiohttp
import os
import json
import giphypop
from giphypop import translate


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
	#help command. 
	if message.content.startswith('{}help'.format(cmd)):
		msg = '```Heres a list of my commands:'\
			'\n\n-Ping - Bot simply replies ping (unless your special) useful for knowing whether or not It\'s online'\
			'\n\n-cat - Bot posts a random cat picture'\
			'\n\n-trump - Bot posts a random Trump gif'\
			'\n\n-hillary - Bot posts a random Hillary gif'\
			'\n\n-bernie - Bot posts a random Bernie gif'\
			'\n\n-horse - Bot posts a random horse gif'\
			'\n\n-dog - Bot posts a random dog gif'\
			'\n\n-restart - restarts the bot (only works for the bot owner)'\
			'\n\n-guess - starts the guessing game'\
			'\n\n-mark - a special song written by Bahar for Mark'\
			'\n\nBot coded by Blake with help from Zach.```'\
		
		await client.send_message(message.channel, msg)
	#Ping command. 
	elif message.content.startswith('{}ping'.format(cmd)):
		if message.author.id == '129437909131591680':
			msg = 'Bang, Bang! {0.author.mention}'.format(message)
			await client.send_message(message.channel, msg)
		elif message.author.id == '183790956754108416':
			msg = 'Hello Master! :wave: {0.author.mention}'.format(message)
			await client.send_message(message.channel, msg)
		elif message.author.id == '129439119737749505':
			msg  = 'You\'re a nerd. you ain\'t got no balls! {0.author.mention}'.format(message)
			await client.send_message(message.channel, msg)
		elif message.author.id == '238469392155803649':
			msg = 'Hello Queen Alexis! :wave: {0.author.mention}'.format(message)
			await client.send_message(message.channel, msg)
		else:
			msg = 'PONG! {0.author.mention}'.format(message)
			await client.send_message(message.channel, msg)
	#cat command
	elif message.content.startswith('{}cat'.format(cmd)):
		async with aiohttp.get('http://random.cat/meow') as r:
			if r.status == 200:
				js = await r.json()
				await client.send_message(message.channel,js['file'])
	#Trump command
	elif message.content.startswith('{}trump'.format(cmd)):
		img = translate('Trump', api_key='dc6zaTOxFJmzC')
		await client.send_message(message.channel,img)	
	#Hillary command
	elif message.content.startswith('{}hillary'.format(cmd)):
		img = translate('Hillary', api_key='dc6zaTOxFJmzC')	
		await client.send_message(message.channel,img)
	#Bernie command
	elif message.content.startswith('{}bernie'.format(cmd)):
		img = translate('Bernie', api_key='dc6zaTOxFJmzC')
		await client.send_message(message.channel,img)
	#Horse command
	elif message.content.startswith('{}horse'.format(cmd)):
		img = translate('Horse', api_key='dc6zaTOxFJmzC')
		await client.send_message(message.channel,img)
	#Dog command
	elif message.content.startswith('{}dog'.format(cmd)):
		img = translate('Dog', api_key='dc6zaTOxFJmzC')
		await client.send_message(message.channel,img)
	#Restart command
	elif message.content.startswith('{}restart'.format(cmd)):
		if message.author.id == '183790956754108416':
			msg = '```Restarting!!```'
			await client.send_message(message.channel, msg)
			os.execl(sys.executable, sys.executable, *sys.argv)
		elif message.author.id == '129437909131591680':
			msg = '```Restarting!!```'
			await client.send_message(message.channel, msg)
			os.execl(sys.executable, sys.executable, *sys.argv)
		else:
			msg = '```ERROR: What the fuck do you think you\'re doing?!```'
			await client.send_message(message.channel, msg)
	#Mark command
	elif message.content.startswith('{}mark'.format(cmd)):
		msg = '```Mark is a nerd. He ain\'t got no balls.'\
			'\n\nHis dick isn\'t big and his asshole\'s not small.'\
			'\n\nThem weird ol voices make you wanna die.'\
			'\n\nSingin\' pen pinapple until the day that I die.'\
			'\n\nSingin\' pen pineapple until the day I die.```'
		await client.send_message(message.channel, msg)
	#Guess command
	elif message.content.startswith('{}guess'.format(cmd)):
		await client.send_message(message.channel, 'Guess a number between 1 to 10')

		def guess_check(m):
			return m.content.isdigit()

		guess = await client.wait_for_message(timeout=5.0, author=message.author, check=guess_check)
		answer = random.randint(1, 10)
		if guess is None:
			fmt = 'Sorry, you took too long. It was {}.'
			await client.send_message(message.channel, fmt.format(answer))
			return
		if int(guess.content) == answer:
			await client.send_message(message.channel, 'You are right!')
		else:
			await client.send_message(message.channel, 'Sorry. It is actually {}.'.format(answer))


@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(Token)