
#imports
import discord
from discord.ext import commands
from random import *
import random as rnd
from time import sleep
from webserver import keep_alive
import os
from tekst import *
import youtube_dl
from quotes import *
import time
import asyncio
import requests
from dotenv import load_dotenv
import utilities
import responses1
import openai

#prefix for commands in the discord chat
bot = commands.Bot(command_prefix=".")

#Add tokens and keys
openai.api_key = "insert your open ai api key here"
hemmeligkode = "insert you discord token here"
      

@bot.command()
async def databrus(ctx):
  await ctx.reply("Forskning viser at voldsomme mengder databrus **faktisk er bra for deg!**\nKjøp det her..."+"\n\n"+"https://www.amazon.com/Monster-Energy-Drink-Green-Original/dp/B019AKA6YU?th=1")
  await ctx.reply("....*sponsored by monster energy*")
  await ctx.message.delete()
  
@bot.command()
async def send_message(message, user_message, is_private):
        try:
            respons = responses1.get_response(user_message)
            await message.author.send(respons) if is_private else await message.channel.send(respons)
            
        except Exception as e:
            print(e) 

@bot.event
async def on_ready():
  print("Bot is ONLINE!...")


@bot.event
async def on_ready():
    activity = discord.Game(name="insert what you want the bots status to say here", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")

@bot.command()
async def status(ctx):
  await ctx.reply("Status:\ninsert a fun status message for you bot here")
  await ctx.message.delete()


@bot.command()
async def hello(ctx):
    await ctx.reply("Hello" + " " + "I'm "+ "**BOTnen**" + ", a Discord Bot created by Hans Botnen\nFor a list of my functions, type .botnen")



@bot.command()
async def add(ctx, num1, num2):
    await ctx.reply(float(num1)+float(num2))


@bot.command()
async def dice(ctx, dice):
    terning = randint(1, int(dice))
    await ctx.reply(str(terning))



@bot.command()
async def teams(ctx, *names: str):
    navn = []
    for e in names:
        navn.append(str(e))
    rnd.shuffle(navn)
    length = len(navn)
    midten = length//2
    lag1 = []
    lag2 = []
    lag1.append(navn[:midten])
    lag2.append(navn[midten:])
    await ctx.reply("Dette blir spennede...")
    sleep(1)
    await ctx.reply("LAG 1 -->   " + str(lag1))
    await ctx.reply("LAG 2 --> " + str(lag2))


@bot.command()
async def flip(ctx):
    terning = randint(1, 2)
    await ctx.reply("Flipping... 50/50")
    sleep(0.2)
    await ctx.reply("5")
    sleep(0.4)
    await ctx.reply("4")
    sleep(0.4)
    await ctx.reply("3")
    sleep(0.4)
    await ctx.reply("2")
    sleep(0.4)
    await ctx.reply("1")
    sleep(0.4)
    if terning == 1:
        await ctx.reply("Heads!")
    else:
        await ctx.reply("Tails!")


@bot.command(description='For when you cant decide what game to play next') #remove the leauge stuff if you actually wanna play that game...
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    lol = ["lol", "LOL", "leauge", "Leauge of legends", "Lol", "league", "League of legends"]
    liste = []
    for e in choices:
        if e not in lol:
            liste.append(str(e))

    rnd.shuffle(liste)
    
    await ctx.send("Jeg velger..."+" "+str(liste[0]))


@bot.command(name="ping")
async def some_crazy_function_name(ctx):
	await ctx.channel.send("pong")


@bot.event
async def on_delete():
    pass


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Check if the message starts with the bot's command prefix
    if message.content.startswith(bot.command_prefix):
        # Check if the message is a command and not just a random message starting with the command prefix
        ctx = await bot.get_context(message)
        if ctx.valid:  # If it's a valid command, let the command handler take care of it
            await bot.process_commands(message)
            return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    
        
    print(f'{username} said: "{user_message}" ({channel})')
        
    liste = message.id
        
        
        
    with open("log.txt", "a") as f:
        f.write("user : ")
        f.write(username)
        f.write("\n")
        f.write("said : ")
        f.write(user_message)
        f.write("\n")
        f.write("in channel : ")
        f.write(channel)
        f.write("\n")
        f.write("message ID : ")
        f.write(str(liste))
        f.write("\n")
        f.write("\n")
            
          
    if user_message[0] == '?':
        user_message = user_message[1:]
        await send_message(message, user_message, is_private=True)
    else:
        await send_message(message, user_message, is_private=False)

keep_alive()

bot.run(hemmeligkode)


