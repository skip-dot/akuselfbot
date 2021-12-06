# NDE5ODkxNDM0MzEzODc1NDc4.YSeHug.XNkQlSti60YpxK3I6mbfhVmcuSI
import os
import time

print(f"""[-] Creating requirements.txt [selfbot modules]""")
with open("requirements.txt", "w") as f:
    f.write("""wheel
discord.py
colorama
numpy
requests
aiohttp
bs4
pymongo
selenium
pyPrivnote
gtts
dnspython
colored""")
time.sleep(1)
os.system("cls")

print(f"""[-] Installing requirements.txt [selfbot modules]""")
os.system("pip install -r requirements.txt")

time.sleep(1)
os.system("cls")

print(f"""[-]Creating SETUPNEW.py [config setup]""")
with open("SETUPNEW.py", "w") as f:
    f.write('''"""
============================
This text is here to run you through a basic idea of what the setup does.
============================
To put it simply all it requires is your token, this lets the selfbot run
on your account. You can get your own token by following these steps.
============================
[1] Open the discord app
[2] Hold CTRL+SHIFT+I
[3] You should see 2 arrows on the top bar of the dev console [Looks something like >>]
[4] Then follow these steps - 
    Application > Local Storage > https://discord.com > Scroll down and press CTRL+R [Restarts Discord]
[5] Once your discord has loaded back up you can see a string it's completely randomized.
[6] Then to finalize you can paste it into the config.json file.

[KEEP IN MIND THAT THIS WILL NOT WORK ON WEB BROWSER.]
============================
Once you've got your token you can run the setup and it'll run 
you through the config setup.

There's 2 options to this setup, it's pretty simple and more will
get added onto this whenever there's an update to the actual config file.

[1] Default Option -
    As stated, everything in the setup will be set to its default settings.
[2] Custom Option -
    Again, as stated wthis option lets you customise everything to your
    preference.
============================
            [FAQ]
[1] What is a token?
    A token is a form of UID [Unique Identifier] for your discord account however
    it's private, with the token you can get account information such as email,
    password, billing details etc, but it also lets the selfbot log in to your
    account and give you abilities you wouldn't have without it.
[2] Can I get banned for using this?
    To keep it short and simple, yes, selfbots are bannable if you're reported
    by someone.
[3] How can I not get banned?
    Don't be stupid.
[4] Can I sell this?
    I mean, you do you but the source is out there and there's many other sources
    which are better than this one however this one is a bit more up to date than
    some of the older sources on github.
[5] Why did you make this?
    Boredom.
[6] Can I add my own commands to the selfbot?
    If you can code python, sure.
    [-] How can I add my own commands?
        You can copy and paste them from other selfbots, however you need to make
        sure that it's discord.py rewrite, and not an old version of discord.py
        otherwise it won't work.
[7] The selfbot isn't working for me?
    you'll have to wait for a new version to release or use an older version that
    worked for you.
============================
"""

# CODE #
from json import loads, dumps
import json
import os
from pathlib import Path
from colored import fg
import time
from urllib.request import Request, urlopen
# VARIABLES #
PRPL = fg(93)
WHT = fg(15)

PATH = Path("config.json")


# DEFINITIONS #
def cls():
    os.system("cls")

def getHeader(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }
    if token:
        headers.update({"Authorization": token})
    return headers

def getUserData(token):
    try:
        return loads(
            urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getHeader(token))).read().decode())
    except:
        pass

# DELETE OLD SETUP FILE #
OLDSETUP = Path("setup.py")
if not OLDSETUP.exists():
    pass
elif OLDSETUP.exists():
    print(f"""{PRPL}[{WHT}-{PRPL}] {WHT}Deleting setup.py""")
    os.remove("setup.py")
    time.sleep(1)
    print(f"""{PRPL}[{WHT}-{PRPL}] {WHT}setup.py has been deleted successfully.""")
    time.sleep(1)
    cls()
REQFILE = Path("requirements.txt")
if not REQFILE.exists():
    pass
elif REQFILE.exists():
    print(f"""{PRPL}[{WHT}-{PRPL}] {WHT}Deleting requirements.txt""")
    os.remove("requirements.txt")
    time.sleep(1)
    print(f"""{PRPL}[{WHT}-{PRPL}] {WHT}setup.py has been deleted successfully.""")
    time.sleep(1)
    cls()

if PATH.exists():
    CONFIGNEW = input(f"""{PRPL}[{WHT}-{PRPL}] {WHT}"config.json" already exists, would you like to redo it? [Y/N]
    
{PRPL}[{WHT}-{PRPL}] {WHT}""")
    cls()

    if CONFIGNEW == "Y".casefold():
        print(f"""{PRPL}[{WHT}-{PRPL}] {WHT}"config.json" was successfully deleted.""")
        os.remove("config.json")
        time.sleep(1)
        cls()
        print(f"""{PRPL}[{WHT}-{PRPL}] {WHT}To redo your config you have to relaunch setup.py.""")
        print(f"""{PRPL}[{WHT}-{PRPL}] {WHT}This program will close in 3 seconds.""")
        time.sleep(3)
        exit()

    elif CONFIGNEW == "N".casefold():
        print(f"""{PRPL}[{WHT}-{PRPL}] {WHT}This program will close in 3 seconds.""")
        time.sleep(3)
        exit()

else:
    # Creating file since file does not exist.
    print(f"""{PRPL}[{WHT}-{PRPL}] {WHT}Could not find "{WHT}config.json"{WHT}. """)
    time.sleep(.4)
    print(f"""{PRPL}[{WHT}-{PRPL}] {WHT}Creating {PRPL}"{WHT}config.json{PRPL}"{WHT}. """)

    TMPDATA = {}

    with open("config.json", "w") as f:
        json.dump(TMPDATA, f)
    
    time.sleep(.4)
    print(f"""{PRPL}[{WHT}-{PRPL}] {WHT}Successfully created {PRPL}"{WHT}config.json{PRPL}" {WHT}moving on to {PRPL}setup{WHT}. """)
    
    time.sleep(1)
    cls()
    
    with open("config.json", "r") as f:
        json.load(f)

    TKN = input(f"""{PRPL}[{WHT}-{PRPL}] {WHT}Your Token -

{PRPL}[{WHT}1{PRPL}] {WHT}Open the discord app
{PRPL}[{WHT}2{PRPL}] {WHT}Hold CTRL+SHIFT+I
{PRPL}[{WHT}3{PRPL}] {WHT}You should see 2 arrows on the top bar of the dev console {PRPL}[{WHT}Looks something like >>{PRPL}]{WHT}
{PRPL}[{WHT}4{PRPL}] {WHT}Then follow these steps - 
    Application {PRPL}> {WHT}Local Storage {PRPL}> https://discord.com > {WHT}Scroll down and press CTRL+R {PRPL}[{WHT}Restarts Discord{PRPL}]{WHT}
{PRPL}[{WHT}5{PRPL}] {WHT}Once your discord has loaded back up you can see a string it's completely randomized.
{PRPL}[{WHT}6{PRPL}] {WHT}Then to finalize you can paste it into the config.json file.

{PRPL}[{WHT}KEEP IN MIND THAT THIS WILL NOT WORK ON WEB BROWSER.{PRPL}]{WHT}
    
{PRPL}[{WHT}-{PRPL}] {WHT}""")

    cls()

    USERDATA = getUserData(TKN)
    USEREMAIL = USERDATA.get("email")
    print(f"""{PRPL}[{WHT}-{PRPL}] {WHT}Checking if token is working.""")
    TKNCHECK = input(f"""{PRPL}[{WHT}-{PRPL}] {WHT}is this your email? - {USEREMAIL} {PRPL}[{WHT}Y/N{PRPL}]

{PRPL}[{WHT}-{PRPL}] {WHT}""")

    if TKNCHECK == "Y".casefold():
        pass
    else:
        exit()

    cls()
    OPTION = int(input(f"""{PRPL}[{WHT}1{PRPL}] {WHT}Default - Every setting will be set to default, can be edited manually later.
{PRPL}[{WHT}2{PRPL}] {WHT}Custom - Every setting can be set by you, can be edited manually later.

{PRPL}[{WHT}-{PRPL}] {WHT}"""))
    cls()
    if OPTION == 1:
        print(f"""{PRPL}[{WHT}-{PRPL}] {WHT}Settings have been set to default""")
        DATA = {"token":TKN,
                "prefix":">"}

        with open("config.json", "w") as f:
            json.dump(DATA, f)
        time.sleep(2)
        cls()

        print(f"""{PRPL}[{WHT}-{PRPL}] {WHT}The setup is complete, here's your settings.

{PRPL}[{WHT}TOKEN{PRPL}] {WHT}{TKN}
{PRPL}[{WHT}PREFIX{PRPL}] {WHT}>
""")

        input(f"""{PRPL}[{WHT}-{PRPL}] {WHT}PRESS ENTER TO EXIT.""")
        exit()

    elif OPTION == 2:
        print(f"""{PRPL}[{WHT}-{PRPL}] {WHT}Since this selfbot is still being developed, the custom option is very limited,
    however more will be added soon.""")
        time.sleep(2)
        cls()

        PREFIX = input(f"""{PRPL}[{WHT}-{PRPL}] {WHT}What would you like your prefix to be?

{PRPL}[{WHT}-{PRPL}] {WHT}""")

        DATA = {"token":TKN,
                "prefix":PREFIX}

        with open("config.json", "w") as f:
            json.dump(DATA, f)
        
        cls()
        
        print(f"""{PRPL}[{WHT}-{PRPL}] {WHT}The setup is complete, here's your settings.

{PRPL}[{WHT}TOKEN{PRPL}] {WHT}{TKN}
{PRPL}[{WHT}PREFIX{PRPL}] {WHT}{PREFIX}
""")

        input(f"""{PRPL}[{WHT}-{PRPL}] {WHT}PRESS ENTER TO EXIT.""")
        exit()
''')


time.sleep(1)
print(f"""[-] Running SETUPNEW.py""")
time.sleep(1)
os.system("cls")
exec(open("SETUPNEW.py").read())
