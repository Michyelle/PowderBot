import discord
import random
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

def randomPowder():
    pics_folder = "picsOfPowder"
    pics = os.listdir(pics_folder)
    random_pic = random.choice(pics)
    return os.path.join(pics_folder, random_pic)

jokes = [
    "There are 10 types of people in the world, those who understand binary and those who don't",
    "Why did the dog sit in the shade? Because he didn't want to be a hot dog!",
    "How do you make a dog stop barking in the front yard? Put him in the backyard!",
    "Why do C++ programmers prefer dark mode? Because light attracts bugs!",
    "How does a C++ programmer propose? They say, 'You complete me like my code completes a function!'",
    "What's a C++ programmer's favorite type of party? A polymorphism party - it's always a different experience!",
    "Why do C++ programmers hate nature? It has too many bugs!",
    "What's a C++ programmer's favorite snack? NULL and void cookies"
]

@bot.event
async def on_ready():
    print(f'{bot.user} successfully connected to Discord!')

@bot.command()
async def helpcommands(ctx):
    embed = discord.Embed(title="Help", description=" ", color=0xf8c8dc)
    embed.add_field(name='!hi', value='Greet the user with a random message.', inline=False)
    embed.add_field(name='!powder', value='Send a random picture.', inline=False)
    embed.add_field(name='!joke', value='Tell a random joke.', inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def hi(ctx):
    greetings = [
    f'Well, well, well, if it isn\'t {ctx.author.mention} gracing us with their presence!',
    f'Look who decided to show up! Hi there, {ctx.author.mention}!',
    f'Oh, it\'s you, {ctx.author.mention}! Brace yourself for my amazing company!',
    f'Hey, {ctx.author.mention}! How are you?',
    f'A wild {ctx.author.mention} appears! How can I assist you today?',
    f'Greetings, {ctx.author.mention}! Did you bring snacks? No? Well, you better have a good reason then!',
    f'Oh look, {ctx.author.mention} is here. The party can officially start now!',
    ]
    greeting = random.choice(greetings)
    await ctx.send(greeting)

@bot.command()
async def joke(ctx):
    joke = random.choice(jokes)
    await ctx.send(joke)

@bot.command()
async def powder(ctx):
    picsOfPow = randomPowder()
    await ctx.send(file=discord.File(picsOfPow))


bot.run(token)