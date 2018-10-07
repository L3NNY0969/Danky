import discord
import os
import io
import traceback
import sys
import time
import datetime
import asyncio
import aiohttp
import random
import textwrap
import inspect
from discord.ext import commands
import json
bot = commands.Bot(command_prefix=commands.when_mentioned_or('?'), description="A bot made by TheContryJapan\n\nHelp Commands", owner_id=250346017671741440)


@bot.event
async def on_guild_join(guild):
    lol = bot.get_channel(438526627824271362)
    em = discord.Embed(color=discord.Color(value=0x11f95e))
    em.title = "I have joined new server!"
    em.description = f"Server: {guild}"
    em.set_footer(text=f"ID: {guild.id}")
    em.set_thumbnail(url=guild.icon_url)
    await lol.send(embed=em)
    try:
        await guild.channels[0].send(f"Hello my peeps. Im a discord bot created by TheCountryJapan#1557. Try me out by doing ``+help``!")
    except discord.Forbidden:
        pass

      
@bot.event
async def on_guild_remove(guild):
    lol = bot.get_channel(438526627824271362)
    em = discord.Embed(color=discord.Color(value=0xf44242))
    em.title = "I have left a server."
    em.description = f"Server: {guild}"
    em.set_footer(text=f"ID: {guild.id}")
    await lol.send(embed=em)


@bot.command()
async def invite(ctx):
    """Allow me to join dat server."""
    await ctx.send("b00M! https://discordapp.com/oauth2/authorize?client_id=497244124399796235&scope=bot&permissions=8")                       

    
@bot.command()
async def support(ctx):
    """join my lit support server""" 
    await ctx.send("time to join! https://discord.gg/FEPNu3A")   
    

if not os.environ.get('TOKEN'):
    print("no token m8")
bot.run(os.environ.get('TOKEN').strip('"'))    
