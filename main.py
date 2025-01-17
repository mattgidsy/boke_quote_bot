import discord
from discord import app_commands
import os
from functions import bot
import settings

#syncs tree/commands to bot, sets Discord status
@bot.event
async def on_ready():
        print(f"Bot User: {bot.user}")
        print(f"Bot Id: {bot.user.id}")
        print(f"Bot Guild ID:{bot.guilds[0].id}")
        print("____________________")
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='/ping')) 
        
        #update slash commands
        bot.tree.copy_global_to(guild=settings.GUILD_ID)
        await bot.tree.sync(guild=settings.GUILD_ID)
        # await ctx.send(f"{user_name}, I have requested to sync with the hive.", ephemeral=True)
        print('--roboke Systems Engaged--')


if __name__ == "__main__":
    # Run the bot
    TOKEN = settings.DISCORD_API_SECRET
    bot.run(TOKEN)
