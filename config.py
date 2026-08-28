# config.py
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8779272496:AAFd1pX-ZzbkDiFgvS8JdQadKXpmy7iiE3g")
OWNER_ID = int(os.environ.get("OWNER_ID", 6533075996))
DEV_NAME = "𝗦𝗔𝗜𝗙ㅤ ✿"
DEV_USER = "saif_Officiel"

KEY_PREFIX = "R32-KEY"
MAX_DEVICES_DEFAULT = 5

KEYS_FILE = "keys.json"
USERS_FILE = "users.json"
BOT_STATUS_FILE = "bot_status.json"

LANG_EN = "en"
LANG_AR = "ar"

FLASK_PORT = int(os.environ.get("PORT", 5000))
FALLBACK_URL = "http://localhost:5000"