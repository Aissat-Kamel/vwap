import get_data as gd
import pandas as pd
import pandas_ta as ta
import mplfinance as mpf


def vwap(df, period):
    klines = df
    klines["tP"] = ta.hlc3(high = klines["High"], low = klines["Low"], close = klines["Close"])
    klines["tPV"] = klines["tP"] * klines["Volume"]
    klines["mtPV"] = ta.sma(klines["tPV"], length = period)
    klines["mV"] = ta.sma(klines["Volume"], length = period)
    klines["vwap"] = klines["mtPV"] / klines["mV"]
    vwap = klines["vwap"]
    columns = klines.columns
    for i in range(6, len(columns)):
        del klines[columns[i]]

    return vwap




data = gd.get_klines("BTCUSDT", "4h", "1400 hours ago UTC+1")
vwap_48 = vwap(data, 48)
vwap_84 = vwap(data, 84)

data["vwap_48"] = vwap_48
data["vwap_84"] = vwap_84

addition_plot = [mpf.make_addplot(data["vwap_48"], type = "scatter", markersize = 1, color = "#f3ff00"), mpf.make_addplot(data["vwap_84"], type = "scatter", markersize = 1, color = "#acff35")]
mpf.plot(data, type = "candle", volume = True, addplot = addition_plot,  style = 'yahoo')
