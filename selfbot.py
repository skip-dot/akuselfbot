class SELFBOT():
    __linecount__ = 871
    __version__ = 1.11

import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, asyncio, functools, logging


from discord import CategoryChannel, Colour, Embed, Member, Role, TextChannel, VoiceChannel, utils
from discord.ext import (
    commands,
    tasks
)
from discord.utils import escape_markdown
import json
import os
from colored import fg
import re, requests
from PIL import Image
import datetime
from subprocess import call
import asyncio
from colorama import Fore
from gtts import gTTS
import subprocess
from bs4 import BeautifulSoup
from pathlib import Path
from random import randint
import platform
from os import system
import socket
import colorsys

aku = discord.Client()
aku = commands.Bot(
    command_prefix=">",
    self_bot=True
)
aku.remove_command('help')

with open("config.json", "r") as f:
    config = json.load(f)

embColor = 0x8400FF

def clear():
    os.system("cls")

def printPrimary():
    print("{}╔═════════════╗   ╔═══════════════╗".format(fg(93)))
    print("{}║ Aku {}Selfbot {}║   ║ {}Made By -{} Aku ║".format(fg(93), fg(15), fg(93), fg(15), fg(93)))
    print("{}╚═════════════╝   ╚═══════════════╝{}".format(fg(93), fg(15)))
    print("")

def Init():
    if config.get("token") == "token-here":
        print(fg("red") + "You did not insert your token in the config.json file.", fg(15))
    else:
        token = config.get('token')
        try:
            aku.run(token, bot=False, reconnect=True)
            os.system(f'title (Akus Selfbot) - Version {SELFBOT.__version__}')
        except discord.errors.LoginFailure:
            print("{}= {}TIF23122xe3 - Improper Token was given.".format(fg(93), fg(15)))
            time.sleep(3)
            exit()

@aku.event
async def on_connect():
    printPrimary()

@aku.command()
async def spam(ctx, int:int, *, msg:str):
    await ctx.message.delete()

    for i in range(int):
        await ctx.send(msg)

@aku.command()
async def clear(ctx, amount:int=None):
    await ctx.message.delete()
    try:
        if amount is None:
            await ctx.send("Invalid amount")
        else:
            deleted = await ctx.channel.purge(limit=amount, before=ctx.message, check=is_me)
            embed = discord.Embed(description = f"Deleted {len(deleted)} message(s)", color = embColor)
            embed.set_author(name = "Deleted Messages")
            await ctx.send(embed=embed, delete_after=3)
            await asyncio.sleep(3)

    except:
        try:
            await asyncio.sleep(1)
            c = 0
            async for message in ctx.message.channel.history(limit=amount):
                if message.author == aku.user:
                    c += 1
                    await message.delete()
                else:
                    pass
            embed = discord.Embed(description = f"Deleted {c} message(s)", color = embColor)
            embed.set_author(name = "Deleted Messages")
            await ctx.send(embed=embed, delete_after=3)
        except Exception as e:
            await ctx.send(f"Error: {e}")

@aku.command()
async def swastika(ctx, amount:int, multi:int=None):
    await ctx.message.delete()

    swastikathing = "卐"

    for i in range(amount):
        if multi is None:
            await ctx.send(f"{swastikathing*10}")
        else:
            await ctx.send(f"{swastikathing*multi}")


if __name__ == '__main__':
    Init()