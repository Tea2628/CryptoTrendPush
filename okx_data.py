# okx_data.py
import requests

def get_kline(symbol, interval="5m", limit=100):
    url = f"https://www.okx.com/api/v5/market/candles?instId={symbol}&bar={interval}&limit={limit}"
    try:
        resp = requests.get(url)
        data = resp.json()
        if data["code"] == "0":
            return data["data"]
        else:
            return []
    except Exception as e:
        print(f"获取K线失败: {e}")
        return []