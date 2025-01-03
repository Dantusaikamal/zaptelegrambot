from flask import Flask
from telethon import TelegramClient, events
from dotenv import load_dotenv
import os
import logging
import threading

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
PHONE = os.getenv("PHONE")
DESTINATION_CHAT_ID = os.getenv("DESTINATION_CHAT_ID")  # Get as string
try:
    # Attempt to convert to integer if it's a numeric ID
    DESTINATION_CHAT_ID = int(DESTINATION_CHAT_ID)
except ValueError:
    # Keep as string if it's a username
    pass

SOURCE_CHAT_IDS = list(map(int, os.getenv("SOURCE_CHAT_IDS", "").split(",")))  # Parse IDs dynamically

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

def start_bot():
    """Starts the Telegram bot."""
    try:
        client.start(phone=PHONE)
        logger.info("Telegram bot started successfully!")
        client.run_until_disconnected()
    except Exception as e:
        logger.critical(f"Critical error in bot: {e}")

if __name__ == "__main__":
    # Run the Telegram bot in a separate thread
    bot_thread = threading.Thread(target=start_bot, daemon=True)
    bot_thread.start()

    # Run the Flask app to bind to a port
    app.run(host="0.0.0.0", port=5000)
