import discord
from discord.ext import commands


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    async def mute(self, ctx, user : discord.Member):
        if ctx.author == user:
            await ctx.send("You can't mute yourself")
        for channel in ctx.message.guild.channels:
            if type(channel) != discord.channel.TextChannel:
                continue
            overwrites = channel.overwrites_for(user)
            overwrites.send_messages = False
            await channel.set_permissions(user, overwrite=overwrites)
    

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    async def unmute(self, ctx, user : discord.Member):
        for channel in ctx.message.guild.channels:
            if type(channel) != discord.channel.TextChannel:
                continue
            overwrites = channel.overwrites_for(user)
            overwrites.send_messages = None
            await channel.set_permissions(user, overwrite=overwrites)




    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason="unspecified reason"):
        embed=discord.Embed(title=f"{member.mention} You Have Been Kicked From The Server By {ctx.author} for {reason}", color=0x6380c5)
        embed.set_author(name=f"Kicked {member}", icon_url="https://i.imgur.com/n9l4wht.jpg")
        await member.send(embed=embed)
        await member.kick(reason=reason)

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason="unspecified reason"):
        embed=discord.Embed(title=f"{member.mention} You Have Been banned From The Server By {ctx.author} for {reason}", color=0x6380c5)
        embed.set_author(name=f"Kicked {member}", icon_url="https://i.imgur.com/n9l4wht.jpg")
        await member.send(embed=embed)
        await member.kick(reason=reason)

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages=True)
    async def clear(self, ctx, num : int):
        channel = ctx.message.channel
        await ctx.message.delete()
        await channel.purge(limit=num, check=None, before=None)
        embed=discord.Embed(title=f"cleared {num} messages ", color=0x6380c5)
        embed.set_footer(text=f"command requested by {ctx.author}")
        await ctx.send(embed=embed)


    @commands.command()
    @commands.guild_only()
    async def userinfo(self, ctx, member : discord.Member):

        embed=discord.Embed()
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="name and id", value=f"{member} has id\n {member.id}", inline=True)
        embed.add_field(name="roles", value=", ".join([i.name for i in member.roles]) , inline=True)
        embed.add_field(name="warnings", value="warns", inline=False)
        embed.add_field(name="joined server at", value=member.joined_at.strftime("%A, %B %d %Y \n %H:%M %p"), inline=True)
        embed.add_field(name="joined discord at", value=member.created_at.strftime("%A, %B %d %Y \n %H:%M %p"), inline=True)
        embed.set_footer(text=f"requested by {ctx.author.name} | {ctx.author.id}")
        await ctx.send(embed=embed)

    @userinfo
    @clear.error
    @ban.error
    @kick.error
    @mute.error
    @unmute.error
    async def on_command_error(self, ctx, error):

        if isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(title="You don't have the permission to do this command")
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed=discord.Embed(title="Bad Argument")
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(title="Missing Arguments")
            await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(help(bot))