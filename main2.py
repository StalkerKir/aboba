import discord
from PIL.Image import Resampling
from bs4 import BeautifulSoup, Tag
import random
import requests
import io
from PIL import Image, ImageFont, ImageDraw
import logging
logger = logging.getLogger('logger')
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle

ssylka = ''
TOKEN=open('token.txt','r', encoding="utf8").read()
bot = commands.Bot(command_prefix='en ')

@bot.event
async def on_ready():
    DiscordComponents(bot)
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def армяне(ctx, *arg):
    await ctx.send(' '.join(arg)+', а там армяне в нарды играют')

@bot.command()
async def card(ctx, member: discord.Member):
    await ctx.channel.purge(limit = 1)
    img = Image.new("RGBA", (450, 120), 0x08a15c)
    url = str(member.avatar_url)[:-10]
    response = requests.get(url, stream = True)
    response = Image.open(io.BytesIO(response.content))
    response = response.convert('RGBA')
    response = response.resize((100,100), Resampling.LANCZOS)
    img.paste(response, (5, 15, 105, 115))
    idraw = ImageDraw.Draw(img)
    name = member.name
    tag = member.discriminator
    stata = member.status
    print(member)
    headline = ImageFont.truetype('arial.ttf', size = 20)
    undertext = ImageFont.truetype('arial.ttf', size = 20)
    idraw.text((145, 15), f'{name}#{tag}', font = headline)
    idraw.text((145, 50), f'ID: {member.id}', font = undertext)
    idraw.text((145, 90), f'{stata}', font = undertext)
    img.save('card.png')
    await ctx.send(file = discord.File(fp = 'card.png'))


@bot.command()
async def голосование(ctx, *args):
    name, k = ' '.join(args).split(', ')
    k = int(k)
    for i in k:
        a
    await ctx.send(
        embed = discord.Embed(title = 'Invite to party'),
        components=[
            Button(style=ButtonStyle.green, label='Accept', emoji="✨"),
            Button(style=ButtonStyle.red, label = 'Go to the dick', emoji="👨🏿")
        ]
    )

    response = await bot.wait_for("button_click")
    if response.channel == ctx.channel:
        if response.component.label == 'Accept':
            await response.respond(content='Great! 😎')
        else:
            await response.respond(
                embed=discord.Embed(title='Are you sure?'),
                components=[
                    Button(style=ButtonStyle.green, label='YES'),
                    Button(style=ButtonStyle.red, label='NO'),
                ]
            )

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
    **en повтор** - повторяет ваш текст
    **en еда** - бот выдает свою любимую еду 
    **en text [Автор]; [Название песни]** - выводит текст песни
    **en coin** - подбрасывает монетку
    **en кто_я** - объявляет себя
    **en армяне** - улучшает любой анекдот в сотню раз
    **en голосование** - позволяет создавать голосование по каким-то вопросам
    **Блок команд, связанных с сайтом Лоры Провансаль:**
    **en лора_список** - выдает список всех альбомов Лоры
    **en лора_категория [Название альбома]** - выдает список песен в искомом альбоме
    **en лора_песня [Название песни, находящейся в выбранном ранее альбоме]** - выдает текст песни (не всегда полностью)'''
    embed = discord.Embed(color = 0x08a15c, title = 'Список команд',description=spis) # Создание Embed'a
    await ctx.send(embed = embed) # Отправляем Embed



@bot.command()
async def еда(ctx):
    await ctx.send(":banana:")

@bot.command()
async def хто_я(ctx):
    await ctx.send("Я бот, созданный для парсинга сайтов и удобного пребывания в дискорде")

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
    author, name = ' '.join(args).split('; ')
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
            href_ = a.attrs["href"]
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
    ssylka = 'http://www.treismorgess.ru/?p='+ap
    response=requests.get(ssylka)
    soup=BeautifulSoup(response.text,'html.parser')
    sel='tr:nth-child(2) > td > div.content > ul'
    b=soup.select_one(sel)
    get_text = b.get_text(separator='\n')
    embed = discord.Embed(color = 0x08a15c, title = arg, description=get_text) # Создание Embed'a
    await ctx.send(embed = embed) # Отправляем Embed
    ap='0'
@bot.command()
async def вывод_ссылки(ctx):
    global ssylka
    if ssylka == '':
            ssylka = 'https://lotr.fandom.com/ru/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
    await ctx.send(ssylka)

@bot.command()
async def лора_песня(ctx, *arg):
    global ssylka
    arg = ' '.join(arg)
    response=requests.get(ssylka)
    soup=BeautifulSoup(response.text,'html.parser')
    sel = 'tr:nth-child(2) > td > div.content > ul'
    select = soup.select(sel)
    s = soup.select("a[href^='?p=']")
    c=None
    href_ = None
    for i in range(0,len(s)):
        #if (s[i] == '?') and (s[i+1] == 'p') and (s[i+2] == '=') .startsWith("?p="):
        if s[i].text==arg:
            c = s[i].attrs['href']
            href_ = 'http://www.treismorgess.ru/?p='+c[3:]
            break
    # href_ = None
    # print(href_)
    if href_ is None:
        embed = discord.Embed(color = 0x08a15c, title = 'Ошибка',description="Песня не найдена") # Создание Embed'a
        await ctx.send(embed = embed) # Отправляем Embed
        return
    sel2 = 'tr:nth-child(2) > td > div.content > div'
    soup=BeautifulSoup(requests.get(href_).text,'html.parser')
    b=soup.select_one(sel2)
    print(b)
    lines = b.select("p")
    res = ""
    for i in lines:
        if i.select('span') or i.select('u'):
            res1=""
            for j in i.select("span"):
                res1+=j.get_text()+'\n'
                # res+=i.get_text()+"\n"
            res+=res1
        else:
            res+=i.get_text(separator='\n')
    get_text = res
    embed = discord.Embed(color = 0x08a15c, title = arg, description=get_text) # Создание Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

# @bot.command()
# async def wiki(ctx, arg):
#     # url = 'https://ru.wikipedia.org/wiki/' + arg
#     url = 'https://ru.wikipedia.org/w/index.php?search='+arg+'&title=Служебная:Поиск&profile=advanced&fulltext=1&ns0=1'
#     response=requests.get(url)
#     soup=BeautifulSoup(response.text,'html.parser')
#     sel = '#mw-content-text > div.searchresults.mw-searchresults-has-iw > ul > li:nth-child(1) > div.mw-search-result-heading'
#     select = soup.select_one(sel)
#     a = select.select_one(sel)
#     # print(a.attrs)
#     href_ = "https:" + a.attrs["href"]
#     sel2 = '#mw-content-text > div.mw-parser-output'
#     soup=BeautifulSoup(requests.get(href_).text,'html.parser')
#     b=soup.select_one(sel2)
#     for c in b.children:
#         if str(c).startswith('<p>'):
@bot.command()
async def Арагорн_сын_Араторна(ctx):
    spis = '''
    Арагорн II сын Араторна II
    Араторн II сын Арадора
    Арадор сын Аргонуи
    Аргонуи сын Араторна I
    Араторн I сын Арассуила
    Арассуил сын Арахада II
    Арахад II сын Араворна
    Араворн сын Арагоста
    Арагост сын Арахада I
    Аразад I сын Арагласа
    Араглас сын Арагорна I 
    Арагорн I сын Аравира
    Аравир сын Арануира
    Арануир сын Арахэля
    Арахаэль сын Аранарта
    Аранарт сын Арведуи
    Арведуи сын Арафанта
    Арафант сын Аравал
    Аравал сын Арвелега II
    Арвелег II сын Арвегила
    Арвегил сын Аргелеба II
    Аргелеб II сын Арафора
    Арафор сын Арвелега I
    Арвелег I сын Аргелеба I
    Аргелеб I сын Малвегила
    Малвегил сын Келебриндора
    Келебриндор сын Келефарна
    Келефарн сын Маллор
    Маллор сын Белега
    Белег сын Амлайта
    Амлайт сын Эарендура
    Эарендур сын Элендура
    Элендур сын Валандура
    Валадур сын Тарондора
    Тарондор сын Таркила
    Таркил сын Арантара
    Арантар сын Эльдакара
    Эльдакар сын Валандил
    Валандил сын Исилдура
    Исилдур сын Элендила
    Элендил сын Амандиля
    Амандиль сын Нумендиля
    Нумендиль сын ???
    ??? сын Эарендура
    *пробел в летописи*
    Валандиль сын Сильмариэн
    Сильмариэн дочь Тар-Элендиля
    Тар-Элендиль сын Тар-Амандиля
    Тар-Амандиль сын Вардамира Нолимона
    Вардамир Нолимон сын Элроса Тар-Миньятура
    Элрос Тар-Миньятур сын Эарендиля Морехода
    Эарендиль Мореход сын Туора Эладара
    Туор Эладар сын Хуора
    Хуор сын Галдора
    Галдор сын Хадора Златовласого
    Хадор Златовласый сын Хатола
    Хатол сын Магора
    Магор сын Малаха
    Малах сын Мараха
    *Конец известной хронологии*
    '''
    embed = discord.Embed(color = 0x08a15c, title = 'Родословная Арагорна по мужской линии', description=spis) # Создание Embed'a
    await ctx.send(embed = embed) # Отправляем Embed
    # get_text = b.get_text(separator='')
    # print(response.text)
    # sel = '#mw-content-text > div.mw-parser-output ul'
    # b=soup.select(sel)
    # get_text = b.get_text(separator='\n')
    # print(get_text)
    # embed = discord.Embed(color = 0x08a15c, title = arg, description=get_text) # Создание Embed'a
    # await ctx.send(embed = embed) # Отправляем Embed

# @bot.command()
# async def kick(ctx, user : discord.User(), *arg, reason='Причина не указана'):
#     await bot.kick(user)
#     await ctx.send('Пользователь {user.name} был изгнан по причине "{reason}"')

# @bot.command()
# async def check_account_age(self, author: discord.Member) -> bool:
#         account_age = self.config.get("account_age")
#         now = datetime.utcno w()
#
#         try:
#             min_account_age = author.created_at + account_age
#         except ValueError:
#             logger.warning("Error with 'account_age'.", exc_info=True)
#             min_account_age = author.created_at + self.config.remove("account_age")
#
#         if min_account_age > now:
#             # User account has not reached the required time
#             delta = human_timedelta(min_account_age)
#             logger.debug("Blocked due to account age, user %s.", author.name)
#
#             if str(author.id) not in self.blocked_users:
#                 new_reason = f"System Message: New Account. Required to wait for {delta}."
#                 self.blocked_users[str(author.id)] = new_reason
#
#             return False
#         return True

# class Tutorial(commands.Cog):
#     def _init_(self, bot):
#         self.bot = bot
#
#         @commands.Cog.listener()
#         async def on_member_join(self, member):
#             channel = member.guild.system_channel
#             await channel.send(embed = discord.Embed(description=f'{member.mention} Добро пожаловать на сервер!'))
#
# def setup(bot):
#     bot.add_cog(Tutorial(bot))
bot.run(TOKEN)


