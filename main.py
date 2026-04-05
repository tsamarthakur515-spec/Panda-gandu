import asyncio
import sys
import logging
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

# Disable annoying logs
logging.basicConfig(level=logging.ERROR)

api_id = 32328353
api_hash = "e8af0d96444a0c6d8800bab8d725e80f"

SESSION = "BQJTLScAKfOaC-El5w3RJ5NM7Y8RCzu4O1HXN5SvKdVZe3UAKFSssdAG2ja4QaxYyzE8jKKM53htYF18KQpMBOffvCFIzmHCF3DpfkPRtXJpWLIBoEJndSuCkjyFV1g09NKtqWuo_nqAM69uKSN6iipw1p0hpjubOtR2OMR4BYOMz08qxQnKZ9c5p_KkjAfPYYj0-qL3TbAL6Zaq54Qjvn3hZWFzkj2B0YNpTtCnJ6svfvLXClNVuOdtnqrv6J9nQT4_jveTWvFJyw_rzOnJNY7suYsD1Y_U5XFs8aTpAKv5Qbxmaa-zeEtBSZPRRe-zm40oWLUeGNDmfmgCGYnbvkC1Cr_PZgAAAAIKSZQTAA"
OWNER_ID = 7450385463

BANNER = """
\033[1;36m
 ____    _    __  __    _    ____    _____ ___ ____ _   _ _____ _____ ____
/ ___|  / \  |  \/  |  / \  |  _ \  |  ___|_ _/ ___| | | |_   _| ____|  _ \\
\___ \\ / _ \\ | |\/| | / _ \\ | |_) | | |_   | | |  _| |_| | | | |  _| | |_) |
 ___) | / ___ \\| |  | |/ ___ \\|  _ <  |  _|  | | |_| |  _  | | | | |___|  _ <
|____/ /_/   \\_\\_|  |_/_/   \\_\\_| \\_\\ |_|   |___\\____|_| |_| |_| |_____|_| \\_\\
\033[0m
\033[1;35m
 Pyrogram Userbot Started
\033[0m
"""

app = Client(
    name="userbot",
    api_id=api_id,
    api_hash=api_hash,
    session_string=SESSION,
    workdir="."
)

MESSAGES = [
    "TERI", "MAA", "KE", "ME", "BOMB", "TAPA", "TAP", "TU", "KASA", "MAA",
    "KA", "DAGAD", "DALLI", "MAA", "KA", "BACHA", "TERI", "MAA", "KE", "PE",
    "BAJA", "DUNGA", "MAA", "KE", "BACHA", "TERI", "BHEN", "KI", "ME", "MOMOS",
    "KI", "CHUTNEY", "DALKA", "PIJAUNGA", "TERI", "MAA KI", "ME", "WINE",
    "DALKA", "PIJAUNGA", "TERI", "MAA", "SE", "CUDWADUNGA", "TERI", "BHEN",
    "KO", "LEJAKA", "CODUNGA", "TERI", "MA", "GHODI", "BNAKA", "CHOMDUNGA",
    "TERI", "MAA", "K", "PE", "LODA", "MARKA", "CODUNGA", "TERI", "MOSI",
    "KO", "KUTTIYA", "BNAKA", "COHDONGA", "TERI", "MAA", "KO", "PGL", "KRDUNGA",
    "TERE", "PE", "LODA", "MARKA", "CODUNGA", "TERI", "MAA", "KO", "GANJA",
    "PIKA", "CODUNGA", "TMKC", "PE CHAPAL", "MARUNGA"
]

DELAY = 0.0

# Global flags
is_stopping = False
is_processing = False

@app.on_message(filters.command("f", prefixes="."))
async def sequence_handler(client, message):
    global is_stopping, is_processing

    # Check if the command sender is the owner
    if message.from_user.id != OWNER_ID:
        return

    # Prevent multiple simultaneous sequences
    if is_processing:
        await message.reply("⚠️ Already processing a sequence. Please wait.")
        return

    if not message.reply_to_message:
        await message.reply("Reply to a message first.")
        return

    is_processing = True
    reply_id = message.reply_to_message.id

    # Try to delete command message
    try:
        await message.delete()
    except:
        pass

    try:
        for msg in MESSAGES:
            # Check if stop command was issued
            if is_stopping:
                await client.send_message(message.chat.id, "⚠️ Stopped by user command.")
                is_stopping = False
                break

            try:
                await client.send_message(
                    chat_id=message.chat.id,
                    text=msg,
                    reply_to_message_id=reply_id
                )
                await asyncio.sleep(DELAY)
            except FloodWait as e:
                await asyncio.sleep(e.value)
                await client.send_message(
                    chat_id=message.chat.id,
                    text=msg,
                    reply_to_message_id=reply_id
                )
            except Exception as e:
                print(f"Error sending message: {e}")
                continue
    finally:
        is_processing = False

@app.on_message(filters.command("ping", prefixes="."))
async def ping_handler(client, message):
    if message.from_user.id != OWNER_ID:
        return
    await message.reply("Pong! Bot is working!")

@app.on_message(filters.command("stop", prefixes="."))
async def stop_handler(client, message):
    global is_stopping, is_processing

    if message.from_user.id != OWNER_ID:
        return

    is_stopping = True

    # Wait for current sequence to finish if any
    if is_processing:
        await message.reply("🛑 Stopping after current sequence...")
    else:
        await message.reply("🛑 Bot is stopping... Goodbye!")
        await asyncio.sleep(1)
        await client.stop()
        sys.exit(0)

print(BANNER)
print("Bot is starting...")
print(f"Owner ID: {OWNER_ID}")
print("Commands:")
print("  .f (reply to a message) - Send sequence of messages")
print("  .ping - Check if bot is working")
print("  .stop - Stop the bot completely")
print("\nNote: Ignore any 'Peer id invalid' errors - they are harmless")

# Run the bot
try:
    app.run()
except KeyboardInterrupt:
    print("\nBot stopped by user")
    sys.exit(0)
except Exception as e:
    print(f"Fatal error: {e}")
    sys.exit(1)
