import yfinance as yf
import pandas as pd

SYMBOL_MAP = {
    "Gold": "GC=F",
    "EUR/USD": "EURUSD=X",
    "GBP/USD": "GBPUSD=X"
}

def fetch_ohlcv(symbol, interval="15m", lookback_days=10):
    ticker = SYMBOL_MAP.get(symbol, symbol)
    df = yf.download(ticker, period=f"{lookback_days}d", interval=interval, progress=False)
    df = df.dropna()
    df.reset_index(inplace=True)
    df.rename(columns={"Datetime": "Datetime"}, inplace=True)
    return df
