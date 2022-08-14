# cleverbotcog
A Cog for discord bots which queries the cleverbot api using [cleverbotfreeapi](https://github.com/Deftera186/cleverbotfreeapi).

## Commands
This Cog adds the following commands to your bot:
- startConversation
  - Starts a conversation in the current Text-Channel. > Note: Only one conversation per Text-Channel is allowed
- endConversation
  - Ends the conversation in the current Text-Channel

## Installation
```
pip install git+https://github.com/IchbinLuka/cleverbotDiscordCog
```

## Usage
```python
from cleverbotcog import CleverbotCog
from nextcord.ext import commands
import nextcord


if __name__ == '__main__':
    # This intent is required for the bot to work.
    intents = nextcord.Intents.default()
    intents.message_content = True # noqa
    
    bot = commands.Bot(command_prefix="[PREFIX]", intents=intents)
    bot.add_cog(CleverbotCog(bot=bot))
    
```
