import discord
from discord.ext import commands
import json


config = json.load(open("config.json"))
class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(ignore_extra=False)

    async def help(self, ctx, name=None):
        if name == None:        
            embed=discord.Embed(title="Prefix: " + config["prefix"], color=0xa7c1dd)
            embed.set_author(name="Help Commands:")
            embed.set_thumbnail(url="https://i.imgur.com/n9l4wht.jpg")
            embed.add_field(name="Info", value="Info about bot and this server", inline=False)
            embed.add_field(name="Roll" , value="Rolls a dice", inline=False)
            embed.add_field(name="Rps <rock, paper or scissor>" , value="plays Rock Paper Scissors with you", inline=False)
            embed.add_field(name="8ball <question>" , value="answers your questions for you", inline=False)
            await ctx.send(embed=embed)
        elif name == "staff":
            embed=discord.Embed(title="Prefix: " + config["prefix"])
            embed.set_author(name="Help Mod commands")
            embed.set_thumbnail(url=ctx.guild.icon_url)
            embed.add_field(name="clear <num of messages>", value="clears the number of messages given", inline=True)
            embed.add_field(name="mute <@user>", value="mutes the user ", inline=True)
            embed.add_field(name="unmute <@user>", value="unmutes the user", inline=True)
            embed.add_field(name="kick <@user>", value="kicks the user", inline=True)
            embed.add_field(name="ban <@user>", value="bans the user", inline=True)
            embed.add_field(name="lock <#channel name>", value="locks the channel", inline=True)
            embed.add_field(name="unlock <#channel name>", value="unlocks the channel", inline=True)
            embed.add_field(name="ignore <#channel name>", value="ignores the channel for commands", inline=True)
            embed.set_footer(text="Made by not a bot and hosted by Hyper")
            await ctx.send(embed=embed)







def setup(bot):
    bot.add_cog(help(bot))