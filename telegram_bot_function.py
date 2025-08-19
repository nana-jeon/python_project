import requests

toked = '8116993901:AAFV2oZ3_MOrEhL_XsqYUjtTIyzOqmqQ0WY'

DEFAULT_CHAT_ID = '@O_Romdoul'

def sendText(message: str, chat_id: str = DEFAULT_CHAT_ID) -> dict:
    """
    :param chat_id:
    :param message:
    :return:

     caption = "<b>Here’s a cute cat!</b>"

    """
    url = f"https://api.telegram.org/bot{toked}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }
    response = requests.post(url, data=payload)
    return response.json()


