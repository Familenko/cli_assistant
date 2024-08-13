import os
import requests
from credentials import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID


def send_telegram_message(message, telegram_bot_token=TELEGRAM_BOT_TOKEN, telegram_chat_id=TELEGRAM_CHAT_ID):
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    data = {
        "chat_id": telegram_chat_id,
        "text": message
    }
    response = requests.post(url, data=data)
    return response.json()


if __name__ == "__main__":
    message = "Hello, World!"
    response = send_telegram_message(message)
    print(response)
