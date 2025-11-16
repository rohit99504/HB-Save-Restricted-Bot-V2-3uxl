# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "27100684"))
API_HASH = getenv("API_HASH", "3d9ff72941b7c8ecafbadf7d625f0108")
BOT_TOKEN = getenv("BOT_TOKEN", "8353255262:AAF2sxswfuvnLJnK6E8eZmgCSZR7LLgik3E")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7616549285").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://foronlyyt458_db_user:foronlyyt458_db_user@cluster0.jexgidm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002812924241")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002812924241"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "1000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", None)
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
