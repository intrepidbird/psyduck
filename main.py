import discord
from discord import Intents
from discord.ext import commands, tasks
import wolframalpha
from itertools import cycle
import openai

intents = Intents.all()
intents.messages = True
status = cycle(['psyduck orz'])
bot = commands.Bot(command_prefix='psyduck ', intents=intents)

@bot.event
async def on_ready(): change_status.start() 
print("[+] Psyduck is ready")

@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

openai.api_key = 'openai-api'
client = wolframalpha.Client('wolfram-api')

@bot.command(name='orz')
async def orz(ctx, *, question: str):
    try:
        res = client.query(question)
        if res['@success'] == 'false':
            await ctx.send('Psyduck cannot find the answer')
        else:
            answer = next(res.results).text
            await ctx.send(f'Psyduck found out that the answer is {answer}')
    except Exception as e:
        await ctx.send('Psyduck Errored')

@bot.command(name='ai')
async def gpt3(ctx, *, prompt: str):
    try:
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100)
        await ctx.send(response.choices[0].text.strip())
    except Exception as e:
        await ctx.send('Psyduck Errored')

bot.run('bot-token')
