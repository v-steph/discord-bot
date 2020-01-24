"""Scan incoming chat messages for trigger words. when triggered reply with string from .txt file."""

import logging
import os
import random
import time
import re

import discord
import asyncio
from smart_open import open 
import json

import settings as s

async def run():
    """on_ready
    on_message"""
    
  
client = discord.Client()
with open('quotes.json', 'r') as f:
        messages = json.load(f)
        print(messages)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(msg):
    """check message for trigger word"""
    # prevent bot spamming
    if msg.author == client.user:
        return
    # behold. the hackiest transformation in history.
    triggers = set(opt.lower().center(len(opt)+2) for opt in (
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
        "hentai",
        "nani",
        "kawaii"
        ))
    for t in triggers:
        if t.lower() in msg.content.lower():
            print(messages)
            response = random.choice(messages)
            await msg.channel.send(response['q'])


client.run(s.discord_token)



