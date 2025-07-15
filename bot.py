def send_to_telegram(text):
    import os, requests
    BOT_TOKEN = "7572960990:AAHyRBXvcEs1f5S5pfx-gkOUADw598L8668"
    CHANNEL = "@Tech_Pulse_Apps_AI_Hacks"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHANNEL,
        "text": text,
        "parse_mode": "HTML"
    }

    response = requests.post(url, data=data)
    print(f"Status: {response.status_code}, Response: {response.text}")

send_to_telegram("✅ Test message from your GitHub bot!\n👉 @Tech_Pulse_Proxy_MTProto")
