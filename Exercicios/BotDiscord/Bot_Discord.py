import discord
from datetime import datetime
from discord.ext import commands
from segredos import token

bot = commands.Bot("!")


@bot.event
async def on_ready():
    print(f'Estou Pronto! Estou conectado como {bot.user}')
    current_time.start()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'palavrão' in message.content:
        await message.channel.send(f'Por favor, {message.author.name}, não ofenda os demais usuarios!')

        await message.delete()

    await bot.process_commands(message)


@bot.command(name='oi')
async def send_hello(ctx):
    name = ctx.author.name

    response = 'Olá, ' + name

    await ctx.send(response)

@tasks.loop(seconds=10)
async def current_time():
    now = datetime.datetime.now()

    now = now.strftime('%d/%m/%y as %H:%M:$S')

    channel = bot.get_channel(834798471889813558)

    await channel.send('Data atual: ' + now)


bot.run(token)