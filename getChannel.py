from telethon import TelegramClient, events
from dotenv import load_dotenv
import os
import logging

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
PHONE = os.getenv("PHONE")


client = TelegramClient("session_name", API_ID, API_HASH)

async def get_channel_id(username):
    try:
        # Fetch the channel entity
        entity = await client.get_entity(username)
        print(f"Channel Name: {entity.title}")
        print(f"Channel ID: {entity.id}")
    except Exception as e:
        print(f"Error fetching channel ID: {e}")

async def main():
    # Add the public username of the Telegram channel
    username = "t.me/zapmyjob"  # Replace with the channel username
    await get_channel_id(username)

# Run the client
with client:
    client.loop.run_until_complete(main())
