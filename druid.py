#from typing import Optional, Any, Tuple, Union
import discord

class Druidbot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())        

bot = Druidbot()

@bot.event
async def on_ready():
    print("Ready")



