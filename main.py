# main.py
from okx_data import get_kline
from telegram_push import send_message
from coin_list import coin_symbols

def analyze_coin(symbol):
    kline = get_kline(symbol)
    if not kline or len(kline) < 20:
        return None
    
    closes = [float(k[4]) for k in kline]  # 收盘价
    avg_price = sum(closes[-20:]) / 20
    current_price = closes[-1]

    if current_price > avg_price * 1.01:
        return f"📈 *{symbol}* → 建议做多（当前价高于20均线）"
    elif current_price < avg_price * 0.99:
        return f"📉 *{symbol}* → 建议做空（当前价低于20均线）"
    else:
        return f"⚖️ *{symbol}* → 观望（震荡）"

def main():
    summary = ["📊 *币种趋势分析推送*"]
    for symbol in coin_symbols:
        result = analyze_coin(symbol)
        if result:
            summary.append(result)
    message = "\n".join(summary)
    send_message(message)

if __name__ == "__main__":
    main()