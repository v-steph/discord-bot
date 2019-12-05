"""Main module of the discord bot"""
import logging
import os
import random
import time

import discord
import asyncio

import settings as s

async def main():
    """on_ready
    on_message"""
    messages = [
        "I feel so bad for people who unironically like anime. Like, they didn't choose to be born with an IQ of 20 in a home with unloving parents. Imagine all the bullying they must experience at home, at school, and at the special services daycare. Let's stop bullying them, guys. They may be too retarded to understand that's what we're doing, but that doesn't mean we should pick on them. Thank you",
        "Is there an anime character stronger than Madara Uchiha? And I'm referring to Rinne Tensei Madara Uchiha with the Eternal Mangekyou Sharingan and Rinnegan doujutsus (with the rikidou paths ability) equipped with his Gunbai and control of the juubi and Gedou Mazou, a complete Susano'o, with Hashirama Senju's DNA implanted in his chest so he can perform Mokuton kekkei genkai and yin-yang release ninjutsu as well as being extremely skilled in taijutsu and bukijutsu",
        "i got this new anime plot. basically there’s this high school girl except she’s got huge boobs. i mean some serious honkers. a real set of badonkers. packin some dobonhonkeros. massive dohoonkabhankoloos. big ol’ tonhongerekoogers. what happens next?! transfer student shows up with even bigger bonkhonagahoogs. humongous hungolomghononoloughongous",
        "ᵘʷᵘ oh frick ᵘʷᵘ ᵘʷᵘ ᵘʷᵘ ᵘʷᵘ ᵘʷᵘ ᵘʷᵘ ᵘʷᵘ ᵘʷᵘ frick sorry guys ᵘʷᵘ ᵘʷᵘ ᵘʷᵘ ᵘʷᵘ ᵘʷᵘ ᵘʷᵘ sorry im dropping ᵘʷᵘ my uwus all over the ᵘʷᵘ place ᵘʷᵘ ᵘʷᵘ ᵘʷᵘ sorry",
        "Would you pwease put on some kawaii anime music, perhaps puddi puddi in G Minor?",
        "First of all, I'm sick of the term 'Weeb'. I didn't study half a semester of Japanese history and do a google maps tour of Tokyo so that some uncultured swine would walk around calling me a weeb like its an insult. Japanese culture is my life, not some sort of past time you idiots. And yes, I will be visiting Japan for the first time next year when air travel costs go down.",
        "I sexually Identify as a WEEB. Ever since I was a boy I dreamed of AYAYA. People say to me that a person being a WEEB is Impossible and I'm fucking retarded but I don't care, I'm cute. From now on I want you guys to call me 'AYAYA-CHAN' and respect my right to be cute. If you can't accept me you're a racist and need to check your privilege. Thank you for being so understanding.",
        "Apparently I 'ruined' Thanksgiving dinner by bringing my girlfriend Asuka. My mum didn't care that she was a giat robot pilot, tasked with protecting the world after the Second Impact. She insisted that Asuka isn't real and now we're banned from the local country club. Anyways, my mum says if I don't bring a 'real' girl to our Christmas dinner I'm going to get kicked out of the house!!! Asuka sets the bar pretty high but if you think you can compete with her please message me :)",
        "(◕‿◕✿) Dear Weebs in the chat, you are sugoi. Whatever is going on in your kokoro right now, please know that you are kawaii and your story is not a filler. You are loved (◕‿◕✿)",
        "You see this fictional character? I'm not afraid to admit that I've lost liters of cum to this character of mere fantasy. Isn't it funny how not even real women arouse me like she does? I have killed millions of my offspring to the thought of having an intercourse with a cartoon"
    ]
async def commands():
    client = discord.Client()

    @client.event
    def on_ready():
        print(f'{client.user.name} has connected to Discord!')

    @client.event
    def on_message(msg):
        """takes in user msg, searches for word in that msg"""
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
                response = random.choice(triggers)
                await msg.channel.send(response)


    def contains_word(s, w):
        return (' ' + str(w) + ' ') in (' ' + s + ' ')

    client.run(s.discord_token)

while True:
    asyncio.run(main())
    time.sleep(300)

