from trend_strategy import detect_volume_spike
from okx_data import get_kline

def analyze_coin(symbol):
    kline_data = get_kline(symbol)
    if not kline_data:
        return "数据获取失败"

    # 判断是否爆量
    if detect_volume_spike(kline_data):
        return f"🚨 {symbol} 出现爆量成交！（注意可能异动）"

    # 可以保留你原来的趋势判断分析逻辑
    return f"{symbol} 正常，无爆量"
