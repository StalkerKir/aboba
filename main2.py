import discord
import random
import json
import requests

from music import music
from discord.ext import commands
TOKEN=open('token.txt','r', encoding="utf8").read()
bot = commands.Bot(command_prefix='ss ')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command(pass_context=True)
async def повтор(ctx, *arg):
    await ctx.send(' '.join(arg))

@bot.command()
async def fox(ctx):

    embed = discord.Embed(color = 0xff9900, title = 'Random Fox') # Создание Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command(pass_context=True)
async def lyrics(ctx, *args):
    author, name = ' '.join(args).split(', ')
    if author not in music:
        await ctx.send('Этот автор не добавлен')
        return True
    if all([name != i for i in music[author]]):
        await ctx.send("Этой песни автора пока нет.")
        return True
    for i in music:
        if i == author:
            for j in music[i]:
                if j == name:
                    await ctx.send(music[author][name])

@bot.command()
async def info(ctx):
    embed = discord.Embed(color = 0xff9900, title = 'Random Fox') # Создание Embed'a
    await ctx.send(embed = embed) # Отправляем Embed
    await ctx.send('''```Cписок команд: 
    ss повтор - повторяет ваш текст
    ss еда - бот выдает свою любимую еду 
    ss lyrics [Автор], [Название песни] - выводит текст песни
    ss хто_я - объявляет себя```''')


@bot.command()
async def еда(ctx):
    await ctx.send(":banana:")

@bot.command()
async def хто_я(ctx):
    await ctx.send("Я Обэмэ нафиг")

@bot.command()
async def coin(ctx):
    a = random.randint(0, 1)
    if a == 0:
        coin='Орёл'
    else:
        coin='Решка'
    await ctx.send("`"+coin+"`")

bot.run(TOKEN)
