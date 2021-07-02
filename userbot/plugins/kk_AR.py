import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "telethon":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit("@ViruThon \n  @ilTTTl")
        else:
            await event.edit("@ViruThon \n  @ilTTTl")
