from okx_data import get_kline
from coin_list import coin_symbols

def analyze_coin():
    summary = ["📊 币种趋势分析结果 ⏬"]

    for symbol in coin_symbols:
        print(f"开始获取 {symbol} 的K线数据")  # 调试输出
        kline = get_kline(symbol)
        print(f"{symbol} 获取到 {len(kline)} 条K线")  # 输出K线条数
        
        if not kline or len(kline) < 20:
            print(f"⚠️ {symbol} 数据不足，跳过")
            continue

        closes = [float(k[4]) for k in kline]  # 收盘价
        avg_price = sum(closes[-20:]) / 20
        current_price = closes[-1]

        if current_price > avg_price * 1.01:
            summary.append(f"📈 *{symbol}* → 建议关注上涨机会")
        elif current_price < avg_price * 0.99:
            summary.append(f"📉 *{symbol}* → 建议留意下跌风险")
        else:
            summary.append(f"⚖️ *{symbol}* → 震荡盘整中")

    return "\n".join(summary)