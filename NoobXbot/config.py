##configaration

from os import getenv 

from dotenv import load_dotenv

load_dotenv()
SESSION_NAME = getenv('SESSION_NAME', 'session')
BOT_TOKEN = getenv('BOT_TOKEN')
API_ID = int(getenv('API_ID', "12345687"))
API_HASH = getenv('API_HASH')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '30'))
COMMAND_PREFIX = list(getenv('COMMAND_PREFIXS', '/.,:;!').split())
MONGO_DB_URI = getenv("MONGO_DB_URI")
SUDO_USER = list(map(int, getenv('SUDO_USERS', '').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001599430559')) 
ASS_ID = int(getenv("ASS_ID", '2144966937'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '').split ()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP")
UPDATES_CHANEL = getenv("UPDATES_CHANNEL")                   
