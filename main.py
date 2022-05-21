import schedule, time, os
import logging
from random import randint

import discord_bot as dc

logging.basicConfig(level=logging.INFO)  
logger = logging.getLogger(os.path.basename(__file__))  
logger.setLevel(20)  

def test(msg):
    print(msg)

# define Jobs
schedule.every(1).day.do(dc.daily)
schedule.every(1).hour.do(dc.work)
schedule.every(1).hour.do(dc.dice, randint(20, 200))
schedule.every(20).to(40).minutes.do(dc.check_invite)
schedule.every(20).to(40).minutes.do(dc.check_level)
schedule.every().day.at("08:00").do(dc.morning)
schedule.every().day.at("12:00").do(dc.afternoon)
schedule.every().day.at("21:00").do(dc.night)

# schedule.every(1).seconds.do(dc.test)

while 1:
    schedule.run_pending()
    time.sleep(1)
