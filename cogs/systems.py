import discord
from discord.ext import commands
import json

config = json.load(open("config.json"))

class systems(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(config["welcome_channel_id"])

        embed=discord.Embed(title="Pls Read The Rules!!", description="And Enjoy The Server!!", color=0x4965bc)
        embed.set_author(name=f"{member}, Welcome To Our Server!!!", icon_url=member.avatar_url)
        embed.set_thumbnail(url="https://i.imgur.com/n9l4wht.jpg")
        embed.set_footer(text="Created In 2020")
        await channel.send(embed=embed)





def setup(bot):
    bot.add_cog(systems(bot))