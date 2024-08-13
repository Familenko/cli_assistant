import os
import requests


def send_telegram_message(message, telegram_bot_token=None, telegram_chat_id=None):
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    data = {
        "chat_id": telegram_chat_id,
        "text": message
    }
    response = requests.post(url, data=data)
    return response.json()
