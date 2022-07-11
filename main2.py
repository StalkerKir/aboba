import discord
from bs4 import BeautifulSoup, Tag
import random
from collections import defaultdict
import requests

ssylka = ''
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
    **ss повтор** - повторяет ваш текст
    **ss еда** - бот выдает свою любимую еду 
    **ss text [Автор], [Название песни]** - выводит текст песни
    **ss coin** - подбрасывает монетку
    **ss хто_я** - объявляет себя'''
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
    # #body > div.content-table > article > div.b-podbor > div:nth-child(2) > div.b-podbor__text > pre
    soup=BeautifulSoup(requests.get(href_).text,'html.parser')
    b=soup.select_one(sel2)
    get_text = b.get_text(separator='')
    get_text = "**"+name+"**"+'''
    '''+get_text
    embed = discord.Embed(color = 0x08a15c, title = author, description=get_text) # Создание Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command(pass_context=True)
async def лора_список(ctx,*args):
    spis = '''
    **Тампль** 
    **Западный предел** - Толкин
    **Небьющееся сердце** - 17 век и барокко
    **College of St-Joanna** - Гарри Поттер
    **Пепел Монсегюра** - Средневековье
    **Чай со слоном** - Махабхарата
    Корень (**-**) - остальное
    '''
    embed = discord.Embed(color = 0x08a15c, title = 'Список категорий',description=spis) # Создание Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command(pass_context=True)
async def лора_категория(ctx, *arg):
    global ssylka
    ap='0'
    arg = ' '.join(arg)
    if arg == 'Тампль':
        ap='5'
    elif arg == 'Западный предел':
        ap = '644'
    elif arg == 'Небьющееся сердце':
        ap = '605'
    elif arg == 'College of St-Joanna':
        ap='159'
    elif arg == 'Пепел Монсегюра':
        ap='675'
    elif arg == 'Чай со слоном':
        ap='723'
    elif arg == '-':
        ap='4'
    else:
        embed = discord.Embed(color = 0x08a15c, title = 'Ошибка',description="Категория не найдена") # Создание Embed'a
        await ctx.send(embed = embed) # Отправляем Embed
    ssylka += 'http://www.treismorgess.ru/?p='+ap
    response=requests.get(ssylka)
    soup=BeautifulSoup(response.text,'html.parser')
    sel='tr:nth-child(2) > td > div.content > ul'
    b=soup.select_one(sel)
    get_text = b.get_text(separator='\n')
    embed = discord.Embed(color = 0x08a15c, title = arg, description=get_text) # Создание Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def вывод_ссылки(ctx):
    global ssylka
    if ssylka == '':
            ssylka = 'https://lotr.fandom.com/ru/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
    await ctx.send(ssylka)
bot.run(TOKEN)
