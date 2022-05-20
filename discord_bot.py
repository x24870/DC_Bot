import random, json
import requests

class Job:
    def __init__(self):
        self.jobs = []

def chat(channel_id, auth_key):
    header = {
        "Authorization": auth_key,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    }

    body = {
        "content": "!work",
        "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
        "tts": False,
    }
    url = "https://discord.com/api/v9/channels/{}/messages".format(channel_id)
    try:
        res = requests.post(url=url, headers=header, data=json.dumps(body))
        print(res.content)
    except Exception as e:
        print(e)
