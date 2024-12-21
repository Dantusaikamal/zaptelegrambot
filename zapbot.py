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
DESTINATION_CHAT_ID = os.getenv("DESTINATION_CHAT_ID")  # Automatically converts to a string

# Source group/chat IDs
SOURCE_CHAT_IDS = [-1502415672, -2059091493, -1002396647930]

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

@client.on(events.NewMessage(chats=SOURCE_CHAT_IDS))
async def forward_message(event):
    """Forward messages from source chats to the destination channel with a custom footer."""
    try:
        if event.message.message:  # Ensure the message has text
            custom_message = event.message.message + FOOTER
            await client.send_message(DESTINATION_CHAT_ID, custom_message)
            logger.info(f"Forwarded text message from {event.chat_id} to {DESTINATION_CHAT_ID}")
        else:
            # Forward non-text messages (e.g., media) directly
            await client.forward_messages(DESTINATION_CHAT_ID, event.message)
            logger.info(f"Forwarded non-text message from {event.chat_id} to {DESTINATION_CHAT_ID}")
    except Exception as e:
        logger.error(f"Error while forwarding message from {event.chat_id}: {e}")

def main():
    """Main function to start the bot."""
    try:
        client.start(phone=PHONE)
        logger.info("Bot is running and listening for new messages...")
        client.run_until_disconnected()
    except Exception as e:
        logger.critical(f"Critical error: {e}")

if __name__ == "__main__":
    main()
