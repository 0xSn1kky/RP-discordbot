import discord
import time
from discord.ext import commands
import config as cfg
from config import cmds
from colorama import Back
p = cfg.prefixbot
# Настройки в config.py 
# Цвет
clr = discord.Color.blue()
# Префикс
client = commands.Bot(command_prefix=cfg.prefixbot)
# Удаление стандартной команды help
client.remove_command('help')

# Сообщение при готовности
@client.event
async def on_ready():
  print(Back.GREEN)
  print("---------------")
  print('Бот был запущен')
  print("---------------")
  print(Back.RESET)
  # Статус
  await client.change_presence(status=discord.Status.online, activity=discord.Game(f'{cfg.botname}, {cfg.prefixbot}help'))

# Команда help
@client.command()
async def help(ctx):
  cfg.cmds("help")
  name = ctx.message.author
  emb=discord.Embed(title="📖 Список команд", colour = clr, description = f" {name.mention} Все разделы (выберите): \n {p}Автор \n {p}Инфо - как использовать \n {p}Команды")
  await ctx.send(embed=emb)
  
@client.command()
async def автор (ctx):
      cfg.cmds("автор")
      await ctx.send(content="Вся информация о создателе кода бота 🔥 \n Youtube: https://youtube.com/channel/UCo3yqAlAobt4KB6o9UwQxeg \n Discord: 0xSn1kky.py#3352 \n Telegram: @dev_0xSn1kky \n VK: @0xSn1kky_dev")
 
@client.command()
async def команды (ctx):
      cfg.cmds("команды")
      emb=discord.Embed(title="📖 Список команд", colour=clr, description="""🎮 РП: \n\
👏 Похлопать \n\
🙀 Испугать [Польз] \n\
🤗 Обнять [Польз] \n\
💋 Поцеловать [Польз] \n\
🤮 Отравить [Польз] \n\
🎁 Подарить [Польз] \n\
👀 Посмотреть [Польз] \n\
😂 Смеяться \n\
😭 Плакать \n\
🚿 Облить [Польз] \n\
🍉 Покормить [Польз] \n\
🥶 Чувствовать \n\
💉 Заразить [Польз] \n\
🧙‍♂️ Заколдовать [Польз] \n\
🤜 Ударить [Польз]\n\
🔪 Убить [Польз]\n\
🔫 Расстрелять [Польз]\n\
💭 Стандартное:\n\
me - Действие от первого лица [Текст]\n\
do - Действие от третьего лица [Текст]\n\
s - кричать [Текст]\n\
w - Шептать [Текст]\n""")
      await ctx.send(embed=emb)
      
@client.command()
async def инфо (ctx):
    cfg.cmds("инфо")
    await ctx.send(f"Чтобы использовать РП команды нужно ввести команду с префиксом \n Пример: {p}Ударить @0xSn1kky.py")
    
@client.command()
async def похлопать(ctx):
    cfg.cmds("похлопать")
    name = ctx.message.author
    emb=discord.Embed(title="РП",  description=f"{name.mention} Похлопал(а) 👏 \n ", colour=clr)
    emb.set_thumbnail(url="https://media.tenor.com/jrIAsC6362EAAAAM/clap-clapping.gif")
    await ctx.send(embed=emb)

@client.command()
async def поцеловать(ctx, user):
    cfg.cmds("поцеловать")
    name = ctx.message.author
    emb=discord.Embed(title="РП",  description=f"{name.mention} \n Поцеловал(а) {user} 💋\n ", colour=clr)
    emb.set_thumbnail(url="https://media.tenor.com/qGwV4sHYkegAAAAM/anime-kiss-love.gif ")
    await ctx.send(embed=emb)

@client.command()
async def обнять(ctx, user):
    cfg.cmds("обнять")
    name = ctx.message.author
    emb=discord.Embed(title="РП",  description=f"{name.mention} \n Обнял(а) {user} 🤗 \n ", colour=clr)
    emb.set_thumbnail(url="https://media.tenor.com/iyztKN68avcAAAAM/aharen-san-aharen-san-anime.gif ")
    await ctx.send(embed=emb)

@client.command()
async def испугать(ctx, user):
    cfg.cmds("испугать")
    name = ctx.message.author
    emb=discord.Embed(title="РП",  description=f"{name.mention} \n Испугал(а) {user} 👻\n ", colour=clr)
    emb.set_thumbnail(url="https://media.tenor.com/Ig2M0z7xKbUAAAAM/scared-spongebob.gif")
    await ctx.send(embed=emb)
    
@client.command()
async def отравить(ctx, user):
    cfg.cmds("отравить")
    name = ctx.message.author
    emb=discord.Embed(title="РП",  description=f"{name.mention} \n Отравил(а) {user} 🤮\n ", colour=clr)
    emb.set_thumbnail(url="https://media.tenor.com/DGruVzwFZvkAAAAM/sick-puke.gif")
    await ctx.send(embed=emb)
    
@client.command()
async def подарить(ctx, user):
    cfg.cmds("подарить")
    name = ctx.message.author
    emb=discord.Embed(title="РП",  description=f"{name.mention} \n Подарил(а) подарок {user} 🎁\n ", colour=clr)
    emb.set_thumbnail(url="https://media.tenor.com/0V8ccm1fuBUAAAAM/glee-blaine-anderson.gif")
    await ctx.send(embed=emb)
    
@client.command()
async def посмотреть(ctx, user):
    cfg.cmds("посмотреть")
    name = ctx.message.author
    emb=discord.Embed(title="РП",  description=f"{name.mention} \n Посмотрел(а) на {user} 👀\n ", colour=clr)
    emb.set_thumbnail(url="https://media.tenor.com/MZ6-fJOmafYAAAAM/eyes-looking.gif ")
    await ctx.send(embed=emb)
      
@client.command()
async def смеяться(ctx):
    cfg.cmds("похлопать")
    name = ctx.message.author
    emb=discord.Embed(title="РП",  description=f"{name.mention} Посмеялся(ась) \n 😂", colour=clr)
    emb.set_thumbnail(url="https://media.tenor.com/An-9HfjvNkwAAAAM/kuroo-tetsurou-haikyuu.gif")
    await ctx.send(embed=emb)

@client.command()
async def плакать(ctx):
    cfg.cmds("плакать")
    name = ctx.message.author
    emb=discord.Embed(title="РП",  description=f"{name.mention} \n Плакал(а) 😭\n ", colour=clr)
    emb.set_thumbnail(url="https://media.tenor.com/A0g9Rrx4aNsAAAAM/sad-angry.gif ")
    await ctx.send(embed=emb)

@client.command()
async def облить(ctx, user):
    cfg.cmds("облить")
    name = ctx.message.author
    emb=discord.Embed(title="РП",  description=f"{name.mention} \n Облил(а) {user} 🚿\n ", colour=clr)
    emb.set_thumbnail(url="https://media.tenor.com/9ESH14I4UOcAAAAM/tom-and-jerry-water.gif")
    await ctx.send(embed=emb)

@client.command()
async def покормить(ctx, user):
    cfg.cmds("покормить")
    name = ctx.message.author
    emb=discord.Embed(title="РП",  description=f"{name.mention} \n Покормил(а) {user} 🥓\n ", colour=clr)
    emb.set_thumbnail(url="https://media.tenor.com/Udkdkaf6-PQAAAAM/masha-bunny.gif")
    await ctx.send(embed=emb)

@client.command()
async def чувствовать(ctx):
    cfg.cmds("чувствовать")
    name = ctx.message.author
    emb=discord.Embed(title="РП",  description=f"{name.mention} Жестко чувствует 🥶 🥶 🥶 🥶 \n ", colour=clr)
    emb.set_thumbnail(url="https://media.tenor.com/0ZWSvwf-06QAAAAM/putin-dance.gif ")
    await ctx.send(embed=emb)

@client.command()
async def заразить(ctx, user):
    cfg.cmds("заразить")
    name = ctx.message.author
    emb=discord.Embed(title="РП",  description=f"{name.mention} \n Заразил(а) {user} 💉\n ", colour=clr)
    emb.set_thumbnail(url="https://media.tenor.com/UgY-tdOoRVsAAAAM/tom-and-jerry-cat.gif ")
    await ctx.send(embed=emb)

@client.command()
async def заколдовать(ctx, user):
    cfg.cmds("испугать")
    name = ctx.message.author
    emb=discord.Embed(title="РП",  description=f"{name.mention} \n Заколдовал(а) {user} 🧙‍♂️\n ", colour=clr)
    emb.set_thumbnail(url="https://media.tenor.com/PvZVfItyThoAAAAM/keystone-science-magic.gif")
    await ctx.send(embed=emb)

@client.command()
async def ударить(ctx, user):
    cfg.cmds("ударить")
    name = ctx.message.author
    emb=discord.Embed(title="РП",  description=f"{name.mention} \n Ударил(а) {user} 🤜 \n ", colour=clr)
    emb.set_thumbnail(url="https://media.tenor.com/z-bP0d5aYnMAAAAM/golpe-anime.gif ")
    await ctx.send(embed=emb)

@client.command()
async def убить(ctx, user):
    cfg.cmds("убить")
    name = ctx.message.author
    emb=discord.Embed(title="РП",  description=f"{name.mention} \n Убил(а) {user} 🔪\n ", colour=clr)
    emb.set_thumbnail(url="https://media.tenor.com/NbBCakbfZnkAAAAM/die-kill.gif")
    await ctx.send(embed=emb)

@client.command()
async def расстрелять(ctx, user):
    cfg.cmds("расстрелять")
    name = ctx.message.author
    emb=discord.Embed(title="РП",  description=f"{name.mention} \n Расстрелял(а) {user} 🔫\n ", colour=clr)
    emb.set_thumbnail(url="https://media.tenor.com/DnaBYckm8b8AAAAM/%D0%BD%D0%B5%D0%BF%D0%BE%D1%81%D0%BB%D1%83%D1%88%D0%BD%D1%8B%D0%B9.gif")
    await ctx.send(embed=emb)

@client.command()
async def me(ctx, text):
    cfg.cmds("me")
    name = ctx.message.author
    emb=discord.Embed(title="РП",  description=f"{name.mention} {text}", colour=clr)
    emb.set_footer(text=f"{cfg.botname} Me")
    await ctx.send(embed=emb)

@client.command()
async def s(ctx, text):
    cfg.cmds("s")
    name = ctx.message.author
    emb=discord.Embed(title="РП",  description=f"{name.mention} Крикнул: {text}", colour=clr)
    emb.set_footer(text=f"{cfg.botname} S")
    await ctx.send(embed=emb)

@client.command()
async def do(ctx, text):
    cfg.cmds("do")
    name = ctx.message.author
    emb=discord.Embed(title="РП",  description=f"{name.mention} {text}", colour=clr)
    emb.set_footer(text=f"{cfg.botname} do")
    await ctx.send(embed=emb)

@client.command()
async def w(ctx, text):
    cfg.cmds("w")
    name = ctx.message.author
    emb=discord.Embed(title="РП",  description=f"{name.mention} {text}", colour=clr)
    emb.set_footer(text=f"{cfg.botname} W")
    await ctx.send(embed=emb)


# Запуск бота

client.run(cfg.token)