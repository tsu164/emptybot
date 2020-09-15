from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_ready():
    print('on_ready')

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.event
async def on_message(message):
    #bot相手なら無視
    if message.author == bot.user:
        return
    if message.content == 'ローソン':
        await message.channel.send('行け')
    if message.content == 'からあげクン':
        await message channel.send('食え')
    poops = ['うんこ', 'うんち' , 'ウンコ' , 'ウンチ', '糞']
    for poop in poops:
        if poop in message.content:
            await message.add_reaction(':poop:')

@bot.event
async def on_guild_join(guild):
    await after.edit(nick = 'はみるとん')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
