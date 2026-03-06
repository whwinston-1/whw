import asyncio
import os
import sys

from telethon import TelegramClient
from telethon.sessions import StringSession


def must_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


async def run() -> None:
    api_id = int(must_env("TG_API_ID"))
    api_hash = must_env("TG_API_HASH")
    session_str = must_env("TG_SESSION")
    target = must_env("TG_TARGET")
    sign_text = must_env("TG_SIGN_TEXT")

    client = TelegramClient(StringSession(session_str), api_id, api_hash)
    await client.connect()
    if not await client.is_user_authorized():
        raise RuntimeError("Session is not authorized. Re-generate TG_SESSION.")

    await client.send_message(target, sign_text)
    print(f"Sent sign message to {target}.")
    await client.disconnect()


if __name__ == "__main__":
    try:
        asyncio.run(run())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
