# config.py
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8315527579:AAHUcXpBkoGwttO0QKdxrHElEFn_58BiBN0")
OWNER_ID = int(os.environ.get("OWNER_ID", 8950729666))
DEV_NAME = "AMIN VIP"
DEV_USER = "amin9384n"

KEY_PREFIX = "Amin-KEY"
MAX_DEVICES_DEFAULT = 5

KEYS_FILE = "keys.json"
USERS_FILE = "users.json"
BOT_STATUS_FILE = "bot_status.json"

LANG_EN = "en"
LANG_AR = "ar"

FLASK_PORT = int(os.environ.get("PORT", 5000))
FALLBACK_URL = "http://localhost:5000"