from coin_list import coin_symbols
from analyze import analyze_coin
from telegram_push import send_message

def main():
    all_results = []

    for symbol in coin_symbols:
        result = analyze_coin(symbol)
        print(result)
        all_results.append(result)

    message = "\n".join(all_results)
    send_message(f"📊 分析结果：\n\n{message}")

if __name__ == "__main__":
    main()
