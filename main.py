from trend_strategy import analyze_coin
from telegram_push import send_message

if __name__ == '__main__':
    print("✅ Crypto Trend Push Started")
    result = analyze_coin()
    print("📊 生成分析结果如下：")
    
    if not result.strip():
        print("⚠️ 没有生成分析结果，可能是 coin_list 为空或网络问题")
    else:
        print(result)  # 打印分析结果
        send_message(result)  # 推送 Telegram