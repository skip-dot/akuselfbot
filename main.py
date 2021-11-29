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

# Removing Config - Until further notice
# Info.json package

#Version

#Loads
with open("config.json", "r") as f:
    config = json.load(f)

#GuildID Checker
ids = requests.get('https://gist.github.com/skip-dot/a176d68c2fa03b745f842594e5dd7e22')
soup = BeautifulSoup(ids.text, features="html.parser")
ids1 = soup.find_all("td")
blacklistedIDs = list([i.text for i in ids1])

#Bots

def printPrimary():
    print("{}╔══════════════╗   ╔═══════════════╗".format(fg(160)))
    print("{}║ Riot {}Selfbot {}║   ║ {}Made By -{} nut ║".format(fg(160), fg(15), fg(160), fg(15), fg(160)))
    print("{}╚══════════════╝   ╚═══════════════╝{}".format(fg(160), fg(15)))
    print("")

width = os.get_terminal_size().columns
hwid1 = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

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

def Clear():
    os.system("cls")

def Init():
    if config.get("token") == "token-here":
        print(fg("red") + "You did not insert your token in the config.json file.", fg(15))
        Clear()
    else:
        token = config.get('token')
        try:
            Riot.run(token, bot=False, reconnect=True)
            os.system(f'title (Riot Selfbot) - Version {SELFBOT.__version__}')
        except discord.errors.LoginFailure:
            print("{}= {}TIF23122xe3 - Improper Token was given.".format(fg(160), fg(15)))
            time.sleep(3)
            exit()

Riot = discord.Client()
Riot = commands.Bot(
    command_prefix=">",
    self_bot=True
)
Riot.remove_command('help')

# @Riot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.CommandNotFound):
#         print("{}= {}Command was not found.".format(fg(160), fg(15)))
#         embed = discord.Embed(
#         description = f"{error}",
#         color = 0xf34747
#         )
#         embed.set_author(name = "Command Error - ")
#         await ctx.send(embed=embed, delete_after=15)

@Riot.group(invoke_without_command = True)
async def afk(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color = 0xf34747)
    embed.add_field(name="**AFK Toggle -**", value = "Toggle AFK On and Off")
    embed.set_footer(text = "Riot Selfbot - AFK Mode", icon_url='https://i.imgur.com/EKYJnYj.png')
    await ctx.send(embed=embed)

@afk.command(aliases=["msg"])
async def message(ctx, *, message):
    await ctx.message.delete()
    with open("config.json", "r") as f:
        afkMessage = json.load(f)
        afkMessage["afk_message"] = message
        with open("config.json", "w") as f:
            json.dump(afkMessage, f)

            print(f"{fg(160)}= {fg(15)}Changed AFK message to: {fg(160)}{message}{fg(15)}\n")

@afk.command()
async def toggle(ctx):
    await ctx.message.delete()
    with open("config.json", "r") as f:
        afkStatus = json.load(f)
        afkStatus1 = afkStatus["afk_status"]

    if afkStatus1 == False:
        print(f"{fg(160)}= {fg(15)}Set AFK Status to {fg(160)}True{fg(15)}")
        afkStatus["afk_status"] = True

        embed = discord.Embed(color = 0xf34747)
        embed.set_author(name = "AFK Mode turned On")
        embed.set_footer(text = "Riot Selfbot - AFK Mode", icon_url='https://i.imgur.com/EKYJnYj.png')
        await ctx.send(embed=embed)

    if afkStatus1 == True:
        print(f"{fg(160)}= {fg(15)}Set AFK Status to {fg(160)}False{fg(15)}")
        afkStatus["afk_status"] = False

        embed = discord.Embed(color = 0xf34747)
        embed.set_author(name = "AFK Mode turned Off")
        embed.set_footer(text = "Riot Selfbot - AFK Mode", icon_url='https://i.imgur.com/EKYJnYj.png')
        await ctx.send(embed=embed)

    with open("config.json", "w") as f:
        json.dump(afkStatus, f)

@Riot.event
async def on_connect():
    ctypes.windll.kernel32.SetConsoleTitleW(f'Riot Selfbot - v{SELFBOT.__version__} | Botting')
    with open("config.json", "r") as f:
        afkStat = json.load(f)
        afkStat["afk_status"] = False
        afkStat["region_changer"] = None
        with open("config.json", "w") as f:
            json.dump(afkStat, f)

width = os.get_terminal_size().columns
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

@Riot.command()
async def clear(ctx):
    await ctx.message.delete()
    if str(ctx.guild.id) in blacklistedIDs:
        print(f"{fg(160)}= {ctx.guild.id}{fg(15)} is a blacklisted server\n")

        embed = discord.Embed(description = "This server is blacklisted - You are unable to use any raid commands on these servers", color = 0xf34747)
        embed.set_author(name = "Blacklisted server")
        embed.set_thumbnail(url = "https://i.imgur.com/3yK4NHf.png")
        await ctx.send(embed=embed, delete_after=25)
        pass
    else:
        await ctx.send('ﾠﾠ' + '\n' * 400 + 'ﾠﾠ')
        print(fg(160) + "= " + fg(15) + f"Successfully cleared {ctx.channel}" + fg(15))


@Riot.command()
async def uptime(ctx):
    await ctx.message.delete()
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    await ctx.send(f'`'+uptime+'`')

@Riot.command(aliases=["encrypt"])
async def encode(ctx, *, string):
    await ctx.message.delete()
    decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
    await ctx.send(encoded_stuff)

@Riot.command(aliases=["decrypt"])
async def decode(ctx, *, string):
    await ctx.message.delete()
    strOne = (string).encode("ascii")
    pad = len(strOne)%4
    strOne += b"="*pad
    encoded_stuff = codecs.decode(strOne.strip(),'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
    await ctx.send(decoded_stuff)

@Riot.command()
async def combine(ctx, name1, name2):
    await ctx.message.delete()
    name1letters = name1[:round(len(name1) / 2)]
    name2letters = name2[round(len(name2) / 2):]
    ship = "".join([name1letters, name2letters])
    emb = discord.Embed(description=f"{ship}", color=0xff003c)
    emb.set_author(name=f"{name1} + {name2}")
    await ctx.send(embed=emb)

@Riot.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user.name}'s Dick size", description=f"8{dong}D", colour=0xff003c)
    await ctx.send(embed=em)

@Riot.command(aliases=['changehypesquad', 'chs'])
async def hypesquad(ctx, house):
    await ctx.message.delete()
    request = requests.Session()
    headers = {
      'Authorization': config.get("token"),
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    if house == "bravery":
      payload = {'house_id': 1}
    elif house == "brilliance":
      payload = {'house_id': 2}
    elif house == "balance":
      payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
        print("{}= {}Changed hypesquad to {}{}{}".format(fg(160), fg(15), fg(160), house, fg(15)))
    except Exception as e:
            print(fg("red")+"[ERROR] "+fg("yellow_1")+f"{e}"+fg(15))

@Riot.command()
async def massban(ctx):
    await ctx.message.delete()
    if str(ctx.guild.id) in blacklistedIDs:
        print(f"{fg(160)}= {ctx.guild.id}{fg(15)} is a blacklisted server\n")

        embed = discord.Embed(description = "This server is blacklisted - You are unable to use any raid commands on these servers", color = 0xf34747)
        embed.set_author(name = "Blacklisted server")
        embed.set_thumbnail(url = "https://i.imgur.com/3yK4NHf.png")
        await ctx.send(embed=embed, delete_after=25)
        pass
    else:
        for user in list(ctx.guild.members):
            try:
                await user.ban()
                print("{}= {}Banned all members".format(fg(160), fg(15)))
            except:
                print("{}= {}You don't have the {}Ban {}permission".format(fg(160), fg(15), fg(160), fg(15)))



@Riot.command()
async def masskick(ctx):
    await ctx.message.delete()
    if str(ctx.guild.id) in blacklistedIDs:
        print(f"{fg(160)}= {ctx.guild.id}{fg(15)} is a blacklisted server\n")

        embed = discord.Embed(description = "This server is blacklisted - You are unable to use any raid commands on these servers", color = 0xf34747)
        embed.set_author(name = "Blacklisted server")
        embed.set_thumbnail(url = "https://i.imgur.com/3yK4NHf.png")
        await ctx.send(embed=embed, delete_after=25)
        pass
    else:
        for user in list(ctx.guild.members):
            try:
                await user.kick()
                print("{}= {}Kicked all members".format(fg(160), fg(15)))
            except:
                print("{}= {}You don't have the {}Kick {}permission".format(fg(160), fg(15), fg(160), fg(15)))


@Riot.command()
async def game(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Riot.change_presence(activity=game)

@Riot.command()
async def listening(ctx, *, message):
    await ctx.message.delete()
    await Riot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))

@Riot.command()
async def watching(ctx, *, message):
    await ctx.message.delete()
    await Riot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))

@Riot.command()
async def reverse(ctx, *, message):
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)

@Riot.command(aliases=['clearconsole', 'consoleclear'])
async def cls(ctx):
    await ctx.message.delete()
    Clear()
    printPrimary()

@Riot.command()
async def ascii(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Ascii art is over 2000 characters."+Fore.RESET)
        return
    await ctx.send(f"```{r}```")

@ascii.error
async def ascii_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        emb = discord.Embed(title = "Error -", description = "Missing Required Argument", color = 0xf34747)
        emb.add_field(name = "Command Usage -", value = f"`>ascii [message]`")
        await ctx.send(embed=emb, delete_after=5)

        print("{}= {}Ascii Command was used incorrectly".format(fg(160), fg(15)))

@Riot.command(aliases=["rapeascii"])
async def asciirape(ctx, amount:int, *, text): # b'\xfc'
    await ctx.message.delete()
    if str(ctx.guild.id) in blacklistedIDs:
        print(f"{fg(160)}= {ctx.guild.id}{fg(15)} is a blacklisted server\n")

        embed = discord.Embed(description = "This server is blacklisted - You are unable to use any raid commands on these servers", color = 0xf34747)
        embed.set_author(name = "Blacklisted server")
        embed.set_thumbnail(url = "https://i.imgur.com/3yK4NHf.png")
        await ctx.send(embed=embed, delete_after=25)
        pass
    else:
        r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
        if len('```'+r+'```') > 2000:
            print(f"{fg(160)}= {fg(15)}Ascii art is over 2000 characters.")
            return
        for i in range(amount):
            await ctx.send(f"```{r}```")

@asciirape.error
async def asciirape_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        emb = discord.Embed(title = "Error -", description = "Missing Required Argument", color = 0xf34747)
        emb.add_field(name = "Command Usage -", value = f"`>asciirape <amount= [message]`")
        await ctx.send(embed=emb, delete_after=5)

        print("{}= {}Ascii Rape Command was used incorrectly".format(fg(160), fg(15)))

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

@Riot.command()
async def nitro(ctx):
    await ctx.message.delete()
    await ctx.send(Nitro())

@Riot.command()
async def rapesniper(ctx, amount:int):
    await ctx.message.delete()
    for i in range(amount):
        msg = await ctx.send(Nitro())
        await msg.delete()


@Riot.command()
async def emb(ctx, *, author):
    await ctx.message.delete()
    embed=discord.Embed(color = 0xf34747)
    embed.set_author(name=f"{author}")
    await ctx.send(embed=embed)

@emb.error
async def embed_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        emb = discord.Embed(title = "Error -", description = "Missing Required Argument", color = 0xf34747)
        emb.add_field(name = "Command Usage -", value = f"`>embed [message]`")
        await ctx.send(embed=emb, delete_after=5)

        print("{}= {}Embed Command was used incorrectly".format(fg(160), fg(15)))

@Riot.command()
async def spam(ctx, amount: int, *, message):
        await ctx.message.delete()
        print("{}= {}Spammed {}{}{} times\n".format(fg(160), fg(15), fg(160), amount, fg(15)))

        for _i in range(amount):
            await ctx.send(message)


@Riot.command()
async def smoke(ctx, user:discord.Member, amount: int, *, message):
    await ctx.message.delete()
    if str(ctx.guild.id) in blacklistedIDs:
        print(f"{fg(160)}= {ctx.guild.id}{fg(15)} is a blacklisted server\n")

        embed = discord.Embed(description = "This server is blacklisted - You are unable to use any raid commands on these servers", color = 0xf34747)
        embed.set_author(name = "Blacklisted server")
        embed.set_thumbnail(url = "https://i.imgur.com/3yK4NHf.png")
        await ctx.send(embed=embed, delete_after=25)
        pass
    else:
        print("{}= {}Spammed {}{} {}- {}{} Times\n".format(fg(160), fg(15), fg(160), user, fg(15), fg("green"), amount))
        for _i in range(amount):
            await user.send(message)


def rgb_to_hex(rgb):
    return int('0x%02x%02x%02x' % rgb, 16)

def get_color(hue:int):
    hue = hue/255
    (r, g, b) = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    R, G, B = int(255 * r), int(255 * g), int(255 * b)
    return R, G, B

@Riot.command(aliases=['rainbow-role'])
async def rainbow(ctx, *, role):
    await ctx.message.delete()
    if str(ctx.guild.id) in blacklistedIDs:
        print(f"{fg(160)}= {ctx.guild.id}{fg(15)} is a blacklisted server\n")

        embed = discord.Embed(description = "This server is blacklisted - You are unable to use any raid commands on these servers", color = 0xf34747)
        embed.set_author(name = "Blacklisted server")
        embed.set_thumbnail(url = "https://i.imgur.com/3yK4NHf.png")
        await ctx.send(embed=embed, delete_after=25)
        pass
    else:
        role = discord.utils.get(ctx.guild.roles, name=role)
        while True:
            try:
                for i in range(0, 255, 20):
                    r, g, b = get_color(i)
                    print(r, g, b)

                    await role.edit(role=role, colour=rgb_to_hex((r, g, b)))
                    await asyncio.sleep(10)
            except:
                break

@Riot.command(aliases = ["ddm"])
async def deletedm(ctx, amount: int):
    await ctx.message.delete()
    await asyncio.sleep(0.5)
    # amount += 1
    print("{}= {}Successfully deleted your messages".format(fg(160), fg(15)))
    index = 0
    channel = ctx.channel
    msgs = await channel.history().flatten()
    index2 = 0
    while index != amount:
        index += 1
        msg = msgs[index2-1]

        if msg.author == ctx.author:
            await msg.delete()
        else:
            index -= 1
        index2 += 1

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))

@Riot.command()
async def destroy(ctx):
    await ctx.message.delete()
    if str(ctx.guild.id) in blacklistedIDs:
        print(f"{fg(160)}= {ctx.guild.id}{fg(15)} is a blacklisted server\n")

        embed = discord.Embed(description = "This server is blacklisted - You are unable to use any raid commands on these servers", color = 0xf34747)
        embed.set_author(name = "Blacklisted server")
        embed.set_thumbnail(url = "https://i.imgur.com/3yK4NHf.png")
        await ctx.send(embed=embed, delete_after=25)
        pass
    else:
        print("{}= {}Successfully Destroyed {}{}".format(fg(160), fg(15), fg(160), ctx.guild))
        chans = ctx.guild.channels
        try:
            await chans.delete()
        except:
            pass
        users1 = ctx.guild.members
        try:
            await users1.ban(reason="Rioted bro.")
        except:
            pass
        roles1 = ctx.guild.roles
        try:
            await roles1.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description="lmao boss up",
            reason="boss up",
            icon=None,
            banner=None
        )
    except:
        pass
    await ctx.guild.create_text_channel(name="riot")

    await ctx.guild.create_role(name="riot", color="purple")

    chan = ctx.guild.channels
        
    embed = discord.Embed(title = "Click to join the destruction", url = "https://youtu.be/dQw4w9WgXcQ", color = 0xf34747)
    embed.set_image(url = "https://i.imgur.com/sWZn4Pb.png")
    await chan.send(embed=embed)


@Riot.command()
async def everyone(ctx):
    if str(ctx.guild.id) in blacklistedIDs:
        print(f"{fg(160)}= {ctx.guild.id}{fg(15)} is a blacklisted server\n")

        embed = discord.Embed(description = "This server is blacklisted - You are unable to use any raid commands on these servers", color = 0xf34747)
        embed.set_author(name = "Blacklisted server")
        embed.set_thumbnail(url = "https://i.imgur.com/3yK4NHf.png")
        await ctx.send(embed=embed, delete_after=25)
        pass
    else:
        await ctx.message.delete()
        await ctx.send('https://@everyone@google.com')

@Riot.command()
async def bold(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('**'+message+'**')

@Riot.command()
async def secret(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('||'+message+'||')

@Riot.command()
async def boldita(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(f'***'+message+'***')

@Riot.command()
async def tts(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    buff = await do_tts(message)
    await ctx.send(file=discord.File(buff, f"{message}.wav"))

@Riot.command()
async def dm(ctx, user:discord.Member, *, message):
    await ctx.message.delete()

    await user.send(f"""{message}""")

@dm.error
async def dm_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        emb = discord.Embed(title = "Error -", description = "Missing Required Argument", color = 0xf34747)
        emb.add_field(name = "Command Usage -", value = f"`>dm <@user= [message]`")
        await ctx.send(embed=emb, delete_after=5)

        print("{}= {}DM Command was used incorrectly".format(fg(160), fg(15)))

@Riot.command()
async def annoy(ctx, *, msg):
    await ctx.message.delete()

    msgs = list(msg)

    send = "||||".join(msgs)

    await ctx.send(f"||{send}||")

# @Riot.command(aliases=["bye"])
# async def dm_e(ctx, amount:int, *, msg):
#     await ctx.message.delete()
#     if str(ctx.guild.id) in blacklistedIDs:
#         print(f"{fg(160)}= {ctx.guild.id}{fg(15)} is a blacklisted server\n")

#         embed = discord.Embed(description = "This server is blacklisted - You are unable to use any raid commands on these servers", color = 0xf34747)
#         embed.set_author(name = "Blacklisted server")
#         embed.set_thumbnail(url = "https://i.imgur.com/3yK4NHf.png")
#         await ctx.send(embed=embed, delete_after=25)
#         pass
#     else:
#         print(f"{Fore.GREEN}[GuildSpammer] {Fore.YELLOW}Sent '{msg}' to {len(list(ctx.guild.members))} members {Fore.WHITE} | {Fore.YELLOW}From Guild - {ctx.guild}")
#         print(f"{fg(160)}= {fg(15)}Sent '{msg} to {len(list(ctx.guild.members))}'")
#         for i in range(amount):
#             for mmbr in ctx.guild.members:
#                 try:
#                     await mmbr.send(msg)

#                 except Exception as fuckingnigger:
#                     member.create_dm()
#                     print(fuckingnigger)
#                 await asyncio.sleep(5)

@Riot.command(aliases=["mcname"])
async def checkname(ctx, *, name):
    await ctx.message.delete()
    unav = "Unavailable"
    r = requests.get("https://namemc.com/search?q={}".format(str(name)))
    text = r.text

    print("{}= {}Checked MC User: {}{}{}".format(fg(160), fg(15), fg(160), name, fg(15)))
    if unav in text:
        print("{}= {} {}is not available".format(fg(160), name, fg(15)))

        embed=discord.Embed(title=" ", color=0xf34747)
        embed.set_author(name="MC Name Checker")
        embed.add_field(name="Username -", value="{}".format(name), inline=True)
        embed.add_field(name="Status -", value="{}".format(unav), inline=True)
        embed.add_field(name="Name MC Link -", value="https://namemc.com/search?q={}".format(str(name)), inline=True)
        embed.set_footer(text="Riot Name Checker")
        await ctx.send(embed=embed, delete_after=20)

        print("")
    else:
        print("{}= {} {}is available".format(fg(160), name, fg(15)))
        embed=discord.Embed(title=" ", color=0xf34747)
        embed=discord.Embed(title=" ", color=0xf34747)
        embed.set_author(name="MC Name Checker")
        embed.add_field(name="Username -", value="{}     ".format(name), inline=True)
        embed.add_field(name="Status -", value= "Available     ", inline=True)
        embed.add_field(name="Name MC Link -", value="https://namemc.com/search?q={}".format(str(name)), inline=True)
        embed.set_footer(text="Riot Name Checker")
        await ctx.send(embed=embed, delete_after=20)

        print("")

@Riot.command(aliases=["fag"])
async def faggot(ctx):
    await ctx.message.delete()
    guild = ctx.guild.members

    await ctx.send("lol {} is a faggot".format(random.choice(guild)))

@Riot.command()
async def userinfo(ctx, user: discord.Member):
    await ctx.message.delete()

    joined = user.created_at
    joinedFormat = joined.strftime("%x %X")

    joinguild = user.joined_at
    joinguildFormat = joinguild.strftime("%x %X")

    rolelist = ""
    for role in user.roles:
        if role.name != "@everyone":
            rolelist += f"{role.mention} "
    custom_status = ''
    if user.activity is not None:
        custom_status = f'\nStatus: {user.activity}'
        
    name = str(user)
    if user.nick:
        name = f"{user.nick} ({name})"

    embed = discord.Embed(title=name, color = 0xf34747)
    embed.set_thumbnail(url=user.avatar_url)

    embed.add_field(name="**User information**", value=f"Created: {joinedFormat}\nProfile: {user.mention}\nID: {user.id}{custom_status}", inline=False)
    embed.add_field(name="**Member Information**", value=f"Joined: {joinguildFormat}\nRoles: {rolelist}", inline=False)
    embed.set_footer(text= "Riot Selfbot | Userinfo", icon_url = "https://i.imgur.com/EKYJnYj.png")
    await ctx.send(embed=embed, delete_after=20)

@Riot.group(invoke_without_command=True)
async def help(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=" ", description="Riot Selfbot - Help Command", color = 0xf34747)
    embed.set_author(name="Help Command")
    embed.add_field(name="**Clear -**", value="Sends a large message which makes the channel look purged", inline=False)
    embed.add_field(name="**Uptime -**", value="Shows you how long you have had the selfbot open", inline=False)
    embed.add_field(name="**Encode/Decode -**", value="You can encode a message or decode it", inline=False)
    embed.add_field(name="**Combine -**", value="Combine 2 names together", inline=False)
    embed.add_field(name="**Dick -** ", value="Shows how large your cock is", inline=False)
    embed.add_field(name="**Hypesquad -**", value="Change your hypesquad [Bravery/Brilliance/Balance/Random]", inline=True)
    embed.set_footer(text="Page 1 of 7", icon_url = "https://i.imgur.com/EKYJnYj.png")
    await ctx.send(embed=embed, delete_after= 30)

@help.command(aliases = ["2"])
async def _2(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=" ", description="Riot Selfbot - Help Command", color = 0xf34747)
    embed.set_author(name="Help Command")
    embed.add_field(name="**Mass Ban/Kick -**", value="Kicks/Bans a whole server [Requires Permissions]", inline=False)
    embed.add_field(name="**Game - **", value="Changes your playing state", inline=False)
    embed.add_field(name="**Listening -**", value="Changes your listening state", inline=False)
    embed.add_field(name="**Watching -**", value="Changes your watching state", inline=False)
    embed.add_field(name="**Reverse -** ", value="Reverses your previous message", inline=False)
    embed.add_field(name="CLS -", value="Clears your console", inline=True)
    embed.set_footer(text="Page 2 of 7", icon_url = "https://i.imgur.com/EKYJnYj.png")
    await ctx.send(embed=embed, delete_after= 30)

@help.command(aliases = ["3"])
async def _3(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=" ", description="Riot Selfbot - Help Command", color = 0xf34747)
    embed.set_author(name="Help Command")
    embed.add_field(name="**Ascii -**", value="Creates an Ascii Art message", inline=False)
    embed.add_field(name="**Ascii Rape  - **", value="Spams an message as Ascii Art", inline=False)
    embed.add_field(name="**Nitro -**", value="Sends a fake nitro code", inline=False)
    embed.add_field(name="**Emb -**", value="Sends an embedded message", inline=False)
    embed.add_field(name="**Spam - **", value="Spams an [int] amount of messages", inline=False)
    embed.add_field(name="**Smoke -**", value="Spams a certain user", inline=True)
    embed.set_footer(text="Page 3 of 7", icon_url = "https://i.imgur.com/EKYJnYj.png")
    await ctx.send(embed=embed, delete_after= 30)

@help.command(aliases = ["4"])
async def _4(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=" ", description="Riot Selfbot - Help Command", color = 0xf34747)
    embed.set_author(name="Help Command")
    embed.add_field(name="**Rainbow -**", value="Sets a role to rainbow [Role has to be typed exactly]", inline=False)
    embed.add_field(name="**DDM  - **", value="Deletes an [int] amount of your messages", inline=False)
    embed.add_field(name="**Destroy -**", value="Destroys a server, replacing all channels and roles with RiotSelfbot", inline=False)
    embed.add_field(name="**Everyone -**", value="Masks an @everyone mention [Must have permissions]", inline=False)
    embed.add_field(name="**TTS - **", value="Sends a TTS message as a `.wav` file", inline=False)
    embed.add_field(name="**DM -**", value="Send a private message to a user", inline=True)
    embed.set_footer(text="Page 4 of 7", icon_url = "https://i.imgur.com/EKYJnYj.png")
    await ctx.send(embed=embed, delete_after= 30)

@help.command(aliases = ["5"])
async def _5(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=" ", description="Riot Selfbot - Help Command", color = 0xf34747)
    embed.set_author(name="Help Command")
    embed.add_field(name="**Annoy -**", value="Send a mass spoiler message", inline=False)
    embed.add_field(name="**Bye  - **", value="Messages an entire guild", inline=False)
    embed.add_field(name="**MCName -**", value="Checks whether a minecraft name is available", inline=False)
    embed.add_field(name="**Faggot -**", value="Who is the faggot in the server?", inline=False)
    embed.add_field(name="**Userinfo -** ", value="Shows you information about a user", inline=False)
    embed.add_field(name="**Help -**", value="Shows this message", inline=True)
    embed.set_footer(text="Page 5 of 7", icon_url = "https://i.imgur.com/EKYJnYj.png")
    await ctx.send(embed=embed, delete_after= 30)

@help.command(aliases = ["6"])
async def _6(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=" ", description="Riot Selfbot - Help Command", color = 0xf34747)
    embed.set_author(name="Help Command")
    embed.add_field(name="**Ghost -**", value="Spams a user's @ and deletes it", inline=False)
    embed.add_field(name="**PFPSteal -** ", value="Steal any user's profile picture", inline=False)
    embed.add_field(name="**Changelog -**", value="Shows you what has been added to the selfbot", inline=False)
    embed.add_field(name="**Count -**", value="Counts to whichever number you set - `count <number>`", inline=False)
    embed.add_field(name="**Create Channel/Role/Category**", value="Lets you create channels, roles or categories with ease - `create <type> [name]` - role color must be set manually", inline=False)
    embed.add_field(name="**Copy [ID]**", value="Copy a server you're in from its ID", inline=False)
    embed.set_footer(text="Page 6 of 7", icon_url = "https://i.imgur.com/EKYJnYj.png")
    await ctx.send(embed=embed, delete_after= 30)

@help.command(aliases = ["7"])
async def _7(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=" ", description="Riot Selfbot - Help Command", color = 0xf34747)
    embed.set_author(name="Help Command")
    embed.add_field(name="**Crashcalls Start/Stop -**", value="Crashes a discord call [Permissions Required]", inline=False)
    embed.add_field(name="**Joke -** ", value="Sends a random joke", inline=False)
    embed.add_field(name="**Countdown -**", value="Counts down from whichever number you enter", inline=False)
    embed.add_field(name="**DeleteG -**", value="Deletes a guild with ease [Must be the owner]", inline=False)
    embed.add_field(name="**AFK Toggle -**", value="Toggles on and off your AFK Status", inline=False)
    embed.add_field(name="**Ping -**", value="Pings a user and shows how long it took them to reply - `ping <@user>`", inline=False)
    embed.set_footer(text="Page 7 of 7", icon_url = "https://i.imgur.com/EKYJnYj.png")
    await ctx.send(embed=embed, delete_after= 30)

@Riot.command(aliases=['pfpget', 'stealpfp'])
async def pfpsteal(ctx, user: discord.Member):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print("{}= {}You did not insert your password in the config.".format(fg(160), fg(15)))
    else:
        password = config.get('password')
        with open(f'Images/{user.name}.png', 'wb') as f:
          r = requests.get(user.avatar_url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)

@Riot.command()
async def ghost(ctx, amount:int, user: discord.Member):
    await ctx.message.delete()
    if str(ctx.guild.id) in blacklistedIDs:
        print(f"{fg(160)}= {ctx.guild.id}{fg(15)} is a blacklisted server\n")

        embed = discord.Embed(description = "This server is blacklisted - You are unable to use any raid commands on these servers", color = 0xf34747)
        embed.set_author(name = "Blacklisted server")
        embed.set_thumbnail(url = "https://i.imgur.com/3yK4NHf.png")
        await ctx.send(embed=embed, delete_after=25)
        pass
    else:
        for i in range(amount):
            message = await ctx.send(user.mention)
            await message.delete()
            await asyncio.sleep(.5)

@ghost.error
async def ghost_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.delete()
        embed = discord.Embed(description = f"{error}",color = 0xf34747)
        embed.set_author(name = "Error has occured -")
        embed.add_field(name = "**Command Usage -**", value = "ghost [amount] <user>")
        await ctx.send(embed=embed, delete_after=10)


@Riot.command()
async def changelog(ctx):
    await ctx.message.delete()

    embed = discord.Embed(title= " ", description = "Changelog V1.11", color = 0xf34747)
    embed.set_author(name = "V1.11 Changelog -")
    embed.add_field(name = "**New Commands -**", value = f"Create Channels/Role/Category, Copy Server, Crash call, Delete Guild, AFK, Countdown", inline=False)

    embed.set_footer(text = f"Riot Changelog | Requested by {ctx.author.name}", icon_url = "https://i.imgur.com/EKYJnYj.png")

    print("{}= V1.11 {}Changelog -".format(fg(160), fg(15)))
    print("{}= 6 {}New Commands".format(fg(160), fg(15)))
    print("{}= {}No changes made to the actual bot".format(fg(160), fg(15)))
    print("{}= {}Added blacklisting system".format(fg(160), fg(15)))
    print("")

    await ctx.send(embed=embed, delete_after = 25)

@Riot.command()
async def count(ctx, seconds:int):
    await ctx.message.delete()
    print("{}= {}Counting to {}{}{}".format(fg(160), fg(15), fg(160), seconds, fg(15)))

    for i in range(1, seconds + 1):
        await ctx.send(i)

        await asyncio.sleep(1)

    print("{}= {}Finished counting to {}{}{}".format(fg(160), fg(15), fg(160), seconds, fg(15)))

@Riot.command()
async def sendchans(ctx, *, msg):
    await ctx.message.delete()
    if str(ctx.guild.id) in blacklistedIDs:
        print(f"{fg(160)}= {ctx.guild.id}{fg(15)} is a blacklisted server\n")

        embed = discord.Embed(description = "This server is blacklisted - You are unable to use any raid commands on these servers", color = 0xf34747)
        embed.set_author(name = "Blacklisted server")
        embed.set_thumbnail(url = "https://i.imgur.com/3yK4NHf.png")
        await ctx.send(embed=embed, delete_after=25)
        pass
    else:
        channels = ctx.guild.channels
        random.shuffle(channels)
        for i in channels:
            await i.send(msg)

@Riot.group(invoke_without_command=True)
async def create(ctx):
    await ctx.message.delete()
    embed=discord.Embed(color = 0xf34747)
    embed.set_author(name = "Create Commands -")
    embed.add_field(name = "**Channel -**", value = "Create a channel - `create channel [name]`", inline=False)
    embed.add_field(name = "**Role -**", value = "Create a role - `create role [name]`", inline=False)
    embed.add_field(name = "**Category -**", value = "Create a category - `create category [name]`", inline=False)
    embed.set_thumbnail(url = "https://i.imgur.com/3yK4NHf.png")
    await ctx.send(embed=embed, delete_after=30)

@create.command()
async def channel(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.create_text_channel(name = name)
    print(f"{fg(160)}= {fg(15)}Created new channel: {fg(160)}{name}{fg(15)}\n")

@create.command()
async def role(ctx, color:discord.Color, *, name):
    await ctx.message.delete()

    await ctx.guild.create_role(name=name, color = color)
    print(f"{fg(160)}= {fg(15)}Created create role: {fg(160)}{name}{fg(15)}\n")

@create.command()
async def category(ctx, *, name):
    await ctx.guild.create_category(name = name)
    print(f"{fg(160)}= {fg(15)}Created create category: {fg(160)}{name}{fg(15)}\n")

@Riot.command()
async def copy(ctx, guildID:int):
    guild = Riot.get_guild(guildID)
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


    print(f"{fg(160)}= {fg(15)}Started copying {fg(160)}{guildID}{fg(15)}")
    for role in ctx.guild.roles:
        try:
            await role.delete(reason = "Riot - Server Paste")
        except:
            pass
    for role in roles[::-1]:
        if role.name != "@everyone":
            await ctx.guild.create_role(name = role.name, color = role.color, permissions = role.permissions, mentionable = role.mentionable, reason = "Riot - Server Paste", hoist = role.hoist)

    for channel in ctx.guild.channels:
        await channel.delete(reason = "Riot - Server Paste")

    for category in categories:

        channels = category.text_channels
        newCat = await ctx.guild.create_category_channel(name = category.name, overwrites = getOverwrites(channel), reason = "Riot - Server Paste")

        for channel in channels:

            await ctx.guild.create_text_channel(name = channel.name, overwrites = getOverwrites(channel), category = newCat, reason = "Riot - Server Paste", topic = channel.topic, slowmode_delay = channel.slowmode_delay, nsfw = channel.nsfw)

        channels = category.voice_channels
        for channel in channels:

            await ctx.guild.create_voice_channel(name = channel.name, overwrites = getOverwrites(channel), category = newCat, reason = "Riot - Server Paste", bitrate = channel.bitrate, user_limit = channel.user_limit)

    channels = guild.text_channels
    for channel in channels:
        if channel.category is None:

            await ctx.guild.create_text_channel(name = channel.name, overwrites = getOverwrites(channel), category = None, reason = "Riot - Server Paste", topic = channel.topic, slowmode_delay = channel.slowmode_delay, nsfw = channel.nsfw)

    channels = guild.voice_channels
    for channel in channels:
        if channel.category is None:

            await ctx.guild.create_voice_channel(name = channel.name, overwrites = getOverwrites(channel), category = None, reason = "Riot Server Backup", bitrate = channel.bitrate, user_limit = channel.user_limit)
    print(f"{fg(160)}= {fg(15)}Finished copying {fg(160)}{guildID}{fg(15)}")

@Riot.command()
async def joke(ctx):
    await ctx.message.delete()
    headers = {'Accept': 'application/json'}
    r = requests.get('https://icanhazdadjoke.com', headers=headers).json()
    jokeEmb = Embed(title='__**Joke**__', description=(f"{r['joke']}"), color=0xf34747)
    jokeEmb.set_footer(text='Riot Selfbot', icon_url='https://i.imgur.com/EKYJnYj.png')
    joke_sent = await ctx.send(embed=jokeEmb)
    await asyncio.sleep(30)
    await joke_sent.delete()

@Riot.command()
async def countdown(ctx, timeframe: int):
    await ctx.message.delete()
    print(f"{fg(160)}= {fg(15)}Started countdown for {fg(160)}{timeframe}{fg(15)} seconds")
    endEmb = Embed(title='**Countdown Started**', description=f"Time: {timeframe}s", color=0xf34747)
    endEmb.set_footer(text='Riot Selfbot', icon_url='https://i.imgur.com/EKYJnYj.png')
    countItDown = await ctx.send(embed=endEmb)
    for i in range(timeframe, -1, -1):
        endEmb = Embed(title='**Countdown Started**', description=f"Time: {i}s", color=0xf34747)
        endEmb.set_footer(text='Riot Selfbot', icon_url='https://i.imgur.com/EKYJnYj.png')
        await countItDown.edit(embed=endEmb)
        await asyncio.sleep(1)

    endEmb = Embed(title='**Countdown Finished**', description=f"Timer Has Ended", color=0xf34747)
    endEmb.set_footer(text=f'Riot Selfbot | {timeframe} seconds', icon_url='https://i.imgur.com/EKYJnYj.png')


    await countItDown.edit(embed=endEmb, delete_after=20)
    print(f"{fg(160)}= {fg(15)}Countdown for {fg(160)}{timeframe}{fg(15)} seconds has ended\n")



@countdown.error
async def countdown_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.delete()
        invalidus = Embed(title='Invalid usage', color=0xf34747)
        invalidus.add_field(name='Valid usage', value='`countdown (time in seconds)``')
        invalidusmsg = await ctx.send(embed=invalidus)
        await asyncio.sleep(5)
        await invalidusmsg.delete()

@Riot.command()
async def deleteg(ctx):
    await ctx.message.delete()
    try:
        await ctx.guild.delete()
        print(f"{fg(160)}= {fg(15)}Deleted {fg(160)}{ctx.guild.name}{fg(15)}")
    except Forbidden:
        print(f"{fg(160)}= {fg(15)}Could not delete guild due to you not being the Guild Owner")

@Riot.command()
async def ping(ctx, user:discord.Member):
    await ctx.message.delete()
    now = time.time()
    ping = await ctx.send(user.mention)
    channelID = ctx.channel.id
    def checkResponse(m):
        return m.channel.id == channelID and m.author == user

    message = await Riot.wait_for('message', check=checkResponse)
    end = time.time() - now
    timeEmb = discord.Embed(description = f"`1` packet transmitted, `1` received, `0%` packet loss, time `{round(end*1000, 5)}ms`", color=0xf34747)
    timeEmb.set_author(name=f"--- {user.display_name} ping statistics --- ")
    timeEmb.set_footer(text = "Riot Selfbot", icon_url = "https://i.imgur.com/EKYJnYj.png")

    await ctx.send(embed=timeEmb, delete_after=20)

# @Riot.command()
# async def log(ctx, limit:int, fileName):
#     await ctx.message.delete()
#     with open(fileName, "w") as logFile:
#         msgHistory = await ctx.channel.history(limit=limit).flatten()
#         print(msgHistory)
#         logFile.write("\n".join([msg.content for msg in msgHistory]))
#
#
#     print(f"{fg(160)}= {fg(15)}Saved {fg(160)}{limit}{fg(15)} messages")

if __name__ == '__main__':
    Init()