import asyncio
from pyrogram import Client, filters

api_id = 32328353
api_hash = "e8af0d96444a0c6d8800bab8d725e80f"

SESSION = "BQJTLScAKfOaC-El5w3RJ5NM7Y8RCzu4O1HXN5SvKdVZe3UAKFSssdAG2ja4QaxYyzE8jKKM53htYF18KQpMBOffvCFIzmHCF3DpfkPRtXJpWLIBoEJndSuCkjyFV1g09NKtqWuo_nqAM69uKSN6iipw1p0hpjubOtR2OMR4BYOMz08qxQnKZ9c5p_KkjAfPYYj0-qL3TbAL6Zaq54Qjvn3hZWFzkj2B0YNpTtCnJ6svfvLXClNVuOdtnqrv6J9nQT4_jveTWvFJyw_rzOnJNY7suYsD1Y_U5XFs8aTpAKv5Qbxmaa-zeEtBSZPRRe-zm40oWLUeGNDmfmgCGYnbvkC1Cr_PZgAAAAIKSZQTAA"
OWNER_ID = 7724452546

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
    session_string=SESSION
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

# ✅ Changed from filters.me to checking user ID in the function
@app.on_message(filters.command("f", prefixes="."))
async def sequence_handler(client, message):
    # Check if the command sender is the owner
    if message.from_user.id != OWNER_ID:
        return

    if not message.reply_to_message:
        await message.reply("Reply to a message first.")
        return

    reply_id = message.reply_to_message.id

    # Try to delete command message (might fail if no permissions)
    try:
        await message.delete()
    except:
        pass  # Ignore deletion errors

    for msg in MESSAGES:
        await client.send_message(
            chat_id=message.chat.id,
            text=msg,
            reply_to_message_id=reply_id
        )
        await asyncio.sleep(DELAY)

# Optional: Add a test command to check if bot is working
@app.on_message(filters.command("ping", prefixes="."))
async def ping_handler(client, message):
    if message.from_user.id != OWNER_ID:
        return
    await message.reply("Pong! Bot is working!")

print(BANNER)
print("Bot is starting...")
print(f"Owner ID: {OWNER_ID}")
print("Commands: .f (reply to a message) or .ping")
app.run()
