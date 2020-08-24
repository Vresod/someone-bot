#!/usr/bin/env python3
import discord
import random

with open("tokenfile", "r") as tokenfile:
	token=tokenfile.read()

client = discord.Client()

@client.event
async def on_ready():
	print("logged in as {0.user}".format(client))
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
		await message.channel.send(f"{randomuser.mention}")

client.run(token)