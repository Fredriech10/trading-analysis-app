import plotly.graph_objects as go

def create_chart(df, fvg_list=[], signals=[]):
    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=df["Datetime"],
        open=df["Open"],
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        name="Candles"
    ))

    for dt, side, low, high in fvg_list:
        color = "rgba(0,255,0,0.2)" if side == "Bullish" else "rgba(255,0,0,0.2)"
        fig.add_shape(type="rect", x0=dt, x1=dt, y0=low, y1=high,
                      fillcolor=color, line=dict(width=0))

    for dt, sig in signals:
        color = "green" if "Bullish" in sig else "red"
        fig.add_trace(go.Scatter(
            x=[dt], y=[df[df["Datetime"] == dt]["Close"].values[0]],
            mode="markers+text", name=sig,
            marker=dict(color=color, size=8),
            text=[sig], textposition="top center"
        ))

    fig.update_layout(height=500, margin=dict(t=10, b=10))
    return fig
