import asyncio

from pytgcalls import idle

from config import SUPPORT, bot
from config import call_py
from Userbot.quote import arq


async def main():
    await call_py.start()
    await bot.join_chat("v3nom_support")            
    await bot.send_message(
            SUPPORT,
            "<b>Congrats!! Music Bot has started successfully!</b>",
        )
    print(
        """
    ------------------
   | Userbot Started! POWERED BY @V3N0M_0P |
    ------------------
"""
    )
    await idle()
    await arq.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
