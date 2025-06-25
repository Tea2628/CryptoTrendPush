from coin_list import coin_symbols
from analyze import analyze_coin
from telegram_push import send_message
from datetime import datetime

def main():
    all_results = []

    for symbol in coin_symbols:
        result = analyze_coin(symbol)
        print(result)
        all_results.append(result)

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    message = f"📈 数据分析推送\n时间：{now}\n\n" + "\n".join(all_results)
    send_message(message)

if __name__ == "__main__":
    main()
