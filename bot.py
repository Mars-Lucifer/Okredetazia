import disnake
from disnake.ext import commands
import asyncio

config = {}

with open('config.txt', 'r') as file:
    for line in file:
        key, value = line.strip().split('=')
        config[key.strip()] = value.strip()

final_config = {
    'token': config['token'],
    'prefix': '>',
}

intents = disnake.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix=config['prefix'], intents=intents, test_guilds=[1048304837567193088]) 

@bot.event
async def on_ready():
    print("Started")

@bot.slash_command(description="Русский язык")
async def rus(inter):
    await inter.send('Отправка сообщений начнется через 5 секунт с интервалом 10 минут')
    await asyncio.sleep(5)
    with open('sub/rus.txt', "r", encoding="utf-8") as file:
        lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            await inter.author.send("`" + line.strip() + "`")
            await asyncio.sleep(1)
            if i % 9 == 0:
                await asyncio.sleep(600)

@bot.slash_command(description="Математика")
async def mat(inter):
    await inter.send('Отправка сообщений начнется через 5 секунт с интервалом 10 минут')
    await asyncio.sleep(5)
    with open('sub/mat.txt', "r", encoding="utf-8") as file:
        lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            await inter.author.send(line.strip())
            await asyncio.sleep(1)
            if i % 9 == 0:
                await asyncio.sleep(600)

@bot.slash_command(description="Физика")
async def phis(inter):
    await inter.send('Отправка сообщений начнется через 5 секунт с интервалом 10 минут')
    await asyncio.sleep(5)
    with open('sub/phis.txt', "r", encoding="utf-8") as file:
        lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            await inter.author.send("`" + line.strip() + "`")
            await asyncio.sleep(1)
            if i % 9 == 0:
                await asyncio.sleep(600)

@bot.slash_command(description="Введение в специальность")
async def vi(inter):
    await inter.send('Отправка сообщений начнется через 5 секунт с интервалом 10 минут')
    await asyncio.sleep(5)
    with open('sub/vi.txt', "r", encoding="utf-8") as file:
        lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            await inter.author.send("`" + line.strip() + "`")
            await asyncio.sleep(1)
            if i % 9 == 0:
                await asyncio.sleep(600)

@bot.slash_command(description="Литература")
async def litr(inter):
    await inter.send('Отправка сообщений начнется через 5 секунт с интервалом 10 минут')
    await asyncio.sleep(5)
    with open('sub/litr.txt', "r", encoding="utf-8") as file:
        lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            await inter.author.send("`" + line.strip() + "`")
            await asyncio.sleep(1)
            if i % 9 == 0:
                await asyncio.sleep(600)

@bot.slash_command(description="ОБЖ")
async def obj(inter):
    await inter.send('Отправка сообщений начнется через 5 секунт с интервалом 10 минут')
    await asyncio.sleep(5)
    with open('sub/obj.txt', "r", encoding="utf-8") as file:
        lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            await inter.author.send("`" + line.strip() + "`")
            await asyncio.sleep(1)
            if i % 9 == 0:
                await asyncio.sleep(600)

@bot.slash_command(description="Астрономия")
async def astro(inter):
    await inter.send('Отправка сообщений начнется через 5 секунт с интервалом 10 минут')
    await asyncio.sleep(5)
    with open('sub/astro.txt', "r", encoding="utf-8") as file:
        lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            await inter.author.send("`" + line.strip() + "`")
            await asyncio.sleep(1)
            if i % 9 == 0:
                await asyncio.sleep(600)

@bot.slash_command(description="География")
async def geo(inter):
    await inter.send('Отправка сообщений начнется через 5 секунт с интервалом 10 минут')
    await asyncio.sleep(5)
    with open('sub/geo.txt', "r", encoding="utf-8") as file:
        lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            await inter.author.send("`" + line.strip() + "`")
            await asyncio.sleep(1)
            if i % 9 == 0:
                await asyncio.sleep(600)

@bot.slash_command(description="Обществознание")
async def obshe(inter):
    await inter.send('Отправка сообщений начнется через 5 секунт с интервалом 10 минут')
    await asyncio.sleep(5)
    with open('sub/obshe.txt', "r", encoding="utf-8") as file:
        lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            await inter.author.send("`" + line.strip() + "`")
            await asyncio.sleep(1)
            if i % 9 == 0:
                await asyncio.sleep(600)

@bot.slash_command(description="Английский язык")
async def eng(inter):
    await inter.send('Отправка сообщений начнется через 5 секунт с интервалом 10 минут')
    await asyncio.sleep(5)
    with open('sub/eng.txt', "r", encoding="utf-8") as file:
        lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            await inter.author.send("`" + line.strip() + "`")
            await asyncio.sleep(1)
            if i % 9 == 0:
                await asyncio.sleep(600)

@bot.slash_command()
async def test(inter):
    await inter.response.defer()
    await inter.edit_original_response(content="Бот активен")

bot.run(config['token'])
