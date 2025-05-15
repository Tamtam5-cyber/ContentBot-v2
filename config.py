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

API_ID = int(getenv("API_ID", "18433784"))
API_HASH = getenv("API_HASH", "a1c73c8713d798ffdd34ed02870d3fe6")
BOT_TOKEN = getenv("BOT_TOKEN", "8158555808:AAGqSGO2TV5wjAA0IBYKHXRmBpzQgJWGk2Y")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6383614933").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://mie28557:q1231234@autobot.mjrqtws.mongodb.net/?retryWrites=true&w=majority&appName=autobot")
LOG_GROUP = getenv("LOG_GROUP", "https://t.me/+-i29TtDEY7s3MjU1")
CHANNEL_ID = int(getenv("CHANNEL_ID", "2403968850"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "https://upshrink.com/st?api= d2b7f35848bb91babed0912654efe1a62e28338b &url= yourdestinationlink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", "https://t.me/UltimateSMMNews")  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
