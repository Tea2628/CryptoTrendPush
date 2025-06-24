from trend_strategy import analyze_coin
from telegram_push import send_message

if __name__ == '__main__':
    print("✅ Crypto Trend Push Started")
    result = analyze_coin()
    print("📊 生成分析结果如下：")
    print(result)  # 打印分析结果
    send_message(result)  # 推送给 Telegram