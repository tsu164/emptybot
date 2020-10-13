from discord.ext import commands
import random

gacha_list = ["alcohol", "drink", "food", "konbini", "misosoup", "shop", "sweets", "tsumami"]

class GachaSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gacha(self, ctx, category, count=1):
        """ガチャができます
        alcohol, drink, food, konbini, misosoup, shop, sweets, tsumami
        数字でいくつか指定できます"""
        try:
            if count == 0 or count > 10:
                return await ctx.send("ムチャ言うな")
            with open(f"/app/list/{category}.txt") as f:
                category_contents = [s.strip() for s in f.readlines()]
            await ctx.send(" ".join(random.sample(category_contents, count)))

        except FileNotFoundError:
            return await ctx.send("そんなガチャないよ")

    @gacha.error
    async def gacha_error(self, ctx, error):
        if isinstance(error, commands.errors.BadArgument):
            await ctx.send("数字で言って！")
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("なんのガチャ？")

    @commands.command()
    async def dice(self, ctx, num_max: int, num_min=1):
        """好きな多面体と数字のサイコロふれます"""
        await ctx.send(random.randint(num_min, num_max))

    @dice.error
    async def dice_error(self, ctx, error):
        if isinstance(error, commands.errors.BadArgument):
            await ctx.send("数字で言って！")
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("どんなサイコロ？")

def setup(bot):
    bot.add_cog(GachaSystem(bot))
