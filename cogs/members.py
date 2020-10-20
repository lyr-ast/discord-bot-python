import discord
from discord.ext import commands
import random
import asyncio

class members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.command(ignore_extra=False)
    async def info(self, ctx):
        embed=discord.Embed(color=0xa7c1dd)
        embed.set_author(name="Info")
        embed.set_thumbnail(url="https://i.imgur.com/n9l4wht.jpg")
        embed.add_field(name="Hypers Galaxy Info:", value="Hypers Galaxy Is A Chill Server For Everyone To Enjoy!! ", inline=False)
        embed.add_field(name="Bot Made By not a bot", value="And Hosted By Hyper", inline=False)
        embed.set_footer(text="Created in 2020")
        await ctx.send(embed=embed)

    @commands.guild_only()
    @commands.command(ignore_extra=False)
    async def serverinfo(self, ctx):
        pass
    
    @commands.guild_only()
    @commands.command(ignore_extra=False)
    async def rps(self, ctx, name=None):
        #name = name.lower()
        moves = ["rock", "paper", "scissor"]
        if name != None:
            name = name.lower()
        if name == None or name not in moves:
            return await ctx.send("Please enter a valid option")
        
        bot_move = random.choice(moves)
        await ctx.send(f"bot has choosen {bot_move}")

        if bot_move == name:
            await ctx.send(f"{ctx.author.mention} Its a Tie!")

        elif name == "rock":
            if bot_move == "paper":
                await ctx.send(f"{ctx.author.mention}, You lose")
            else:
                await ctx.send(f"{ctx.author.mention}, You win")

        elif name == "paper":
            if bot_move == "scissor":
                await ctx.send(f"{ctx.author.mention}, You lose")
            else:
                await ctx.send(f"{ctx.author.mention}, You win")
        
        elif name == "scissor":
            if bot_move == "rock":
                await ctx.send(f"{ctx.author.mention}, You lose")
            else:
                await ctx.send(f"{ctx.author.mention}, You win")
        
        else:
            await ctx.send("A error occured while playing")


    @commands.guild_only()
    @commands.command(ignore_extra=False)
    async def roll(self, ctx):
        num = random.randint(1, 6)
        mes = await ctx.send("Rolling....")
        await asyncio.sleep(1)
        await mes.edit(content=f"Your number is {num}")


    @commands.command(name="8ball")
    async def _8ball(self, ctx, *, question=None):
        if question == None:
            await ctx.send("please type your question")
        responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
               "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
               "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
               "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
               "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]


        ball_res = random.choice(responses)
        await ctx.send(ball_res)

def setup(bot):
    bot.add_cog(members(bot))