#Jayden's Only Friend Python 3.9.5 Bot Version: 1.8
import discord # For discord
from discord.ext import commands, tasks # For discord
from discord.ext.commands import MissingPermissions
from discord_components import *
import os
import random
from discord.voice_client import VoiceClient
import datetime
import asyncio
import json # For interacting with json
from dotenv import load_dotenv
from googleapiclient.discovery import build # For the google command
from PIL import Image
from io import BytesIO
import jishaku
import aiofiles
import time
import datetime
import aiofiles
from pathlib import Path # For paths
import platform # For stats
import logging
from typing import List
from pistonapi import PistonAPI
from urllib.parse import quote_plus
import contextlib

piston = PistonAPI()

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

intents = discord.Intents.all()

client = commands.Bot(command_prefix = commands.when_mentioned_or('$'), intents = intents, case_insensitive = True, owner_id = 667664521577365514)
client.load_extension('jishaku')
client.remove_command("help")

os.chdir("C:\\Users\\jayde\\OneDrive\\Desktop\\Discord Bot")

api_key = "AIzaSyBWCne8MsDmFjOtbItAPZB3BSi3owioX_0"

client.blacklisted_users = []

'''
------------------------------------------------------Important Commands------------------------------------------------------
'''

def read_json(filename):
    with open(f"{cwd}/{filename}.json", "r") as file:
        data = json.load(file)
    return data

def write_json(data, filename):
    with open(f"{cwd}/{filename}.json", "w") as file:
        json.dump(data, file, indent=4)

@client.event
async def on_ready(): 
    change_status.start()
    print(client.user)
    print("----------------I have connected to the server----------------")
    data = read_json("blacklist")
    client.blacklisted_users = data["blacklistedUsers"]
    DiscordComponents(client)

status = ["Vibing to songs", "Eating Rice","Fortnite", "Shooting people", "Sleeping Zzz", "Coding with Jayden", "Thinking about my life", "Watching anime"]

roasts = ["Your face makes onions cry.", "You are as useless as the ueue in queue.", "You are as useless as a white colour pencil.", "You must have born on the highway because thats where most accidents happen.", "If laughter was the best medicine, your face would cure the world.", "Your ass must jealous because of the amount of bullshit that came out of your mouth."]

@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(random.choice(status)))

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return

    if message.author.id in client.blacklisted_users:
        return

    if message.content.startswith("amogus"):
        await message.channel.send("???")

    if message.content.startswith("gayden"):
        await message.channel.send(random.choice(roasts))

    if message.content.startswith("soviet"):
        await message.channel.send('???')

    if message.content.startswith("nazi"):
        await message.channel.send('???')

    await client.process_commands(message)

@client.command()
@commands.is_owner()
@commands.cooldown(1, 3, commands.BucketType.user)
async def blacklist(ctx, user: discord.Member):
    if user == None:
        await ctx.send("You need to mention a user for this to work!")
        return

    if ctx.message.author.id == user.id:
        await ctx.send("Hey, you cannot blacklist yourself????")
        return

    client.blacklisted_users.append(user.id)
    data = read_json("blacklist")
    data["blacklistedUsers"].append(user.id)
    write_json(data, "blacklist")
    await ctx.send(f"Hey, I have blacklisted {user.name} for you.")

@client.command()
@commands.is_owner()
@commands.cooldown(1, 3, commands.BucketType.user)
async def unblacklist(ctx, user: discord.Member):
    client.blacklisted_users.remove(user.id)
    data = read_json("blacklist")
    data["blacklistedUsers"].remove(user.id)
    write_json(data, "blacklist")
    await ctx.send(f"Hey, I have unblacklisted {user.name} for you.")

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def ping(ctx):
    embed = discord.Embed(title="Bot Latency", description=f"Bot Latency: {round(client.latency * 1000)}ms", color=discord.Color.random(), timestamp=ctx.message.created_at)
    embed.add_field("Bot Version: v1.8")
    await ctx.send(embed=embed)

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def dm(ctx, user_id=None, *, args=None):
    if user_id != None and args != None:
        try:
            target = await client.fetch_user(user_id)
            await target.send(args)
            await ctx.channel.send("'" + args + "' sent to: " + target.name)
        except:
            await ctx.channel.send("Couldn't dm the given user.")

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def date(ctx):
    datetoday = datetime.today().strftime('%Y-%m-%d-%H:%M')
    await ctx.send(datetoday)

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def jesus(ctx):
    await ctx.send(file="jesus.png")

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def buddha(ctx):
    await ctx.send(file="buddhist.png")

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def run(ctx, n, *, code):
  nm = n.lower()
  a = code.replace("```", "")

  if nm == "py":
      b = (piston.execute(language="py", version="3.9", code=a))
      c = str(b)
      em = discord.Embed(title="Python Code Output!", 
        description=f'```py\nOutput:\n{c}```',
        color=discord.Color.green())
      
  elif nm == "java":
      b = (piston.execute(language="java", version="15.0.2", code=a))
      c = str(b)
      em = discord.Embed(title="Java Code Output!",
       description=f'```py\nOutput:\n{c}```',
       color=discord.Color.green())
      
  elif nm == "js":
      b = (piston.execute(language="js", version="15.10.0", code=a))
      c = str(b)
      em = discord.Embed(title="JavaScript Code Output!",
       description=f'```py\nOutput:\n{c}```',
       color=discord.Color.green())
      
  elif nm == "go":
      b = (piston.execute(language="go", version="1.16.2", code=a))
      c = str(b)
      em = discord.Embed(title="Go Code Output!",
       description=f'```py\nOutput:\n{c}```',
       color=discord.Color.green())
 
  elif nm == "ts":
      b = (piston.execute(language="typescript", version="4.2.3", code=a))
      c = str(b)
      em = discord.Embed(title="TypeScript Code Output!", 
        description=f'```py\nOutput:\n{c}```',
        color=discord.Color.green())
  else:
      em = discord.Embed(title="Not a supported language!", description = "Please input a supported language!", colour = discord.Colour.red())

  await ctx.send(embed=em)

'''
------------------------------------------------------Button Commands------------------------------------------------------
'''

'''
@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def rps(ctx):
    choices = ["rock","scissors","paper"]
    bot_choice = random.choice(choices)

    start = discord.Embed(title=f"{ctx.author.name}'s Rock Paper Scissors Game", description = "Choose Rock, Paper Or Scissors", color = discord.Colour.blue(), timestamp=ctx.message.created_at)
    
    win = discord.Embed(title="You won!", description = f"We both picked {bot_choice}", color = discord.Colour.green(), timestamp=ctx.message.created_at)
    
    out = discord.Embed(title="You didn't respond in time!", description = "Pick faster next time!", color = discord.Colour.red(), timestamp=ctx.message.created_at)
    
    lose = discord.Embed(title="You lost!", description = f"I picked {bot_choice} L", color = discord.Colour.red(), timestamp=ctx.message.created_at)
    
    tie = discord.Embed(title="We tied!", description = f"We both picked {bot_choice}", color = discord.Colour.gold(), timestamp=ctx.message.created_at)            
    
    m = await ctx.send(embed=start, components=[[Button(style=1, label="Rock"), Button(style=3, label="Paper"), Button(style=ButtonStyle.red, label="Scissors")]])
    def check(res):
        return ctx.author == res.user and res.channel == ctx.channel
    try:
        res = await client.wait_for("button_click", check=check, timeout=20)
        answer = str(res.component.label)
        
        if answer == 'rock':
            if bot_choice == 'rock':
                await m.edit(embed=tie, components=[])
            elif bot_choice == 'paper':
                await m.edit(embed=lose, components=[])
            elif bot_choice == 'scissors':
                await m.edit(embed=win, components=[])

        elif answer == 'paper':
            if bot_choice == 'rock':
                await m.edit(embed=win, components=[])
            elif bot_choice == 'paper':
                await m.edit(embed=tie, components=[])
            elif bot_choice == 'scissors':
                await m.edit(embed=lose, components=[])

        elif answer == 'scissors':
            if bot_choice == 'rock':
                await m.edit(embed=lose, components=[])
            elif bot_choice == 'paper':
                await m.edit(embed=win, components=[])
            elif bot_choice == 'scissors':
                await m.edit(embed=tie, components=[])
        
    except TimeoutError:
        await m.edit(embed=out, components=[])
'''

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def guess(ctx):
    number = random.randint(1, 3)
    start = discord.Embed(title=f"{ctx.author}'s Number Guessing Game!", description="Try to guess the number by clicking on the buttons.", color=discord.Color.blue(), timestamp=ctx.message.created_at)
    
    win = discord.Embed(title=f"{ctx.author}, You Guessed It Right!", description="You won!", color=discord.Color.green(), timestamp=ctx.message.created_at)
    
    out = discord.Embed(title=f"{ctx.author}, You Didn't Respond On Time", description="Timed Out!", color=discord.Color.gold(), timestamp=ctx.message.created_at)
    
    lose = discord.Embed(title=f"{ctx.author}, You Lost!", description=f"The Number Was {number}", color=discord.Color.red(), timestamp=ctx.message.created_at)
  
    m = await ctx.send(embed=start, components=[[Button(style=1, label="1"), Button(style=3, label="2"), Button(style=ButtonStyle.red, label="3")]])

    def check(res):
        return ctx.author == res.user and res.channel == ctx.channel

    try:
        res = await client.wait_for("button_click", check=check, timeout=20)
        if res.component.label == str(number):
            await m.edit(embed=win, components=[])
        else: 
            await m.edit(embed=lose, components=[])
            return

    except asyncio.TimeoutError:
        await m.edit(embed=out, components=[])

def calculate(exp):
    o = exp.replace('??', '*')
    o = o.replace('??', '/')
    result = ''
    try:
        result = str(eval(o))
    except:
        result = 'An error occurred.'
    return result

@client.command(aliases=["calc"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def calculator(ctx):
    buttons = [
    [
        Button(style=ButtonStyle.grey, label='1'),
        Button(style=ButtonStyle.grey, label='2'),
        Button(style=ButtonStyle.grey, label='3'),
        Button(style=ButtonStyle.blue, label='??'),
        Button(style=ButtonStyle.red, label='Exit')
    ],
    [
        Button(style=ButtonStyle.grey, label='4'),
        Button(style=ButtonStyle.grey, label='5'),
        Button(style=ButtonStyle.grey, label='6'),
        Button(style=ButtonStyle.blue, label='??'),
        Button(style=ButtonStyle.red, label='???')
    ],
    [
        Button(style=ButtonStyle.grey, label='7'),
        Button(style=ButtonStyle.grey, label='8'),
        Button(style=ButtonStyle.grey, label='9'),
        Button(style=ButtonStyle.blue, label='+'),
        Button(style=ButtonStyle.red, label='Clear')
    ],
    [
        Button(style=ButtonStyle.grey, label='00'),
        Button(style=ButtonStyle.grey, label='0'),
        Button(style=ButtonStyle.grey, label='.'),
        Button(style=ButtonStyle.blue, label='-'),
        Button(style=ButtonStyle.green, label='=')
    ],
    ]
    m = await ctx.send(content='Loading Calculator...')
    expression = 'None'
    delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
    e = discord.Embed(title=f'{ctx.author.name}\'s calculator | {ctx.author.id}', description=expression,
                        timestamp=delta)
    await m.edit(components=buttons, embed=e)
    while m.created_at < delta:
        res = await client.wait_for('button_click')
        if res.author.id == int(res.message.embeds[0].title.split('|')[1]) and res.message.embeds[
            0].timestamp < delta:
            expression = res.message.embeds[0].description
            if expression == 'None' or expression == 'An error occurred.':
                expression = ''
            if res.component.label == 'Exit':
                await res.respond(content='Calculator Closed', type=7)
                break
            elif res.component.label == '???':
                expression = expression[:-1]
            elif res.component.label == 'Clear':
                expression = 'None'
            elif res.component.label == '=':
                expression = calculate(expression)
            else:
                expression += res.component.label
            f = discord.Embed(title=f'{res.author.name}\'s calculator|{res.author.id}', description=expression,
                                timestamp=delta)
            await res.respond(content='', embed=f, components=buttons, type=7)

@client.command(aliases=["rr"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def rickroll(ctx):
    embed1 = discord.Embed(title=f"Free stuff alert!", description="You should click on a button for free stuff!", color=discord.Color.random(), timestamp=ctx.message.created_at)
    await ctx.send(embed=embed1, components=[Button(style=5, url="https://youtu.be/OyNmzX22DHk", label="Robux"), Button(style=5, url="https://youtu.be/QxXcrTKmEGI", label="Vbucks"), Button(style=5, url="https://youtu.be/dQw4w9WgXcQ", label="Money")])

'''
------------------------------------------------------Beta Commands------------------------------------------------------
'''

@client.command()
async def google(ctx, query: str):
    query = quote_plus(query)
    url = f'https://www.google.com/search?q={query}'
    await ctx.send(f'Google Result for: `{query}` \nLink: {url}')

@client.command()
async def afk(ctx, reason=None):
    if reason == None:
        reason = "AFK"

    with open("afk.json", "r") as f:
        data = json.load(f)

    if str(ctx.author.id) not in data:
        data[ctx.author.id] = reason
        with open("cogs\\afk.json", "w") as f:
            json.dump(data, f, indent=4)
        await ctx.send(f"{ctx.author.mention} I set your AFK: {reason}")
        try:
            await ctx.author.edit(nick=f"[AFK] {ctx.author.name}")
        except discord.Forbidden:
            await ctx.send(f'I do not have permission to change this member\'s nickname. I may not have high enough role hierarchy.')

    else:
        data.pop(str(ctx.author.id))
        with open("cogs\\afk.json", "w") as f:
            json.dump(data, f, indent=4)
        await ctx.send(f"Welcome back {ctx.author.mention}, I removed your AFK")
        try:
            await ctx.author.edit(nick=ctx.author.name)
        except discord.Forbidden:
            await ctx.send(f"I do not have permission to change this member\'s nickname. I may not have high enough role hierarchy.")

'''
------------------------------------------------------Economy Commands------------------------------------------------------
'''

mainshop = [{"name":"Jett Bathwater", "price":69, "description":"Jetts Bath Water"},
            {"name":"Vietnamese Black Coffee", "price":150, "description":"c?? ph?? vi???t nam cao c???p"},
            {"name":"Razer Viper v2", "price":250, "description":"Razer Mouse Go Squeek"},
            {"name":"SteelSeries Apex Pro Keyboard", "price":350, "description":"Pro Gamer Keyboard"},
            {"name":"PewDiePie Gaming Chair", "price":450, "description":"Its Just His Gaming Chair"},
            {"name":"Rolex Watch", "price":500, "description":"Rolex Made In China"},
            {"name":"Asus Laptop", "price":2000, "description":"Decent Laptop"},
            {"name":"Samsung Galaxy Z Flip", "price":3000, "description":"Sam The Egirl"},
            {"name":"Prism Monitor X Ultra", "price":5000, "description":"Gaming Monitor RTX 6090"},
            {"name":"Gold Thophy", "price":99999, "description":"Flex On Em Normies"}]

@client.command(aliases=["bal"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def balance(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author

    await open_account(member)

    users = await get_bank_data()
    user = member
    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    balembed = discord.Embed(title = f"{user.name}'s Balance", color = discord.Colour.random())
    balembed.add_field(name = "Wallet", value = wallet_amt)
    balembed.add_field(name = "Bank", value = bank_amt)

    await ctx.send(embed = balembed)

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()
    user = ctx.author
    earnings = random.randrange(500)

    await ctx.send(f"Someone gave you {earnings} coins!")

    users[str(user.id)]["wallet"] += earnings
    
    with open("bank.json", "w") as f:
            json.dump(users, f, indent=4)

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def withdraw(ctx, amount = None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("Please type the amount of coins to withdraw.")
        return

    bal = await update_bank(ctx.author)

    if amount == "all":
        amount = bal[1]
    elif amount == "max":
        amount = bal[1]

    amount = int(amount)

    if amount < 0:
        await ctx.send("You have to input a number larger than 0.")
        return

    if amount > bal[1]:
        await ctx.send("You don\'t have enough coins.")
        return

    await update_bank(ctx.author, amount, "wallet")
    await update_bank(ctx.author, -1*amount, "bank")

    await ctx.send(f"You withdrew {amount} coins.")

@client.command(aliases = ["dep"])
@commands.cooldown(1, 5, commands.BucketType.user)
async def deposit(ctx, amount = None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("Please type the amount of coins to deposit.")
        return

    bal = await update_bank(ctx.author)

    if amount == "all":
        amount = bal[1]
    elif amount == "max":
        amount = bal[1]

    amount = int(amount)

    if amount < 0:
        await ctx.send("You have to input a number larger than 0.")
        return

    if amount > bal[1]:
        await ctx.send("You don\'t have enough coins.")
        return

    await update_bank(ctx.author, -1*amount, "wallet")
    await update_bank(ctx.author, amount, "bank")

    await ctx.send(f"You deposited {amount} coins.")

@client.command(aliases = ["give"])
@commands.cooldown(1, 5, commands.BucketType.user)
async def send(ctx, member : discord.Member, amount = None):
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        await ctx.send("Please enter the amount you want to give.")
        return

    bal = await update_bank(ctx.author)
    if amount == 'all':
        amount = bal[0]

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You don\'t have enough coins in your wallet.')
        return
    if amount < 0:
        await ctx.send('Amount must be a positive number!')
        return

    await update_bank(ctx.author, -1*amount, 'wallet')
    await update_bank(member, amount, 'wallet')
    await ctx.send(f'{ctx.author.mention} You gave {member} {amount} coins.')

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def slots(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount you want to gamble.")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You don\'t have enough coins.')
        return

    if amount < 0:
        await ctx.send('Amount must be positive number!')
        return

    final = []
    for i in range(3):
        a = random.choice(['????','????','????'])

        final.append(a)

    await ctx.send(str(final))

    if final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
        await update_bank(ctx.author, 1.5*amount)
        winembed = discord.Embed(Title = 'You won!', description = str(final), colour = discord.Colour.random())
        winembed.set_footer(icon_url = ctx.author.avatar_url, text = f"Winner winner")
        await ctx.send(embed = winembed)
    else:
        await update_bank(ctx.author , -1*amount)
        loseembed = discord.Embed(Title = 'You lost!', description = str(final), colour = discord.Colour.random())
        loseembed.set_footer(icon_url = ctx.author.avatar_url, text = f"Loser Loser")
        await ctx.send(embed = loseembed)

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def shop(ctx):
    em = discord.Embed(title = "Shop")

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name = name, value = f"${price} | {desc}")

    await ctx.send(embed = em)

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def buy(ctx, item, amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author, item, amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object Doesn\'t Exist!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
            return

    await ctx.send(f"You just bought {amount} {item}.")

@client.command(aliases = ["inventory"])
@commands.cooldown(1, 5, commands.BucketType.user)
async def inv(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []

    em = discord.Embed(title = f"{ctx.author.name}\'s Inventory")
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name = name, value = amount)    

    await ctx.send(embed = em)

async def buy_this(user, item_name, amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False, 1]

    cost = price * amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0] < cost:
        return [False, 2]

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name, "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name, "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("bank.json", "w") as f:
        json.dump(users, f)

    await update_bank(user, cost*-1, "wallet")

    return [True, "Worked"]

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def sell(ctx, item, amount = 1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author, item, amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have {amount} {item} in your inventory.")
            return
        if res[1]==3:
            await ctx.send(f"You don't have the item in your inventory.")
            return

    await ctx.send(f"You just sold {amount} {item}.")

async def sell_this(user, item_name, amount, price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price == None:
                price = 0.8 * item["price"]
            break

    if name_ == None:
        return [False, 1]

    cost = price * amount

    users = await get_bank_data()

    bal = await update_bank(user)

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False, 2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1 
        if t == None:
            return [False, 3]
    except:
        return [False, 3]    

    with open("bank.json", "w") as f:
        json.dump(users, f)

    await update_bank(user, cost, "wallet")

    return [True, "Worked"]

async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False

    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 2000
    
    with open(f"bank.json", "w") as f:
        json.dump(users, f, indent = 4)
    return True

async def get_bank_data():
    with open("bank.json", "r") as f:
        users = json.load(f)

    return users

async def update_bank(user, change=0, mode="wallet"):
    users = await get_bank_data()
    
    users[str(user.id)][mode] += change

    with open(f"bank.json", "w") as f:
        json.dump(users, f, indent=4)

    bal = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]
    return bal

'''
------------------------------------------------------Owner Only Commands------------------------------------------------------
'''

@client.command()
@commands.is_owner() 
@commands.cooldown(1, 3, commands.BucketType.user)
async def load(ctx, extension):
    if extension == None:
        await ctx.send("You have to input a name of a cog name bro")
        return
    else:
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f"Loaded {extension}")

@client.command()
@commands.is_owner() 
@commands.cooldown(1, 3, commands.BucketType.user)
async def test(ctx):
    await ctx.send("Test")

@client.command()
@commands.is_owner() 
@commands.cooldown(1, 3, commands.BucketType.user)
async def unload(ctx, extension):
    if extension == None:
        await ctx.send("You have to input a cog name bro")
        return
    else:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(f"Unloaded {extension}")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
@commands.is_owner()
@commands.cooldown(1, 3, commands.BucketType.user)
async def botstats(ctx):
    pythonVersion = platform.python_version()
    dpyVersion = discord.__version__
    serverCount = len(client.guilds)
    memberCount = len(set(client.get_all_members()))
    await ctx.send(f"Im in {serverCount} guilds with a total of {memberCount} members.\nIm running Python version {pythonVersion} and discord.py version {dpyVersion}")

@client.command(aliases=['disconnect', 'close', 'stopbot'])
@commands.is_owner()
@commands.cooldown(1, 3, commands.BucketType.user)
async def logout(ctx):
    await ctx.send(f"Hey {ctx.author.mention}, I am now logging out")
    await client.logout()

'''
------------------------------------------------------Image Commands------------------------------------------------------
'''

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def wanted(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    wanted = Image.open("wanted 2.jpg")

    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((252, 252))

    wanted.paste(pfp, (97, 200))

    out = BytesIO()
    wanted.save(out, format='PNG')
    out.seek(0)
    await ctx.send(file=discord.File(out, filename='profile.png'))

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def birthday(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    birthday = Image.open("birthday.png")

    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((114, 114))

    birthday.paste(pfp, (258, 27))

    out = BytesIO()
    birthday.save(out, format='PNG')
    out.seek(0)
    await ctx.send(file=discord.File(out, filename='profile.png'))

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def rip(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    rip = Image.open("rip.jpg")

    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((208, 208))

    rip.paste(pfp, (133, 216))

    out = BytesIO()
    rip.save(out, format='PNG')
    out.seek(0)
    await ctx.send(file=discord.File(out, filename='profile.png'))

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def monke(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    monke = Image.open("monke2.png")

    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((56, 56))

    monke.paste(pfp, (103, 38))

    out = BytesIO()
    monke.save(out, format='PNG')
    out.seek(0)
    await ctx.send(file=discord.File(out, filename='profile.png'))

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def slap(ctx, user: discord.Member = None):
    if user == None:
        await ctx.send("You need to mention a user for this to work!")

    slap = Image.open("slap (2).jpg)")

    asset = ctx.author.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((100, 100))

    asset2 = user.avatar_url_as(size = 128)
    data2 = BytesIO(await asset2.read())
    pfp2 = Image.open(data2)

    pfp2 = pfp2.resize((120, 120))

    slap.paste(pfp, (255, 142))
    slap.paste(pfp2, (972, 215))

    out = BytesIO()
    slap.save(out, format='PNG')
    out.seek(0)
    await ctx.send(file=discord.File(out, filename='profile.png'))

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def stonk(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    stonk = Image.open("stonk.jpg")

    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((103, 103))

    stonk.paste(pfp, (163, 67))

    out = BytesIO()
    stonk.save(out, format='PNG')
    out.seek(0)
    await ctx.send(file=discord.File(out, filename='profile.png'))

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def punch(ctx, user: discord.Member = None):
    if user == None:
        await ctx.send("You need to mention a user for this to work!")

    punch = Image.open("punch.png")

    asset = ctx.author.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((155, 155))

    asset2 = user.avatar_url_as(size = 128)
    data2 = BytesIO(await asset2.read())
    pfp2 = Image.open(data2)

    pfp2 = pfp2.resize((120, 120))

    punch.paste(pfp, (565, 120))
    punch.paste(pfp2, (972, 215))

    out = BytesIO()
    punch.save(out, format='PNG')
    out.seek(0)
    await ctx.send(file=discord.File(out, filename='profile.png'))

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def marry(ctx, user: discord.Member = None):
    if user == None:
        await ctx.send("You need to mention a user for this to work!")

    marry = Image.open("marry.png")

    asset = ctx.author.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((55, 55))

    asset2 = user.avatar_url_as(size = 128)
    data2 = BytesIO(await asset2.read())
    pfp2 = Image.open(data2)

    pfp2 = pfp2.resize((55, 55))

    marry.paste(pfp, (69, 5))
    marry.paste(pfp2, (166, 32))

    out = BytesIO()
    marry.save(out, format='PNG')
    out.seek(0)
    await ctx.send(file=discord.File(out, filename='profile.png'))

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def kill(ctx, user: discord.Member = None):
    if user == None:
        await ctx.send("You need to mention a user for this to work!")

    kill = Image.open("killing (1).jpg")

    asset = ctx.author.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((186, 186))

    asset2 = user.avatar_url_as(size = 128)
    data2 = BytesIO(await asset2.read())
    pfp2 = Image.open(data2)

    pfp2 = pfp2.resize((95, 95))

    kill.paste(pfp, (770, 49))
    kill.paste(pfp2, (211, 318))

    out = BytesIO()
    kill.save(out, format='PNG')
    out.seek(0)
    await ctx.send(file=discord.File(out, filename='profile.png'))

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def googleimg(ctx, *, search):
    ran = random.randint(0, 9)
    resource = build("customsearch", "v1", developerKey=api_key).cse()
    result = resource.list(
        q=f"{search}", cx="72d4af716fd5ef0e7", searchType="image"
    ).execute()
    url = result["items"][ran]["link"]
    embed = discord.Embed(title=f"Here Is Your Image ({search.title()})")
    embed.set_image(url=url)
    await ctx.send(embed=embed)

'''
------------------------------------------------------Tic Tac Toe------------------------------------------------------
'''

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command(aliases=['ttt'])
@commands.cooldown(1, 3, commands.BucketType.user)
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if p1 == None:
        await ctx.send('You need to mention a player')

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the $tictactoe command.")

def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")
    else:
        raise error

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")
    else:
        raise error

'''
------------------------------------------------------Giveaway Commands------------------------------------------------------
'''

def convert(time):
    pos = ["s","m","h","d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]

@client.command(aliases=["gstart"])
@commands.cooldown(1, 10, commands.BucketType.user)
async def giveaway(ctx):
    await ctx.send("Let's start the giveaway! Answer these questions within 20 seconds!")

    questions = ["Which channel should it be hosted in?", 
                "What should be the duration of the giveaway? (s|m|h|d)",
                "What is the prize of the giveaway?"]

    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel 

    for i in questions:
        await ctx.send(i)

        try:
            msg = await client.wait_for('message', timeout=20.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('You didn\'t answer in time, please be quicker next time!')
            return
        else:
            answers.append(msg.content)

    try:
        c_id = int(answers[0][2:-1])
    except:
        await ctx.send(f"You didn't mention a channel properly. Do it like this {ctx.channel.mention} next time.")
        return

    channel = client.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
        await ctx.send(f"You didn't answer the time with a proper unit. Use (s|m|h|d) next time!")
        return
    elif time == -2:
        await ctx.send(f"The time must be an integer. Please enter an integer next time")
        return            

    prize = answers[2]

    await ctx.send(f"The Giveaway will be in {channel.mention} and will last {answers[1]}!")

    embed1 = discord.Embed(title = "Giveaway!", description = f"{prize}", color = discord.Colour.random(), timestamp=ctx.message.created_at)

    embed1.add_field(name = "Hosted by:", value = ctx.author.mention)

    embed1.set_footer(text = f"Ends {answers[1]} from now!")

    my_msg = await channel.send(embed = embed)

    await my_msg.add_reaction("????")

    await asyncio.sleep(time)

    new_msg = await channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    winembed = discord.Embed(title=f"Giveaway for {prize} is over!", description=f"{winner.mention} won the giveaway for {prize}!", color=discord.Color.gold(), timestamp=ctx.message.created_at)

    await my_msg.edit(embed=endembed)

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def reroll(ctx, channel : discord.TextChannel, id_ : int):
    try:
        new_msg = await channel.fetch_message(id_)
    except:
        await ctx.send("The id was entered incorrectly.")
        return
    
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await channel.send(f"Congratulations! The new winner is {winner.mention}!")

'''
------------------------------------------------------Error Handling------------------------------------------------------
'''

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandOnCooldown):  
        return await ctx.send('The command **{}** is still on cooldown for {:.2f}'.format(ctx.command.name, error.retry_after))
    else:
        raise error

@client.event
async def on_command_error(ctx, error):
    ignored = (commands.CommandNotFound)
    if isinstance(error, ignored):
        return

    if isinstance(error, commands.errors.CommandOnCooldown):  
        return await ctx.send('The Command **{}** Is Still On Cooldown For {:.2f} Seconds'.format(ctx.command.name, error.retry_after))

    if isinstance(error, commands.MissingPermissions):
        return await ctx.send('You Don\'t Have Sufficient Permissions To Use This Command.')

    if isinstance(error, commands.BotMissingPermissions):
        return await ctx.send('I Am Missing Some Required Permissions.')

    if isinstance(error, commands.errors.NotOwner):
        return await ctx.send('Only The Bot Owner: J??YD??N#1919 Can Use This Command, Nice Try!')

    if isinstance(error, commands.ExtensionNotFound):
        return await ctx.send('This Cog Was Not Found.')
    else:
        raise error

load_dotenv()
token = os.environ.get("DISCORD_TOKEN") 
client.run(token)