import schedule, time
from config import conf

from discord_bot import chat

schedule.every(1).hours.do(chat("ch_id", "auth_key"))

while 1:
    schedule.run_pending()
    time.sleep(1)
