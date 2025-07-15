import telebot
import random
import requests

# 🛡 Bot ka token aur channel set karo
BOT_TOKEN = "7572960990:AAHyRBXvcEs1f5S5pfx-gkOUADw598L8668"
CHANNEL = "@Tech_Pulse_Apps_AI_Hacks"  # ya "-1001234567890" for private channels

bot = telebot.TeleBot(BOT_TOKEN)

def get_random_post():
    with open("posts.txt", "r", encoding="utf-8") as f:
        posts = f.read().strip().split("\n\n")
        return random.choice(posts)

@bot.message_handler(commands=['post'])
def handle_post_command(message):
    post = get_random_post()
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHANNEL,
        "text": post,
        "parse_mode": "HTML"
    }
    r = requests.post(url, data=data)
    if r.status_code == 200:
        bot.reply_to(message, "✅ Post sent to channel!")
    else:
        bot.reply_to(message, f"❌ Error: {r.text}")

print("🤖 Bot is running... Send /post command.")
bot.infinity_polling()
