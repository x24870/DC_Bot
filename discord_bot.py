import json, logging, os, time
import requests
import schedule
from datetime import timedelta
from random import randint, choice, randrange

from config import conf

AUTH_KEY = conf['AUTH']['key']
CH_GAME = conf['CHANNELS']['game']
CH_INVITE = conf['CHANNELS']['invite']
CH_LEVEL = conf['CHANNELS']['level']
CH_GENERAL = conf['CHANNELS']['general']

logger = logging.getLogger(os.path.basename(__file__))  
logger.setLevel(logging.INFO)

def chat(ch_id, msg):
    print(f'{ch_id}, {msg}')
    logger.info(f'{ch_id}, {msg}')
    header = {
        "Authorization": AUTH_KEY,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    }

    body = {
        "content": msg,
        "nonce": "82329451214{}33232234".format(randrange(0, 1000)),
        "tts": False,
    }
    url = "https://discord.com/api/v9/channels/{}/messages".format(ch_id)
    try:
        res = requests.post(url=url, headers=header, data=json.dumps(body))
        print(res.content)
        logger.info(res.content)
    except Exception as e:
        print(e)
        logger.error(e)

def daily():
    chat(CH_GAME, '!daily')

def work():
    chat(CH_GAME, '!work')

def dice(bet):
    chat(CH_GAME, f'!dice {bet}')

def check_invite():
    chat(CH_INVITE, '!invites')

def check_level():
    chat(CH_LEVEL, '!rank')

def morning():
    ctx = [
        "早安",
        "大家早!",
        "Morning guys",
        "吃早餐ㄌ"
    ]
    td = timedelta(hours=randint(0, 2), minutes=randint(0, 30))
    time.sleep(td.seconds)
    chat(CH_GENERAL, choice(ctx))

def afternoon():
    ctx = [
        "午安",
        "午休時間!",
        "Good after noon guyz",
    ]
    td = timedelta(hours=randint(0, 1), minutes=randint(0, 30))
    time.sleep(td.seconds)
    chat(CH_GENERAL, choice(ctx))

def night():
    ctx = [
        "晚安",
        "晚上好",
        "Good night guyz",
    ]
    td = timedelta(hours=randint(0, 3), minutes=randint(0, 50))
    time.sleep(td.seconds)
    chat(CH_GENERAL, choice(ctx))

def test():
    msg = 'ㄎㄎ'
    print("test")
    td = timedelta(seconds=randint(0, 3))
    print("test", td)
    time.sleep(td.seconds)
    print(f'ch: general, sleepd {td.seconds}s, msg: {msg}')
    return schedule.cancel_job