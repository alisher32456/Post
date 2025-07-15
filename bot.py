import os
import requests
import random

BOT_TOKEN = os.getenv("7572960990:AAHyRBXvcEs1f5S5pfx-gkOUADw598L8668")
CHANNEL = os.getenv("@Tech_Pulse_Apps_AI_Hacks")

def get_random_post():
    with open("posts.txt", "r", encoding="utf-8") as f:
        posts = f.read().strip().split("\n\n")
        return random.choice(posts)

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHANNEL,
        "text": text,
        "parse_mode": "HTML"
    }
    r = requests.post(url, data=data)
    print(f"Status: {r.status_code}, Response: {r.text}")

if __name__ == "__main__":
    post = get_random_post()
    send_to_telegram(post)
  
