# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Files Sharing Bot!
*I am official file Cloud bot of [M'Cube Movies](https://t.me/joinchat/F_6ts1iYxSE4YzNl)

🤖 **My Name:** [Files Cloud Bot](https://t.me/{BOT_USERNAME})

🧑🏻‍💻 **Developer:** [Rashmika](https://t.me/rashmikamandannaofficial1)

👥 **Support Group:** [GROUP](https://t.me/joinchat/F_6ts1iYxSE4YzNl)

📢 **Updates Channel:** [CHANNEL](https://t.me/MCubeMediaOfficial)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** [Rashmika](https://t.me/rashmikamandannaofficial1)
M'Cube Media
–––––––––––
Official channel
🖇 @MCubeMediaofficial

"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\n**ഞാൻ ഒരു ഫയൽ Cloud bot ആണ് ഞങ്ങളുടെ ഗ്രൂപ്പ് സന്ത്രശിക്കുക** **File Cloud Bot**.

"""
