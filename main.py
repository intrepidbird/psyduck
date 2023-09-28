import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='$')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def quack(ctx):
    await ctx.send('Quack quack 🦆')

@bot.command()
async def super_command(ctx):
    responses = ['intrepidbird', 'igafig']
    await ctx.send(random.choice(responses))

@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)

@bot.command()
async def tictactoe(ctx, a: int, b: int):
    # This is a placeholder for the actual implementation of the game.
    # Game logic coming soon...
    await ctx.send('This is where the tic-tac-toe game would be played.')

bot.run('token')
