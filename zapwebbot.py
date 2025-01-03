from flask import Flask
from telethon import TelegramClient, events
from dotenv import load_dotenv
import asyncio
import os
import logging
import threading

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
PHONE = os.getenv("PHONE")
DESTINATION_CHAT_ID = os.getenv("DESTINATION_CHAT_ID")  # Can be username or channel ID
SOURCE_CHAT_IDS = list(map(int, os.getenv("SOURCE_CHAT_IDS", "").split(",")))

# Custom footer to add to forwarded messages
FOOTER = "\n\n🔗 Powered by ZapMyJob"

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialize the Telegram client
client = TelegramClient("forwarder_session", API_ID, API_HASH)

# Flask app for keeping Render instance alive
app = Flask(__name__)

@app.route("/")
def home():
    return "ZapMyJob Bot is running and ready!"

@client.on(events.NewMessage(chats=SOURCE_CHAT_IDS))
async def forward_message(event):
    """Forward messages from source chats to the destination channel with a custom footer."""
    try:
        if event.message.message:  # If the message contains text
            custom_message = event.message.message + FOOTER
            await client.send_message(DESTINATION_CHAT_ID, custom_message)
            logger.info(f"Forwarded text message from {event.chat_id} to {DESTINATION_CHAT_ID}")
        else:  # Non-text messages (e.g., media)
            await client.forward_messages(DESTINATION_CHAT_ID, event.message)
            logger.info(f"Forwarded non-text message from {event.chat_id} to {DESTINATION_CHAT_ID}")
    except Exception as e:
        logger.error(f"Error while forwarding message from {event.chat_id}: {e}")

async def start_bot():
    """Starts the Telegram bot."""
    try:
        await client.start(phone=PHONE)
        logger.info("Telegram bot started successfully!")
        await client.run_until_disconnected()
    except Exception as e:
        logger.critical(f"Critical error in bot: {e}")

if __name__ == "__main__":
    # Run the Telegram bot in a separate thread with an asyncio loop
    def run_bot():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(start_bot())

    # Start the bot in a separate thread
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()

    # Use the Render-assigned port for the Flask server
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port)
