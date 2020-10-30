import discord
from discord.ext import commands
import random
import asyncio

class members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.guild_only()
    @commands.command(ignore_extra=False)
    async def serverinfo(self, ctx):
        embed=discord.Embed(title=f"ID: {ctx.guild.id}")
        embed.set_author(name=ctx.guild.name)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="members", value=ctx.guild.member_count, inline=True)
        embed.add_field(name="Region", value=ctx.guild.region, inline=True)
        embed.add_field(name="Channels", value=f"Categories {len(ctx.guild.categories)} \nText: {len(ctx.guild.text_channels)}\n Voice: {len(ctx.guild.voice_channels)}", inline=False)
        embed.add_field(name="Owner", value=ctx.guild.owner, inline=False)
        embed.add_field(name="created on", value=ctx.guild.created_at.strftime("%A, %B %d %Y \n %H:%M %p"), inline=False)
        embed.add_field(name="boosts", value=ctx.guild.premium_subscription_count, inline=True)
        await ctx.send(embed=embed)

    
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

    @commands.guild_only()
    @commands.command(name="8ball")
    async def _8ball(self, ctx, *, question=None):
        if question == None:
            return await ctx.send("You didn't specify a question")
           
        responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
               "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
               "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
               "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
               "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]


        ball_res = random.choice(responses)
        await ctx.send(ball_res)

def setup(bot):
    bot.add_cog(members(bot))
