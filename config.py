from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://filegram.pronet.cfd/dl/rcYFiXVZ35tZVJ-T3k3/5877473525953052206_y_4.jpg")
START_IMG = getenv("START_IMG", "https://filegram.pronet.cfd/dl/rcYFiXVZ35tZVJ-T3k3/5877473525953052206_y_4.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/o_c_v")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/o_c_v")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6654496819").split()))


FAILED = "https://telegra.ph/file/4b06002f7b2b9742d02b2.jpg"
