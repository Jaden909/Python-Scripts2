
from asyncio import coroutines
import os
import asyncio
import discord
from asyncio import Task

token='OTYyNzAxMDU4MjIyNzIzMDc1.YlLXOg.97wygTQuPrVgLM6hAnSBWKvhcGg'
streak=0
CLIENT=discord.Client()
@CLIENT.event
async def on_ready():
    print('Bot has connected to Discord')
    
@CLIENT.event
async def on_message():
    global streak
    newStreak=streak+1
    streak=newStreak
    newStreak=str(newStreak)
    response='this server now has a streak of '+newStreak+'!'


CLIENT.run(token)
