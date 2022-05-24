from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "12787577"))
API_HASH = getenv("API_HASH", "d30cef43991a144be80615919bfcfc6c")
BOT_TOKEN = getenv("BOT_TOKEN","5384359690:AAFvC2DCE8iikRMBOrQ6yvVooHIkmS26WTo")
BOT_NAME = getenv("BOT_NAME","AGORA_ROBOT")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME","AQBE4MJekIGpCNEBTsMPeqxtNAvcU1NGdOyP-pwci3b6Osc1Cb9bDMJAKU92XqmQlHtiffC4WN_-h-08L7kdXtJqPtnz2b_bIGz-qIyRtdVfwElFrTrn0lk7c8KRfJtIZmTx2GYGfC7HyP7NtII5kV87S00Y6GP7aAtgm6KiyHTshREW80xYEgHmTolqc7bgSlqWrrTPbOpY6JrRZTwTYmqLzZOJLBfeptKQC_Sv8bOw_tJmmC31UgsjPa9L1awIFT05nvv3Va-TwJ4VlkNv9nZ1ZnZepwdv6QVTAKBb-yGWSp7ZozebzgQGG_4eQ9GCMSwtAvjLBmMfcl9BBZDEhyuPAAAAATe3gk0A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5272015055").split()))
