from discord.ext import commands
import random

class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def slot(self, ctx, latch=1):
        """スロットを回そう"""
        if letch > 1000000:
            return await ctx.send("破滅すな")
        if letch <= 0:
            return await ctx.send("ムチャ言うな")
        results = []
        icons = ["🐔", "🐤", "🥚", "🍗", "🍳", "🈚", "💩"]
        rand = random.randint(1, 1000)
        # 1%🐔
        if rand <= 10:
            results = icons[0] * 3
            win = 10 * latch
        # 2.5%🐤
        elif rand <= 35:
            results = icons[1] * 3
            win = 8 * latch
        # 3%🥚
        elif rand <= 65:
            results = icons[2] * 3
            win = 5 * latch
        # 5%🍗
        elif rand <= 115:
            results = icons[3] * 3
            win = 2 * latch
        # 8%🍳
        elif rand <= 195:
            results = icons[4] * 3
            win = 1 * latch
        # 10%🈚
        elif rand <= 295:
            results = icons[5] * 3
            win = 0
        # 12.5%💩
        elif rand <= 420:
            results = icons[6] * 3
            win = (-1) * latch
        # スカ
        else:
            results.append(random.choice(icons))
            results.append(random.choice(icons))
            # 当たりにしない
            if results[0] == results[1]:
                icons.remove(results[0])
            results.append(random.choice(icons))
            win = 0
        # スロットの表示
        slots = "❓" * 3
        message = await ctx.send(" ".join(slots))
        i = 0
        while i < 3:
            slots[i] = results[i]
            slot_results = " ".join(slots)
            await message.edit(content=slot_results, delete_after=1)
            i += 1
        await ctx.send(f"{latch}円賭けて、{win}円になりました。")

    @slot.error
    async def slot_error(self, ctx, error):
        if isinstance(error, commands.errors.BadArgument):
            await ctx.send("数字で言って！")

def setup(bot):
    bot.add_cog(Gamble(bot))
