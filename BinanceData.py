class BinanceData:
    """This class contain functions and objects to dowlonad data from Binance API"""

import urllib.request
from datetime import datetime
import json
import requests
import pandas as pd

# URL DEFINITIONS

candle_root_url = 'https://api.binance.com/api/v1/klines'

def candle_url(symbol, interval):
    candle_url = candle_root_url + '?symbol=' + symbol + '&interval=' + interval
    return candle_url

exchange_url = 'https://api.binance.com/api/v1/exchangeInfo'

# GET CANDLESTICK CHART DATA

def get_bars(symbol, interval):
    url = candle_url(symbol, interval)
    data = json.loads(requests.get(url).text)
    df = pd.DataFrame(data)
    df = df.astype('float32')
    df.columns = ['open_time',
                  'open', 'high', 'low', 'close', 'volume',
                  'close_time', 'qav', 'num_trades',
                  'taker_base_vol', 'taker_quote_vol', 'ignore']
    df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
    df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')
    df.index = range(0,500)
    df.drop('ignore', inplace=True, axis=1)
    return df

# GET LIST OF AVAILABLE SYMBOLS

def get_symbols():
    exchange_info = json.loads(requests.get(exchange_url).text)
    symbols = []
    for s in exchange_info['symbols']:
        status = s['status']
        if(status == 'TRADING'):
            symbols.append(s['symbol'])
    return symbols


