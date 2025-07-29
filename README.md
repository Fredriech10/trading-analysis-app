- **Dependencies**: yfinance, pandas, numpy

### Technical Analysis (`technical_analysis.py`)
- **Purpose**: Performs comprehensive technical analysis on market data
- **Key Features**:
  - Swing point detection using rolling window approach
  - Fair Value Gap (FVG) identification for market inefficiencies
  - Trading channel analysis with parallel support/resistance lines
  - Trade setup detection (rejection candles, engulfing patterns, wick patterns)
  - Channel breakout signal detection
- **Algorithm**: Uses statistical methods including linear regression for trend line analysis and pattern recognition

### Main Application (`app.py`)
- **Purpose**: Streamlit web interface and application orchestration
- **Key Features**:
  - Symbol selection for Gold, EUR/USD, and GBP/USD
  - Real-time analysis triggering with comprehensive reporting
  - Interactive plotly charts for 1H and 15M timeframes
  - Trading channel analysis and breakout detection
  - Trade opportunity identification and risk management guidance

### Chart Creator (`chart_creator.py`)
- **Purpose**: Creates interactive plotly charts for technical analysis visualization
- **Key Features**:
  - Candlestick charts with OHLC data
  - Swing point overlays with visual markers
  - Fair Value Gap highlighting with color-coded regions
  - Trading channel lines with support/resistance visualization
  - Breakout signal indicators
  - Volume analysis charts

## Data Flow

1. **User Input**: User selects trading symbol from sidebar dropdown
2. **Data Retrieval**: Application maps symbol to Yahoo Finance ticker and fetches historical data
3. **Technical Analysis**: System analyzes price data to identify swing points and patterns
4. **Results Display**: Analysis results are presented in the main content area
5. **State Persistence**: Results are stored in Streamlit session state for continued interaction

## External Dependencies

### Core Libraries
- **Streamlit**: Web application framework for the user interface
- **yfinance**: Yahoo Finance API client for market data retrieval
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing operations
- **plotly**: Interactive charting and visualization library
- **scikit-learn**: Machine learning library for linear regression in channel analysis

### Data Source
- **Yahoo Finance**: Primary data provider for real-time and historical market data
- **Supported Instruments**: 
  - Gold futures (GC=F)
  - EUR/USD forex pair (EURUSD=X)
  - GBP/USD forex pair (GBPUSD=X)

## Deployment Strategy

### Current Setup
- **Platform**: Designed for Streamlit deployment (local or cloud-based)
- **Configuration**: Uses Streamlit's built-in page configuration with wide layout
- **Dependencies**: Managed through standard Python package imports

### Scalability Considerations
- **Session Management**: Uses Streamlit's session state for user data persistence
- **Data Caching**: Potential for implementing Streamlit caching decorators for improved performance
- **Error Handling**: Basic error handling implemented in data fetcher with user-friendly warnings

### Performance Optimizations
- **Data Fetching**: Configurable historical data range (default 30 days) to balance data completeness with performance
- **Analysis Window**: Adjustable swing point detection window for fine-tuning analysis sensitivity
- **Real-time Updates**: On-demand analysis execution rather than continuous polling

## Technical Notes

### Symbol Mapping
The application uses a predefined mapping between user-friendly symbol names and Yahoo Finance ticker symbols to abstract the complexity of financial data identifiers from the end user.

### Analysis Methodology
- **Swing Points**: Rolling window approach identifies local extremes requiring minimum data points
- **Fair Value Gaps**: Detects price gaps between candles indicating market inefficiencies
- **Trading Channels**: Uses linear regression to identify parallel support and resistance lines
- **Channel Breakouts**: Monitors price movement relative to channel boundaries for direction change signals
- **Trade Setups**: Analyzes candlestick patterns including rejections, engulfing patterns, and wick formations

### Recent Changes (January 2025)
- Added trading channel analysis using linear regression for parallel trend line detection
- Implemented interactive plotly charts for both 1H and 15M timeframes
- Enhanced technical analysis with Fair Value Gap identification
- Added channel breakout detection and trading guidance
- Integrated comprehensive trade setup analysis with risk/reward calculations
- Created chart visualization system with technical indicator overlays

### Latest Changes (July 29, 2025)
- **Removed Channel Detection**: Completely removed channel analysis due to accuracy issues and false signals
- **Implemented Multi-Timeframe Selection**: Added dropdown with paired timeframes (1min/5min, 5min/15min, 15min/1h, 1h/4h)
- **FVG Analysis on Larger Timeframe**: Fair Value Gap detection now focuses on the selected larger timeframe for market bias
- **Reversal Analysis on Smaller Timeframe**: Trade setup detection and reversal patterns analyzed on the smaller selected timeframe
- **Enhanced Chart Visualization**: Updated charts to show FVG analysis on larger timeframe and trade setups on smaller timeframe
- **Streamlined User Interface**: Simplified analysis approach focusing on multi-timeframe correlation without complex channel calculations
- **Signal Accuracy Improvement**: Removed unreliable channel signals, focusing on proven FVG and reversal pattern detection# trading-analysis-app
