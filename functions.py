import discord
import settings
from discord import app_commands
from discord.ext import commands


intents = discord.Intents.all()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix= "!", intents=intents)

q_list = []

# # bot console log
# @bot.event
# async def on_ready():
#     print(f"Bot User: {bot.user}")
#     print(f"Bot Id: {bot.user.id}")
#     print(f"Bot Guild ID:{bot.guilds[0].id}")
#     print("____________________")
#     await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='/ping')) 
    
#     #update slash commands
#     bot.tree.copy_global_to(guild=settings.GUILD_ID)
#     await bot.tree.sync(guild=settings.GUILD_ID)
#     # await ctx.send(f"{user_name}, I have requested to sync with the hive.", ephemeral=True)
    
@bot.hybrid_command(
    help = "ping pong test",
    description = "respond with pong when pinged"
)
async def ping(ctx):
    await ctx.send("pong")
    
#boke quote hybrid command         
@bot.hybrid_command(
    help = "submit a quote",
    description = "type a quote and who said it" 
)
async def quote(ctx, speaker, quote):
    await ctx.send( f"{ctx.author.name} submitted a quote: \n{quote}")
    q_list.append(f"{ctx.author.name} | {speaker} | {quote}")
    print("quote submitted")
    print(f"current list:\n{q_list}")
    

#testing Bryce's poll 
@bot.tree.command(
    name="poll",
    description="Start a poll!",
    guild=settings.GUILD_ID
    )
async def poll(interaction, question: str, option1: str, option2: str):
    """
    Creates a poll with two options.
    """
    embed = discord.Embed(
        title="📊 Poll",
        description=question,
        color=discord.Color.blue()
    )
    embed.add_field(name="Option 1", value=f"👍 {option1}", inline=False)
    embed.add_field(name="Option 2", value=f"👎 {option2}", inline=False)
    embed.set_footer(text=f"Poll started by {interaction.user.display_name}")

    # Defer the response and send the embed
    await interaction.response.defer()  # Defer the response to allow message editing
    poll_message = await interaction.followup.send(embed=embed, wait=True)

    # Add reactions to the poll message
    await poll_message.add_reaction("👍")
    await poll_message.add_reaction("👎")
    
    
@bot.command(hidden=True)
async def bokesync(ctx):
    user_id = ctx.author.id
    owner_id = ctx.guild.owner_id
    user_name = ctx.author.name
    if user_id == owner_id:
        bot.tree.copy_global_to(guild=settings.GUILD_ID)
        await bot.tree.sync(guild=settings.GUILD_ID)
        await ctx.send(f"{user_name}, I have requested to sync with the hive.", ephemeral=True)
    else:
        await ctx.send(f"Sorry, {user_name}, you don't have permission to use that command.\n Dad doesn't want to get rate limited.")
    

