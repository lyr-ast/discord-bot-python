import discord
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.has_guild_permissions(administrator=True)
    @commands.command()
    async def reload(self, ctx, extension=None):
        if extension == None:
            return await ctx.send("You haven't mentioned any cog to reload")
        try:
            self.bot.reload_extension(f"cogs.{extension}")
            await ctx.send(f"{extension} was succesfully reloaded")
        except:
            await ctx.send("A error occured while reloading the cog")

    @commands.has_guild_permissions(administrator=True)
    @commands.command()
    async def load(self, ctx, extension=None):
        if extension == None:
            return await ctx.send("You haven't mentioned any cog to load")
        try:
            self.bot.load_extension(f"cogs.{extension}")
            await ctx.send(f"{extension} was succesfully loaded")
        except:
            await ctx.send("A error occured while loading the cog")

    @commands.has_guild_permissions(administrator=True)
    @commands.command()
    async def unload(self, ctx, extension=None):
        if extension == None:
            return await ctx.send("You haven't mentioned any cog to unload")
        try:
            if extension == "admin":
                return await ctx.send("You can't unload this cog as its the admin cog")
            self.bot.unload_extension(f"cogs.{extension}")
            await ctx.send(f"{extension} was succesfully unloaded")

        except:
            await ctx.send("A error occured while unloading the cog")


def setup(bot):
    bot.add_cog(Admin(bot))