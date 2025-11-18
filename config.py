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
BOT_TOKEN = getenv("BOT_TOKEN", "7400991879:AAHPVor0c7Evi5ZGs7dldV6eX8RgQWjggi4")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7616549285").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://foronlyyt458_db_user:foronlyyt458_db_user@cluster0.jexgidm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002812924241")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002812924241"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "1000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", None)
STRING = getenv("STRING", " BQGLEW8AEPjGirfr9RG-APIgPbPffmViPGXcaBxwE5nU-2BDx7q7aikTF9XViwmfFy70mX33Ddp96E5QwqofIsdC_neHZn2z9ZBZYkxdrh9NX9Vq4YH3HwE7iBoi0oJVrPovtpyznW1aDTW-RcTGnaDZ_McaI4kXiLQhQo0wPMxmfzs3ocHmw06VbKxmjeXLxCcDYZOOs1DKaIIWGd6RSEMH760kkN7wvDT4bTyiv164vhqQjAisEnRA0NE2JZIFC_WfIBo6FLN77pNyCrDHHi8_nQZ0nI-be4ymDZvehI0Bt1ZN0yFkD3eYSdnVcQ3Xbf-ql2viFvk1q55Bwh74iJbWWNhSpAAAAAH1jf68AA")
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", "BQGLEW8AQjGkL09qxBbcb4JWGkRsZ-pRLbBJCXmjtQZLQZ4-90WG2zjZ40rso8SiwDHwL6W5md6QkBC-XGxmjr5scL3qZOpAsyQlmbbe6d0n8w5U0FvJ_SQXbR8AhCPqQG84ipG_qXSF32s5g69mjR0ZlKIfS9RbOHUmOdujVUqr76N9DJOfb57mLGvTXa9pGj0HGsmSMoWGPRWh26GMzkkt3MP2-RgA1ZrxZvBth0XEX0XVX_gjBDCbdg5gy7JF_Ll3ZXs0CCb9_6Gg_Oy_wJBtbmM4h_66XOVcaEjxvlGKlA_TnCWHPEjyCW2kGhFWBJc0Yi7b6gQKr-es3MaRyNt1bIgWkwAAAAH1jf68AA")  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
