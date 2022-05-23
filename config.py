from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "12787577"))
API_HASH = getenv("API_HASH", "d30cef43991a144be80615919bfcfc6c")
BOT_TOKEN = getenv("BOT_TOKEN","5339877539:AAGXXR3pHnZdzpM1_2jkWTHMQ_Dusg8iYZI")
BOT_NAME = getenv("BOT_NAME","BROKEN_SHIV_MUSIC_BOT")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME","AQCixVsVq03X4ewNpE2Km1ay0eaLrQOAr9gSGux8PcggbzPwoKLQeTeFEeLWa99MXLe9l9iCnAorBLUAQWwWEMeSw2vi6ZAjiJyPY8vbhXpzCbpyluz7UwTPly9wpFCKhljqLuupgUYdekm90hbdnWu-cMdYJp3SHX-WCdO6oajWBbsBELzl3nZGQ2BOb3YLhEJiqxuNdg0vsSPSLkjhpWx-oWZGeWXtqsPr_j03MvNj2hkekRecWhP-1rDb_eZq5lkOKEN-4DZ_Yze30svRW7BGMxY6ERz8kYI4a8_NvSCR4LofpfEaO2V6dXGSbOrFgL3BMb9FaolPmm3r5B9T1_R7AAAAAUAIcxAA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5272015055").split()))
