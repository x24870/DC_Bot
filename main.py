import schedule, time, os
import logging
from random import randint

import discord_bot as dc

logging.basicConfig(level=logging.INFO)  
logger = logging.getLogger(os.path.basename(__file__))  
logger.setLevel(20)  

# define Jobs
schedule.every(1).day.do(dc.daily)
schedule.every(61).minutes.do(dc.work)
schedule.every(62).minutes.do(dc.dice)
schedule.every(63).minutes.do(dc.guess)
schedule.every(40).to(70).minutes.do(dc.check_invite)
schedule.every(30).to(60).minutes.do(dc.check_level)
schedule.every(20).to(40).minutes.do(dc.coins)
schedule.every(60).to(90).minutes.do(dc.items)
schedule.every(30).to(90).minutes.do(dc.go_along)
schedule.every().day.at("08:00").do(dc.morning)
schedule.every().day.at("12:00").do(dc.afternoon)
schedule.every().day.at("21:00").do(dc.night)


# schedule.every(1).seconds.do(dc.test)

while 1:
    schedule.run_pending()
    time.sleep(1)
