from okx_data import get_kline
from coin_list import coin_symbols

def analyze_coin():
    summary = ["📊 币种趋势分析结果 🔽"]
    for symbol in coin_symbols:
        kline = get_kline(symbol)
        if not kline or len(kline) < 20:
            continue

        closes = [float(k[4]) for k in kline]  # 第5列是收盘价
        avg_price = sum(closes[-20:]) / 20
        current_price = closes[-1]

        if current_price > avg_price * 1.01:
            summary.append(f"📈 *{symbol}* ➜ 建议做多（当前价高于20均线）")
        elif current_price < avg_price * 0.99:
            summary.append(f"📉 *{symbol}* ➜ 建议做空（当前价低于20均线）")
        else:
            summary.append(f"⚖️ *{symbol}* ➜ 震荡观望（当前价接近均线）")

    return "\n".join(summary)