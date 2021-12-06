class SELFBOT():
    __linecount__ = 871
    __version__ = 1.11

import discord, time, os, io
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, asyncio, functools, logging


from discord import CategoryChannel, Colour, Embed, Member, Role, TextChannel, VoiceChannel, utils
from discord.ext import (
    commands,
    tasks
)
from discord.utils import escape_markdown, get
import json
import os
from colored import fg
import re, requests
from PIL import Image
from mojang import MojangAPI
import datetime
import asyncio
from gtts import gTTS
import subprocess
from bs4 import BeautifulSoup
from pathlib import Path
from random import randint
from os import system


with open("config.json", "r") as f:
    prfx = json.load(f)

getPrfx = prfx.get("prefix")

aku = discord.Client()
aku = commands.Bot(
    command_prefix=getPrfx,
    self_bot=True
)
aku.remove_command('help')

with open("config.json", "r") as f:
    config = json.load(f)

embColor = 0x8400FF
loop = asyncio.get_event_loop()


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

            ### PRINT ###
            print(f"{fg(93)}[{fg(15)}-{fg(93)}] {fg(15)}Deleted {fg(93)}{len(deleted)} {fg(15)}message{fg(93)}({fg(15)}s{fg(93)})")

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

            ### PRINT ###
            print(f"{fg(93)}[{fg(15)}-{fg(93)}] {fg(15)}Deleted {fg(93)}{c} {fg(15)}message{fg(93)}({fg(15)}s{fg(93)})")

        except Exception as e:
            await ctx.send(f"Error: {e}")

@aku.command(aliases=['pfpget', 'stealpfp'])
async def pfpsteal(ctx, user: discord.Member):
    await ctx.message.delete()

    with open(f'Images/{user.name}.png', 'wb') as f:
        r = requests.get(user.avatar_url, stream=True)
        for block in r.iter_content(1024):
            if not block:
                break
            f.write(block)

def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)
        return inner
    return outer

@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang="en")
    tts.write_to_fp(f)
    f.seek(0)
    return f

@aku.command()
async def tts(ctx, *, message):
    await ctx.message.delete()
    buff = await do_tts(message)
    await ctx.send(file=discord.File(buff, f"{message}.mp3"))

@aku.command()
async def ping(ctx, user:discord.Member):
    await ctx.message.delete()
    now = time.time()
    ping = await ctx.send(user.mention)
    channelID = ctx.channel.id
    def checkResponse(m):
        return m.channel.id == channelID and m.author == user

    message = await aku.wait_for('message', check=checkResponse)
    end = time.time() - now
    timeEmb = discord.Embed(description = f"`1` packet transmitted, `1` received, `0%` packet loss, time `{round(end*1000, 5)}ms`", color=embColor)
    timeEmb.set_author(name=f"--- {user.display_name} ping statistics --- ")

    await ctx.send(embed=timeEmb, delete_after=20)

@aku.command()
async def anilist(ctx):
    emb = discord.Embed(color = embColor)
    emb.set_author(name="AniList", url="https://anilist.co/user/aaakumaaa", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb, delete_after=30)

@aku.command()
async def sauce(ctx, hentai:int, img:bool=None):
    await ctx.message.delete()
    req = requests.get(f"https://nhentai.net/g/{hentai}")
    soup = BeautifulSoup(req.content, "html.parser")

    getError = soup.find('p').get_text()

    if getError == "Looks like what you're looking for isn't here.":
        embed = discord.Embed(color = embColor)
        embed.set_author(name=f"Sauce doesn't exist.", icon_url=ctx.author.avatar_url)
        embed.set_footer(text = f"nhentai.net/g/{hentai} - aku spent too long on this", icon_url="https://i.imgur.com/uLAimaY.png")
        await ctx.send(embed=embed, delete_after=30)
        
    else:
        midTitle = soup.find('span', class_="pretty").get_text()
        beforeTitle = soup.find('span', class_="before").get_text()
        afterTitle = soup.find('span', class_="after").get_text()

        thumbnail = soup.find_all('img', class_="lazyload")
        
        uploadTime = soup.find('time', class_="nobold").get_text()
        if img is False:
            embed = discord.Embed(description = f"Uploaded - {uploadTime}", color = embColor)
            embed.set_author(name=f"{beforeTitle}{midTitle}{afterTitle}", url=f"https://nhentai.net/g/{hentai}", icon_url=ctx.author.avatar_url)
            embed.set_footer(text = f"nhentai.net/g/{hentai} - aku spent too long on this", icon_url="https://i.imgur.com/uLAimaY.png")
            await ctx.send(embed=embed, delete_after=30)
        elif img is None or True:
            embed = discord.Embed(description = f"Uploaded - {uploadTime}", color = embColor)
            embed.set_author(name=f"{beforeTitle}{midTitle}{afterTitle}", url=f"https://nhentai.net/g/{hentai}", icon_url=ctx.author.avatar_url)
            embed.set_image(url=thumbnail[0].find("img")["src"])
            embed.set_footer(text = f"nhentai.net/g/{hentai} - aku spent too long on this", icon_url="https://i.imgur.com/uLAimaY.png")
            await ctx.send(embed=embed, delete_after=30)

@aku.command()
async def copy(ctx, guildID:int):
    guild = aku.get_guild(guildID)
    categories = guild.categories
    roles = guild.roles

    def getOverwrites(channel):
        overwrite = {}

        for role, perm in channel.overwrites.items():
            roleName = role.name
            roleObj = discord.utils.get(ctx.guild.roles, name = roleName)
            if roleObj is not None:
                overwrite[roleObj] = perm
            return overwrite

    for role in ctx.guild.roles:
        try:
            await role.delete(reason = "Aku's handy dandy server copy machine")
        except:
            pass
    for role in roles[::-1]:
        if role.name != "@everyone":
            await ctx.guild.create_role(name = role.name, color = role.color, permissions = role.permissions, mentionable = role.mentionable, reason = "Aku's handy dandy server copy machine", hoist = role.hoist)

    for channel in ctx.guild.channels:
        await channel.delete(reason = "Aku's handy dandy server copy machine")

    for category in categories:

        channels = category.text_channels
        newCat = await ctx.guild.create_category_channel(name = category.name, overwrites = getOverwrites(channel), reason = "Aku's handy dandy server copy machine")

        for channel in channels:

            await ctx.guild.create_text_channel(name = channel.name, overwrites = getOverwrites(channel), category = newCat, reason = "Aku's handy dandy server copy machine", topic = channel.topic, slowmode_delay = channel.slowmode_delay, nsfw = channel.nsfw)

        channels = category.voice_channels
        for channel in channels:

            await ctx.guild.create_voice_channel(name = channel.name, overwrites = getOverwrites(channel), category = newCat, reason = "Aku's handy dandy server copy machine", bitrate = 64000, user_limit = channel.user_limit)

    channels = guild.text_channels
    for channel in channels:
        if channel.category is None:

            await ctx.guild.create_text_channel(name = channel.name, overwrites = getOverwrites(channel), category = None, reason = "Aku's handy dandy server copy machine", topic = channel.topic, slowmode_delay = channel.slowmode_delay, nsfw = channel.nsfw)

    channels = guild.voice_channels
    for channel in channels:
        if channel.category is None:

            await ctx.guild.create_voice_channel(name = channel.name, overwrites = getOverwrites(channel), category = None, reason = "Aku's handy dandy server copy machine", bitrate = 64000, user_limit = channel.user_limit)
    print(f"{fg(93)}[{fg(15)}-{fg(93)}] {fg(15)}Finished copying {fg(93)}{guildID}{fg(15)}")

@aku.group()
async def player(invoke_without_command = True):
    print("hypixel stuff")

@player.command()
async def bedwars(ctx, user:str):
    ### UUID STUFF ###
    uuid = MojangAPI.get_uuid(user)
    url = f"https://api.hypixel.net/player?key=734032f9-e6a5-4203-bdf1-5c75a961b1ee&uuid={uuid}"
    req = requests.get(url).json()
    ######

    ### EXTRA STUFF ###
    avurl = f"https://mc-heads.net/avatar/{uuid}"
    namemc = f"https://namemc.com/search?q={user}"
    await ctx.message.delete()
    ######

    ### REQUESTS ###
    totalGames = req["player"]["stats"]["Bedwars"]["games_played_bedwars_1"]
    totalDeaths = req["player"]["stats"]["Bedwars"]["deaths_bedwars"]
    winstreak = req["player"]["stats"]["Bedwars"]["winstreak"]
    lostGames = req["player"]["stats"]["Bedwars"]["losses_bedwars"]
    winGames = req["player"]["stats"]["Bedwars"]["wins_bedwars"]
    bwCoins = req["player"]["stats"]["Bedwars"]["coins"]
    totalKills = req["player"]["stats"]["Bedwars"]["kills_bedwars"]
    finalKills = req["player"]["stats"]["Bedwars"]["final_kills_bedwars"]
    finalDeaths = req["player"]["stats"]["Bedwars"]["final_deaths_bedwars"]

    bwStars = req["player"]["achievements"]["bedwars_level"]

    username = req["player"]["displayname"]

    winLoss = winGames/lostGames
    fkdr = finalKills/finalDeaths
    ######

    ### EMBEDS ###
    em = discord.Embed(color=embColor)
    em.set_author(name=f"[{bwStars}*] {username}", url=namemc, icon_url=ctx.author.avatar_url)
    em.set_thumbnail(url=avurl)
    
    em.add_field(name = "Bedwars Stats", value=f"""**W/L Ratio -** `{round(winLoss, 2)}`
    **FKDR -** `{round(fkdr, 2)}`
    **Games Played -** `{totalGames}`
    **Total Deaths -** `{totalDeaths}`
    **Total Kills -** `{totalKills}`
    **Games Lost -** `{lostGames}`
    **Games Won -** `{winGames}`
    
    **Coins -** `{bwCoins}`
    **Winstreak -** `{winstreak}`
    """)

    em.set_footer(text = "Overall Bedwars Stats", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=em)
    ######



if __name__ == '__main__':
    Init()
