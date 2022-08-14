# Future Imports
from __future__ import annotations

# Typing Imports
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import *

# Builtin Imports
import logging
import os
import sys

# Library Imports
import nextcord
from nextcord.ext import commands

# Project Imports
from cleverbotcog.cogs.cleverbot import CleverbotCog
from config import *

_logger = logging.getLogger(__name__)


def setup_logging():
    try:
        os.makedirs("logs", exist_ok=True)
        formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
        file_handler = logging.FileHandler(
            filename="logs/discord.log", encoding="utf-8", mode="w"
        )
        file_handler.setFormatter(formatter)
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)

        logging.basicConfig(
            level=logging.DEBUG if DEBUG else logging.INFO,
            handlers=(file_handler, stream_handler),
        )
    except OSError:
        print("Failed to set up logging")


def main():
    setup_logging()
    intents = nextcord.Intents.default()
    intents.message_content = True  # noqa
    bot = commands.Bot(command_prefix=PREFIX, intents=intents)
    bot.add_cog(CleverbotCog(bot))
    bot.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()
