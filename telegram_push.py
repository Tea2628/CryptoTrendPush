import requests
import config

def send_message(message):
    url = f"https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": config.CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"  # 支持换行与格式
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code != 200:
            print(f"Telegram推送失败: {response.text}")
    except Exception as e:
        print(f"Telegram连接错误: {e}")
