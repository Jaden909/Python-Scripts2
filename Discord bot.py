import os
import asyncio
import discord
streak=0

token='OTYyNzAxMDU4MjIyNzIzMDc1.Gv1zyq.PL7WK_jT9JER8Z7jaQm7W7iKBpH2qhplMhp03o'
CLIENT=discord.Client()
@CLIENT.event
async def on_ready():
    print('Bot has connected to Discord')

    
CLIENT.run(token)
@CLIENT.event
async def on_message(message):
    if message.content =='streak':
        newStreak=streak+1
        response=message.author+'now has a streak of '+newStreak
        print('message')