import pandas as pd

def init_log():
    return pd.DataFrame(columns=["Datetime", "Symbol", "Timeframe", "Setup", "Notes"])

def add_trade(log_df, symbol, timeframe, setup, notes):
    return pd.concat([log_df, pd.DataFrame([{
        "Datetime": pd.Timestamp.now(),
        "Symbol": symbol,
        "Timeframe": timeframe,
        "Setup": setup,
        "Notes": notes
    }])], ignore_index=True)
