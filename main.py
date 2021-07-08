import io

import discord
import aiohttp
from discord import File
from discord.ext import commands
client = commands.Bot(command_prefix='$', case_insensitive=True)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))




@client.event
async def on_message(message):
    msg = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith('$help'):
        await message.channel.send('*Commands are*:\n ** >>> $info\n$topi\n$bakat\n$greet\n$ping\n$src\n$pic**')
    if message.content.startswith('$topi'):
        await message.channel.send('```fix\n Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ```')
    if message.content.startswith('$bakat'):
        await message.channel.send(f'```yaml\n Di diay mu bakat ang imoha {message.author.name}? ```')
    if message.content.startswith('$info'):
        await message.channel.send('> **Topi Bot was created in honor of the late Vietnam War Veteran Brig. General Christopher Lao. '
                                   'The Topi in Topi Bot is derived from Christophers nickname which is kinda lame imho** *GAMAY OTEN TOPI*')
    if message.content.startswith('$greet'):
        await message.channel.send(f'> Hello {message.author.name}')
    if message.content.startswith('$ping'):
        await message.channel.send(f'```fix\nMy server latency: {round(client.latency * 1000)}ms``` ')
    if msg.startswith('gg'):
        await message.channel.send(f'```yaml\n Good Game {message.author.name}! Toms again ``` ')
    if msg.startswith('$src'):
        await message.channel.send('> **SHAMELESS PLUG** \n'
                                   '> Hey, check out the source code written on python here on my github page: **https://github.com/beefysalad/Discordbot/blob/main/main.py**'
                                   '  \n > You can also checkout my github page and give me a follow XD ** https://github.com/beefysalad **')
    if msg.startswith('jett'):
        await message.channel.send('> Did somebody mentioned jett? DYK that Jett Lao is the best jett to have ever lived in Southeast asia with a KD of **0.76** and win percentage of **51%** across all maps on Competitive Queue! Checkout his valorant stats here on ** https://tracker.gg/valorant/profile/riot/Ashimoyu%238544/overview **')
    if msg.startswith('$pic'):
        await message.channel.send('Take a look at the best Jett in SEA')
        await message.channel.send(file=discord.File(r'path\pic.png'))

client.run('TOPI_BOT_TOKEN')



