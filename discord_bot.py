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
    chat(CH_GAME, '!work claim')
    time.sleep(randint(5, 10))
    chat(CH_GAME, '!work')

def coins():
    chat(CH_GAME, '!coins')

def items():
    chat(CH_GAME, '!items')

def dice():
    bet = randint(20, 200)
    chat(CH_GAME, f'!dice {bet}')

def guess():
    bet = randint(1, 10)
    chat(CH_GAME, f'!guess {bet}')
    for i in range(5):
        time.sleep(randint(5, 10))
        chat(CH_GAME, f'{randint(1, 99)}')

def check_invite():
    chat(CH_INVITE, '!invites')

def check_level():
    chat(CH_LEVEL, '!rank')

def morning():
    ctx = [
        "早安",
        "大家早!",
        "Morning guys",
        "吃早餐ㄌ",
    ]
    chat(CH_GENERAL, choice(ctx))


def afternoon():
    ctx = [
        "午安",
        "午休時間!",
        "Good after noon guyz",
        "好餓",
    ]
    chat(CH_GENERAL, choice(ctx))


def night():
    ctx = [
        "晚安",
        "晚上好",
        "Good night guyz",
        "想睡...",
    ]
    chat(CH_GENERAL, choice(ctx))


def go_along():
    ctx = [
        "對",
        "同意",
        "hahahaha",
        "哈",
        "可惡...",
        "zzz",
        "相信O2 META!",
        "怪怪的...",
        "來人啊",
        "XDDDDDD",
        "><",
        "==",
        "!!!",
        "沒事",
        "可能吧",
        "好像是",
        "QQ",
        "頂不住了...",
        "缺$$",
        "不太確定",
        "sorry~",
        "抱歉打錯ㄎㄎ",
    ]
    chat(CH_GENERAL, choice(ctx))

def test():
    msg = 'ㄎㄎ'
    print("test")
    td = timedelta(seconds=randint(0, 3))
    print("test", td)
    print(f'ch: general, sleepd {td.seconds}s, msg: {msg}')
    return schedule.cancel_job