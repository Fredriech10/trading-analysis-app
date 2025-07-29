def detect_fvg(df):
    fvg_list = []
    for i in range(2, len(df)):
        prev2_low = df.loc[i-2, "Low"]
        prev1_high = df.loc[i-1, "High"]
        if prev2_low > prev1_high:  # Bullish FVG
            fvg_list.append((df.loc[i, "Datetime"], "Bullish", prev1_high, prev2_low))
        elif prev2_low < prev1_high and df.loc[i-1, "Low"] > df.loc[i-2, "High"]:  # Bearish FVG
            fvg_list.append((df.loc[i, "Datetime"], "Bearish", prev2_low, prev1_high))
    return fvg_list

def detect_rejection_candles(df):
    signals = []
    for i in range(1, len(df)):
        body = abs(df.loc[i, "Close"] - df.loc[i, "Open"])
        wick_top = df.loc[i, "High"] - max(df.loc[i, "Close"], df.loc[i, "Open"])
        wick_bottom = min(df.loc[i, "Close"], df.loc[i, "Open"]) - df.loc[i, "Low"]
        if wick_top > body * 2:
            signals.append((df.loc[i, "Datetime"], "Bearish Rejection"))
        elif wick_bottom > body * 2:
            signals.append((df.loc[i, "Datetime"], "Bullish Rejection"))
    return signals
