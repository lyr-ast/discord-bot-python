import discord
from discord.ext import commands
import json

config = json.load(open("config.json"))

class systems(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member, ctx):
        channel = self.bot.get_channel(config["welcome_channel_id"])

        embed=discord.Embed(title="Pls Read The Rules!!", description="And Enjoy The Server!!", color=0x4965bc)
        embed.set_author(name=f"{member}, Welcome To Our Server!!!", icon_url=member.avatar_url)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text="Created In 2020")
        await channel.send(embed=embed)



    @commands.guild_only()
    @commands.command()
    async def verify(self, ctx):
        if (ctx.channel.id == 768318211573415955):
            for i in ["Member", "Verified"]:
                role = discord.utils.get(ctx.guild.roles, name=i)
                await ctx.author.add_roles(role)
            await ctx.message.delete()
        else:
            return
        
    

def setup(bot):
    bot.add_cog(systems(bot))
