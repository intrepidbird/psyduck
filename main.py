import discord
from discord import Intents
from discord.ext import commands, tasks
import wolframalpha
from itertools import cycle

intents = Intents.all()
intents.messages = True
status = cycle(['psyduck orz'])
bot = commands.Bot(command_prefix='psyduck ', intents=intents)

@bot.event
async def on_ready(): change_status.start() 
print("Psyduck Ready! OTZ OTZ OTZ")

@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

client = wolframalpha.Client('id')

@bot.command(name='orz')
async def orz(ctx, *, question: str):
    try:
        res = client.query(question)
        if res['@success'] == 'false':
            await ctx.send('Even with Psyduck having infinite Mathematical knowledge, the answer cannot be found...')
        else:
            answer = next(res.results).text
            await ctx.send(f'Psyduck is so orz that he knows the answer is {answer}')
    except Exception as e:
        await ctx.send('Psyduck Errored')

bot.run('token')

