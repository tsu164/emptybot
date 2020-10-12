from discord.ext import commands
import random

class Gacha(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gacha(self, ctx, category, count: int):
        with open(f"../list/{category}.txt") as f:
            category_contents = [s.strip() for s in f.readlines()]
        for i in range(count):
            await ctx.send(random.choice(category_contents))

    @gacha.error
    async def gacha(self, ctx, error):
        if isinstance(error, commands.errors.BadArgument):
            await ctx.send("数字で言って！")
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("そんなガチャないよ")

def setup(bot):
    bot.add_cog(Gacha(bot))
