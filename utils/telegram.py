import requests


TELEGRAM_BOT_TOKEN = '7353444926:AAFoIaBpjV_w_0BFAfP3jzA-cyQOFFupaJw'
TELEGRAM_CHAT_ID = '484955140'


def send_telegram_message(
        message: str, 
        telegram_bot_token: str = TELEGRAM_BOT_TOKEN, 
        telegram_chat_id: str = TELEGRAM_CHAT_ID
        ):
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
