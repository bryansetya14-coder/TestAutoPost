import asyncio
from discord.ext import commands

bot = commands.Bot(command_string="!", self_bot=True)

MESSAGE = """SELL CHEAP GO <:Arrow:850540193626193941> FKFVH <:Verified:1000267030550827128>  

- Arroz Con Pollo / 2 <:WL:880251447470596157>  

SELL CHEAP GO <:Arrow:850540193626193941> FKFVH <:Verified:1000267030550827128>"""


@bot.event
async def on_ready():
  print(f"Bot 2 Logged in as {bot.user}")
  bot.loop.create_task(auto_post())


async def auto_post():
  await bot.wait_until_ready()
  channel_id = 123456789012345678  # Ganti dengan ID channel tujuanmu

  while not bot.is_closed():
    channel = bot.get_channel(channel_id)
    if channel:
      try:
        await channel.send(MESSAGE)
        print("Bot 2: Pesan 2 terkirim!")
      except Exception as e:
        print(f"Error: {e}")
    await asyncio.sleep(7200)  # Jeda 2 jam


bot.run("MASUKKAN_TOKEN_DISCORD_MU")