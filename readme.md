# 🚀 **ZapMyJob Forwarder Bot**

<p align="center">
  <img src="https://github.com/Dantusaikamal/zaptelegrambot/blob/main/zap.jpg" alt="Bot Image" width="300">
</p>

> **Your automated job forwarder bot!**  
> This bot forwards messages from selected Telegram groups or channels into your own group/channel, making job hunting easier for your audience. Customize it with a footer, filters, and more!

---

## 🎯 **Features**

- 🌟 **Forward Messages**: Automatically forwards messages from source groups/channels to a destination.
- 📝 **Custom Footer**: Adds a branded footer (e.g., "🔗 Powered by ZapMyJob") to forwarded messages.
- 🔍 **Text & Media**: Handles both text and media messages seamlessly.
- 🚦 **Real-Time Updates**: Works in real time, keeping your destination group/channel updated.
- 🛡️ **Error Handling**: Logs errors to ensure smooth operation.

---

## 🛠️ **Setup Instructions**

Follow these steps to get the bot up and running:

### 1️⃣ **Prerequisites**

- Python 3.7+ installed on your system
- Telegram API credentials:
  - Get `API_ID` and `API_HASH` from [Telegram API](https://my.telegram.org/).

### 2️⃣ **Clone the Repository**

```bash
git clone https://github.com/yourusername/zaptelegrambot.git
cd zaptelegrambot
```

### 3️⃣ Install Dependencies

```bash
pip install telethon python-dotenv
```

### 4️⃣ Configure Environment Variables

- Create a .env file in the project root and add your credentials:

```bash
API_ID=your_api_id
API_HASH=your_api_hash
PHONE=your_phone_number
DESTINATION_CHAT_ID=your_destination_id
```

### 5️⃣ Run the Bot

- Start the bot by running the script:

```bash
python zapbot.py
```

## 🧑‍💻 Usage

- Join Source Groups/Channels: Add your bot or Telegram account to the groups/channels you want to monitor.

- Add Source Group IDs: Use tools like IDBot or the Telethon script to fetch group/channel IDs, Update SOURCE_CHAT_IDS in the code with these IDs.

- Forward Messages: The bot will listen for new messages in the source groups/channels and forward them to the destination with a custom footer.

## ✨ Show Your Support

- If this project helped you, please give it a ⭐️ on GitHub and share it with others!

## 📄 License

- This project is licensed under the MIT License. Feel free to use, modify, and distribute!
