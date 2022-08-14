# Future Imports
from __future__ import annotations

# Typing Imports
import asyncio
from typing import TYPE_CHECKING

import nextcord

if TYPE_CHECKING:
    from typing import *
from nextcord.ext.commands import Context

# Builtin Imports
import logging
import uuid
import re

# Library Imports
from nextcord.ext import commands
from nextcord import Message, Game
from cleverbotfreeapi import cleverbot

# Project Imports
# []

_logger = logging.getLogger(__name__)


class CleverbotCog(commands.Cog, name="Cleverbot"):

    # region - MAGIC -
    def __init__(self, bot: commands.Bot):
        self._bot = bot
        self._conversations: Dict[int, str] = dict()

    # endregion

    # region - COMMANDS -
    @commands.command(name="startConversation")
    async def start_conversation(self, ctx: Context, name: str = str(uuid.uuid4())):
        self._conversations[ctx.message.channel.id] = name

    @commands.command(name="endConversation")
    async def end_conversation(self, ctx: Context):
        try:
            self._conversations.pop(ctx.message.channel.id)
            await ctx.send("Goodbye!")
        except KeyError:
            pass

    # endregion
    @staticmethod
    def __fix_string(string: str) -> str:
        pattern = r"\\x..\\x.."
        regex = list(map(lambda x: x.replace("\\x", ""), re.findall(pattern, string)))
        parts = re.split(pattern, string)
        # print(list(regex))
        # print(parts)

        def literal_to_string(s: str) -> str:
            return bytes.fromhex(s).decode(errors="ignore")

        return "".join(
            map(lambda x: x[0] + x[1], zip(parts, map(literal_to_string, regex + [""])))
        )

    # region - EVENTS -
    @commands.Cog.listener()
    async def on_message(self, message: Message):
        if (
            m_id := message.channel.id
        ) in self._conversations.keys() and message.author != self._bot.user:

            def get_answer() -> str:
                return self.__fix_string(
                    cleverbot(message.clean_content, session=self._conversations[m_id])
                )

            answer = get_answer()
            if "<html>" in answer:
                wait_msg = await message.channel.send(
                    embed=nextcord.Embed(
                        title="Service Temporarily Unavailable. Please wait... :clock1:"
                    )
                )
                while "<html" in (answer := get_answer()):
                    await asyncio.sleep(6)
                await wait_msg.delete()
            await message.channel.send(answer)

    @commands.Cog.listener()
    async def on_ready(self):
        _logger.info("Bot has successfully logged in")
        await self._bot.change_presence(activity=Game(name="Talk to me"))

    # endregion

    # region - PROPERTIES -
    # endregion

    # region - PUBLIC -
    # endregion

    # region - PROTECTED -
    # endregion

    # region - PRIVATE -
    # endregion
