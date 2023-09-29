import discord
from discord import Intents
from discord.ext import commands, tasks
import wolframalpha

intents = Intents.all()
intents.messages = True
status = cycle(['psyduck orz'])

@bot.event
async def on_ready(): change_status.start() 
print("[+] Ready")

@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))
  
bot = commands.Bot(command_prefix='psyduck ', intents=intents)

client = wolframalpha.Client('client-id')

@bot.command(name='orz')
async def orz(ctx, *, question: str):
    res = client.query(question)
    if res['@success'] == 'false':
        await ctx.send('I could not find an answer to your question.')
    else:
        answer = next(res.results).text
        await ctx.send(f'The answer to your question is: {answer}')

bot.run('your-bot-token')
