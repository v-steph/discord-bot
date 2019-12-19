"""Main module of the discord bot"""
import logging
import os
import random
import time

import discord
import asyncio
from smart_open import open 

import settings as s

  
client = discord.Client()
messages = open(s.responses, 'r')

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(msg):
    """check message for trigger word"""
    # prevent bot msg recursion
    if msg.author == client.user:
        return

    triggers = set(opt.lower() for opt in (
        "anime", 
        "uwu", 
        "owo", 
        "weeb", 
        "chan", 
        "kun", 
        "senpai", 
        "sempai", 
        "kokoro", 
        "doki",
        "hentai"
        ))
    for t in triggers:
        if contains_word(msg, t):
            response = random.choice(messages)
            await msg.channel.send(response)


def contains_word(s, w):
    return (' ' + str(w) + ' ') in (' ' + s + ' ')

client.run(s.discord_token)



