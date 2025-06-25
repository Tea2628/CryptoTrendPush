def detect_volume_spike(candles, compare_length=20, volume_threshold_multiplier=2.0):
    """
    判断当前K线是否为爆量。
    参数:
        candles: list，每根K线格式 [timestamp, open, high, low, close, volume]
        compare_length: int，向前对比的K线数量
        volume_threshold_multiplier: float，爆量倍数阈值
    返回:
        bool，是否爆量
    """
    if len(candles) < compare_length + 1:
        return False  # 数据不足

    current_volume = candles[-1][5]
    recent_volumes = [c[5] for c in candles[-compare_length-1:-1]]
    avg_volume = sum(recent_volumes) / compare_length

    return current_volume > avg_volume * volume_threshold_multiplier