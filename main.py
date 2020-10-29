from discord.ext import commands
import discord
import json
import os



config = json.load(open("config.json"))
bot = commands.Bot(command_prefix=config["prefix"], help_command=None, case_insensitive=True)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}#{bot.user.discriminator}")
    print(f"")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="to u!help | Galaxy Utilities "))

@bot.event
async def on_message(message):
    if message.channel.id in config["Ignored"]:
        return
    elif message.author == bot.user:
        return

    await bot.process_commands(message)



for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        try:
            bot.load_extension(f"cogs.{file[:-3]}")
            print(f"{file} is loaded")
        except:
            print(f"Error occured while loading {file}")



#bot.run(config["token"])
bot.run(os.environ["token"])
