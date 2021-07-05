import discord
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
        await message.channel.send('*Commands are*:\n ** >>> $info\n$topi\n$bakat\n$greet\n$ping**')
    if message.content.startswith('$topi'):
        await message.channel.send('> Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat ~ Topi Bakat')
    if message.content.startswith('$bakat'):
        await message.channel.send(f'> Di diay mu bakat imoha **{message.author.name}?**')
    if message.content.startswith('$info'):
        await message.channel.send('> **Topi Bot was created in honor of our Vietnam War Veteran Brig. General Christopher Lao. '
                                   'The Topi in Topi Bot is derived from Christophers nickname which is kinda lame** *GAMAY OTEN TOPI*')
    if message.content.startswith('$greet'):
        await message.channel.send(f'> Hello {message.author.name}')
    if message.content.startswith('$ping'):
        await message.channel.send(f'> My server latency: **{round(client.latency * 1000)}ms**')
    # if msg.startswith('ggs'):
    #     await message.channel.send(f'> Good Game **{message.author.name}!**  Toms again')
    if msg.startswith('gg'):
        await message.channel.send(f'> Good Game **{message.author.name}!**  Toms again')

# @client.command()
# async def joinVc(ctx):
#     channel = ctx.author.voice.channel
#     await channel.connect()
# @client.event
# async def getName(message):
#     if message.content.startswith('$get'):
#         await message.channel.send("Hello  {ctx.author.name}")

client.run('TOKEN_FOR_BOT')



