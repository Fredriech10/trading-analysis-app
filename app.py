import streamlit as st
import pandas as pd
from data_fetcher import fetch_ohlcv
from technical_analysis import detect_fvg, detect_rejection_candles
from chart_creator import create_chart
from trade_log import init_log, add_trade

st.set_page_config(layout="wide")
st.title("📊 Trading Analysis App")

if "trade_log" not in st.session_state:
    st.session_state.trade_log = init_log()

col1, col2 = st.columns([1, 2])

with col1:
    symbol = st.selectbox("Select Symbol", ["Gold", "EUR/USD", "GBP/USD"])
    timeframe_pair = st.selectbox("Select Timeframe Pair", [
        ("1m", "5m"), ("5m", "15m"), ("15m", "1h"), ("1h", "4h")
    ])
    if st.button("Run Analysis"):
        ht, lt = timeframe_pair

        df_high = fetch_ohlcv(symbol, ht)
        df_low = fetch_ohlcv(symbol, lt)

        fvg = detect_fvg(df_high)
        reversals = detect_rejection_candles(df_low)

        st.session_state["fvg"] = fvg
        st.session_state["reversals"] = reversals
        st.session_state["df_low"] = df_low

with col2:
    if "df_low" in st.session_state:
        fig = create_chart(
            st.session_state["df_low"],
            st.session_state["fvg"],
            st.session_state["reversals"]
        )
        st.plotly_chart(fig, use_container_width=True)

        with st.expander("💾 Log Trade Idea"):
            setup = st.text_input("Setup Type", "FVG + Rejection")
            notes = st.text_area("Notes")
            if st.button("Save Trade"):
                st.session_state.trade_log = add_trade(
                    st.session_state.trade_log,
                    symbol, f"{timeframe_pair[0]}/{timeframe_pair[1]}",
                    setup, notes
                )
                st.success("Trade logged.")

with st.expander("📜 Trade Log"):
    st.dataframe(st.session_state.trade_log)
