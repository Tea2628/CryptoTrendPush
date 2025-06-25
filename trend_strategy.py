kline = get_kline(symbol)
print(f"{symbol} 获取到K线: {kline[:2]}... 共 {len(kline)} 条")
def detect_volume_spike(kline_data, threshold=2.0):
    """
    检测是否出现成交量爆量（当前K线成交量大于过去N根的均值*阈值）
    :param kline_data: K线数据，格式为 [['timestamp', open, high, low, close, volume], ...]
    :param threshold: 判定为爆量的倍数阈值，默认是2倍
    :return: 是否爆量 (True/False)
    """
    volumes = [float(k[5]) for k in kline_data]
    if len(volumes) < 10:
        return False  # 数据不足，不判断

    avg_volume = sum(volumes[-10:-1]) / 9  # 最近9根的平均
    latest_volume = volumes[-1]

    if latest_volume > avg_volume * threshold:
        return True
    return False