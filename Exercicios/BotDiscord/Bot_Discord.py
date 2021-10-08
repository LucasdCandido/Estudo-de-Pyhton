import discord
from discord.ext import commands
from segredos import token

bot = commands.Bot("!")

@bot.event
async def on_ready():
    print(f'Estou Pronto! Estou conectado como {bot.user}')

@bot.command()
async def send_hello(ctx):
    name = ctx.author.name

    response = 'Olá, ' + name

    await ctx.send(response)

bot.run(token)