import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    print(f"📤 准备推送消息：{message}")  # 打印将要推送的内容
    try:
        response = requests.post(url, json=payload)
        print(f"📩 返回状态码: {response.status_code}")  # 打印返回状态
        print(f"📦 返回内容: {response.text}")            # 打印完整响应
        if response.status_code != 200:
            print("❌ 推送失败，状态码异常")
    except Exception as e:
        print(f"⚠️ 发送 Telegram 消息出错: {e}")