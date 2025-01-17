import os
from dotenv import load_dotenv
import discord

load_dotenv()

DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")
GUILD_ID = discord.Object(id=int(os.getenv("GUILD")))
