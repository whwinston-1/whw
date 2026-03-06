import asyncio
import os

from telethon import TelegramClient
from telethon.sessions import StringSession


def must_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


async def main() -> None:
    api_id = int(must_env("TG_API_ID"))
    api_hash = must_env("TG_API_HASH")

    client = TelegramClient(StringSession(), api_id, api_hash)
    print("Starting Telegram login in cloud terminal...")
    await client.start()
    session_str = client.session.save()
    print("\n=== COPY THIS TO GITHUB SECRET: TG_SESSION ===")
    print(session_str)
    print("=== END ===\n")
    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
