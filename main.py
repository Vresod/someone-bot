#!/usr/bin/env python3
import discord
import random
from sys import argv as cliargs

with open("tokenfile", "r") as tokenfile:
	token=tokenfile.read()

changeNick = False if "dontChangeNick" in cliargs else True # default value: True
includeBots = True if "includeBots" in cliargs else False # default value: False
print(f"changeNick: {changeNick}\nincludeBots: {includeBots}")

client = discord.Client()
@client.event
async def on_guild_join(guild):
	if(not changeNick):
		return
	for guild in client.guilds:
		if guild.me.nick != "someone":
			await guild.me.edit(nick="someone")

@client.event
async def on_ready():
	print("logged in as {0.user}".format(client))
	if(not changeNick):
		return
	for guild in client.guilds:
		if guild.me.nick != "someone":
			await guild.me.edit(nick="someone")

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	memberlist = message.guild.members
	if message.guild.me in message.mentions:
		randomuser = memberlist[random.randint(0,len(memberlist))]
		while includeBots or randomuser.bot:
			randomuser = memberlist[random.randint(0,len(memberlist) - 1)]
		await message.channel.send(f"{randomuser.mention}")

client.run(token)