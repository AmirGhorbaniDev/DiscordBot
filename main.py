# Import necessary libraries
import discord
from discord.ext import commands

# Set up the bot
intents = discord.Intents.default()
intents.members = True  # Enable the 'members' intent to detect new member events
bot = commands.Bot(command_prefix="!", intents=intents)

# Add your bot token here (replace with your actual token)
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

# Event: When a new member joins a server
@bot.event
async def on_member_join(member):
    try:
        # Define the welcome message
        welcome_message = (
            f"Hi {member.name}, welcome to {member.guild.name}!"
            "\nWe're glad to have you here. 🎉"
        )
        # Send the welcome message as a direct message
        await member.send(welcome_message)
        print(f"Welcome message sent to {member.name}")
    except Exception as e:
        print(f"Failed to send welcome message to {member.name}: {e}")

# Run the bot
bot.run(BOT_TOKEN)
