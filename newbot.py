import nextcord
from nextcord.ext import commands,tasks
from nextcord import slash_command,SelectOption
import datetime

import os
intens = nextcord.Intents.all()
intens.members = True 
bot = commands.Bot(command_prefix="!",intents=intens)
for filename in os.listdir("./buttons"):
    if filename.endswith(".py"):
        bot.load_extension(f"buttons.{filename[:-3]}")

bot.run("")