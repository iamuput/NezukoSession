import env
import logging
from pyrogram import Client, idle
from pyromod import listen
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid


logging.basicConfig(level=logging.INFO, encoding="utf-8", format="%(asctime)s - %(levelname)s - \033[32m%(pathname)s: \033[31m\033[1m%(message)s \033[0m")

Auput = Client(
    "NezukoSession",
    api_id=env.API_ID,
    api_hash=env.API_HASH,
    bot_token=env.BOT_TOKEN,
    in_memory=True,
    plugins={'root':'AuputSession'},
)


if __name__ == "__main__":
    logging.info("Starting the bot")
    try:
        Auput.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = Auput.me.username
    logging.info(f"@{uname} is now running!")
    idle()
    Auput.stop()
    logging.info("NezukoStringBot stopped.!")
