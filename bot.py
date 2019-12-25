"""Main module of the discord bot"""
import logging
import os
import random
import time

import discord
import asyncio

import settings as s

async def run():
    """on_ready
    on_message"""
    with open('quotes.html', 'r') as f:
        messages = f.read().split(',')
  
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user.name} has connected to Discord!')

    @client.event
    async def on_message(msg):
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
            "hentai",
            "kawaii"
            ))
        for t in triggers:
            if contains_word(msg, t):
                response = random.choice(messages)
                await msg.channel.send(response)


    def contains_word(s, w):
        return (' ' + str(w) + ' ') in (' ' + s + ' ')

    client.run(s.discord_token)

while True:
    await run()
    time.sleep(300)

