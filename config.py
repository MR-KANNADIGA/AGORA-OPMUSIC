from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "12787577"))
API_HASH = getenv("API_HASH", "d30cef43991a144be80615919bfcfc6c)
BOT_TOKEN = getenv("BOT_TOKEN","5384359690:AAFvC2DCE8iikRMBOrQ6yvVooHIkmS26WTo")
BOT_NAME = getenv("BOT_NAME","ΛႺՕ𝖱Λ 𝖱ՕΒՕΤ")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "AQBz5n5rUrxlWOWaBVGplD_qHRQz0zTQd9OKvkd8chrSDHaT6fA9KcvlrUsS4s2yb7xRl5RZZdj-XJ1q4Y9XYgzPruChblz9zK06vXl5gmXHUppK5qFRHohl05Dpint_XOvhfD2QHxa7friwMYbvZWQlnjbmaQ9r1v90kRUyAc_fFaM90p5ACDuyCp74gJAGNCcmrOU2RO6YAkAaFoGJcU8MCHYq0E7vz2T1zMiusNBs9oKCwDkzidKtu6gGTP-ITIHg0Qr3U6FrhK-ke1NeRGS3odROZ_SgXt7DCtEnBs8aMvd_yaT41X-Zyeyz_4FSLzQ5h5cmF1pQpX2ozGzTV1fcAAAAATe3gk0A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5272015055").split()))
