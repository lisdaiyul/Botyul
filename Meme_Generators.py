import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
  
@bot.command()
async def meme(lucu):
    luck = random.randint(1, 100)
    if luck == 7:
        img_name = random.choice(os.listdir('hartakarun'))
        with open(f'hartakarun/{img_name}', 'rb') as f:
            picture = discord.File(f)
    
        await lucu.send(file=picture)
    else:
        img_name = random.choice(os.listdir('Gambar-gambar'))
        with open(f'Gambar-gambar/{img_name}', 'rb') as f:
            picture = discord.File(f)
    
        await lucu.send(file=picture)

bot.run("TOKEN")
