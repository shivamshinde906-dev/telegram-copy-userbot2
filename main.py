import asyncio
from telethon import TelegramClient, events

# ----------------------------
api_id = 31837772        # Replace with your api_id
api_hash = "2a58f29db0c2e645c45d2f3b3775ade8"  # Replace with your api_hash

SOURCE_GROUP = "@approveccigcc"   # Replace with your source group
TARGET_GROUP = "https://t.me/+alkRKOqrvsAzZDQ1" # Replace with your target group

# ----------------------------
client = TelegramClient('user_session', api_id, api_hash)

# ----------------------------
@client.on(events.NewMessage(chats=SOURCE_GROUP))
@client.on(events.MessageEdited(chats=SOURCE_GROUP))
async def copy_and_reformat(event):
    message = event.message
    text = message.text or ""

    # Only process approved messages (simple filter)
    if "Approved" in text or "approved" in text:
        # Example parsing (customize depending on your message)
        lines = text.splitlines()
        cc = lines[0].split(":")[-1].strip() if len(lines) > 0 else "N/A"
        response = lines[1].split(":")[-1].strip() if len(lines) > 1 else "N/A"
        gateway = lines[2].split(":")[-1].strip() if len(lines) > 2 else "N/A"
        bank = lines[3].split(":")[-1].strip() if len(lines) > 3 else "N/A"
        category = lines[4].split(":")[-1].strip() if len(lines) > 4 else "N/A"
        type_ = lines[5].split(":")[-1].strip() if len(lines) > 5 else "N/A"
        country = lines[6].split(":")[-1].strip() if len(lines) > 6 else ""
        took = lines[7].split(":")[-1].strip() if len(lines) > 7 else "N/A"

        formatted_message = f"""
CC: {cc}
Status: Approved ✅
Response: {response}
Gateway: {gateway}
Bank: {bank}
Category: {category}
Type: {type_}
Country: {country}
Took: {took}
Checked by: 𝗧𝗢𝗠_ ⋆⃝🇮🇳 ┈➤ [5758032952]
""".strip()

        # Send formatted message to target group
        await client.send_message(TARGET_GROUP, formatted_message)
        print(f"Copied & reformatted message ID {message.id}")

# ----------------------------
async def main():
    await client.start()
    print("Bot is running...")
    await asyncio.Event().wait()

# ----------------------------
if __name__ == "__main__":
    asyncio.run(main())
