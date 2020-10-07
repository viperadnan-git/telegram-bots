from config import Config
from pyrogram import Client

plugins = dict(root="plugins")
app = Client(
     'inkick-bot',
      bot_token = Config.BOT_TOKEN,
      api_id = Config.APP_ID,
      api_hash = Config.API_HASH,
      plugins = plugins
)
app.run()