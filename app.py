import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import traceback
from data_fetcher import DataFetcher
from technical_analysis import TechnicalAnalysis
from chart_creator import ChartCreator

# Page configuration
st.set_page_config(
    page_title="Trading Analysis App",
    page_icon="📈",
    layout="wide"
)

# Title and description
st.title("📈 Trading Analysis Application")
st.markdown("**Multi-timeframe technical analysis for Forex pairs and Gold**")
st.markdown("---")

# Initialize session state
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = None

# Symbol mapping for yfinance
SYMBOL_MAP = {
    "Gold": "GC=F",
    "EUR/USD": "EURUSD=X",
    "GBP/USD": "GBPUSD=X"
}

# Sidebar for controls
st.sidebar.header("Analysis Controls")

# Symbol selection
selected_symbol = st.sidebar.selectbox(
    "Select Trading Symbol:",
    options=list(SYMBOL_MAP.keys()),
    index=0
)

# Timeframe selection
timeframe_options = {
    '1min & 5min': ('1m', '5m'),
    '5min & 15min': ('5m', '15m'),
    '15min & 1hour': ('15m', '1h'),
    '1hour & 4hour': ('1h', '4h')
}

selected_timeframes = st.sidebar.selectbox(
    "Select Timeframe Combination:",
    options=list(timeframe_options.keys()),
    index=2  # Default to 15min & 1hour
)

# Get the actual timeframe values
smaller_tf, larger_tf = timeframe_options[selected_timeframes]
