import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
  else:
    BOT_TOKEN = ""
    APP_ID = ""
    API_HASH = ""

class Messages():
      HELP_MSG = [
        ".",

        "**Kick Inactive Members**\n__Kick incative members from group. Add me as admin with ban users permission in group send the /inkick command with required arguments and i will kick members from group.\nUse /instatus to check current status of chat members.\n\nSee next page for command information & usages.__",
        
        "**Command**\n__/instatus - Get current members status.\n/dkick - Kick all deleted accounts from group.\n/inkick (arguments) - Kick inactive members from group.\nUse arguments with caution and seperated by space.__\n\n**Arguments -** __User’s Last Seen & Online status. Can be one of the following: “online”, user is online right now. “offline”, user is currently offline. “recently”, user with hidden last seen time who was online between 1 second and 2-3 days ago. “within_week”, user with hidden last seen time who was online between 2-3 and seven days ago. “within_month”, user with hidden last seen time who was online between 6-7 days and a month ago. “long_time_ago”, blocked user or user with hidden last seen time who was online more than a month ago. None, for bots.__\n\nSee next page for examples.",
        
        "**Examples**\n```/inkick within_month long_time_ago``` - __To kick users who are offline for more than 6-7 days.__\n\n```/inkick long_time_ago``` - __To kick members who are offline for more than a month and Deleted Accounts.__\n\n```/dkick``` - __To kick deleted accounts.__",
        
        "**Developer - @viperadnan**"
        ]

      START_MSG = "**Hey [{}](tg://user?id={})**\n__I can kick inactive members from group.\nLearn more at /help__"
      
      CREATOR_REQUIRED = "❗ **You have to be the group creator to do that.**"
      
      INPUT_REQUIRED = "❗ **Arguments Required**\n__See /help in personal message for more information.__"
      
      KICKED = "✔️ **Successfully Kicked {} members according to the arguments provided.**"
      
      START_KICK = "🚮**Removing inactive members this may take a while...**"
      
      ADMIN_REQUIRED = "❗**I am not an admin here**\n__Leaving this chat, add me again as admin with ban user permission.__"
      
      DKICK = "✔️ **Kicked {} Deleted Accounts Successfully.**"
      
      FETCHING_INFO = "**Collecting users information...**"
      
      STATUS = "**{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}"