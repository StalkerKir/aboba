import discord
from bs4 import BeautifulSoup, Tag
import random
from collections import defaultdict
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

@bot.command(pass_context=True)
async def song(ctx):
    page = requests.get("https://genius.com/")
    await ctx.send(page.text)

# @bot.command(pass_context=True)
# async def lyrics(ctx, *args):
#     author, name = ' '.join(args).split(', ')
#     if author not in music:
#         await ctx.send('Этот автор не добавлен')
#         return True
#     if all([name != i for i in music[author]]):
#         await ctx.send("Этой песни автора пока нет.")
#         return True
#     for i in music:
#         if i == author:
#             for j in music[i]:
#                 if j == name:
#                     await ctx.send(music[author][name])

@bot.command()
async def info(ctx):
    spis='''
    ss повтор - повторяет ваш текст
    ss еда - бот выдает свою любимую еду 
    ss lyrics [Автор], [Название песни] - выводит текст песни
    ss coin - подбрасывает монетку
    ss хто_я - объявляет себя'''
    embed = discord.Embed(color = 0x08a15c, title = 'Список команд',description=spis) # Создание Embed'a
    await ctx.send(embed = embed) # Отправляем Embed



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

@bot.command(pass_context=True)
async def text(ctx,*args):
    author, name = ' '.join(args).split(', ')
    url='https://amdm.ru/search/?q='+author+' '+name

    # print(url)
    response=requests.get(url)
    # print(response.text)

    # sel = '#application > main > div.SongPageGriddesktop-sc-1px5b71-0.bRkvZc.SongHeaderdesktop__Container-sc-1effuo1-0.ldQzNt > div.SongHeaderdesktop__Column-sc-1effuo1-1.SongHeaderdesktop__Center-sc-1effuo1-3.kUJuua > div > h1 > span'
    soup=BeautifulSoup(response.text,'html.parser')
    #sel1 = '#ya-site-results > div > yass-div > table.l-page.l-page_layout_70-30.l-page_type_search > tbody > tr > td > yass-div.b-body-items > yass-ol > yass-li:nth-child(1) > yass-div > yass-h3 > a > yass-span'
    # sel1='#ya-site-results > div > yass-div > table.l-page.l-page_layout_70-30.l-page_type_search > tbody > tr > td > yass-div.b-body-items > yass-ol > yass-li:nth-child(1) > yass-div > yass-h3 > a > yass-span'
    sel1 = "table > tr"
    select = soup.select(sel1)
    href_=None
    for i in range(0,len(select)):
        text = select[i].text
        if name in text:
            sel2 = "a:nth-child(2)"
            a = select[i].select_one(sel2)
            # print(a.attrs)
            href_ = "https:" + a.attrs["href"]
            break
    if href_ is None:
        embed = discord.Embed(color = 0x08a15c, title = 'Ошибка',description="Песня не найдена") # Создание Embed'a
        await ctx.send(embed = embed) # Отправляем Embed
        return
    # await ctx.send(href_)
    # print(requests.get(href_).text)
    sel2='div.content-table > article > div.b-podbor > div:nth-child(2) > div.b-podbor__text > pre'
    soup=BeautifulSoup(requests.get(href_).text,'html.parser')
    b=soup.select_one(sel2)
    get_text = b.get_text(separator='')
    embed = discord.Embed(color = 0x08a15c, title = name,description=get_text) # Создание Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

bot.run(TOKEN)
