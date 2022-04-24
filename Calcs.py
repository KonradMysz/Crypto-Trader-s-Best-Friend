class Calcs(object):
    """This class contains functions to calculate basic technical indicators for the symbol"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# Simple Moving Average

def SMA(data_frame, wind):
    col_name = 'SMA_' + str(wind)
    data_frame[col_name] = data_frame['close'].rolling(window = wind).mean()

# Exponential Moving Average

def EMA(data_frame, n):
    alpha = 2 / (n + 1)
    col_name = 'EMA_' + str(n)
    data_frame[col_name] = data_frame['close'].ewm(alpha=alpha).mean()

# Relative Strength Index

def RSI(data_frame):
    close_delta = data_frame['close'].diff()
    
    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)
    
    ma_up = up.rolling(window = 9).mean()
    ma_down = down.rolling(window = 9).mean() 
    
    rs = ma_up / ma_down
    data_frame['RSI'] = 100 - (100/(1 + rs))

# Bollinger Bands

def boll_bands(data_frame):
    
    std = data_frame['close'].rolling(20).std()
    
    data_frame['boll_up'] = data_frame['SMA_20'] + 2 * std
    data_frame['boll_down'] = data_frame['SMA_20'] - 2 * std

# Classical Momentum

def momentum(data_frame):
    close_20 = data_frame['close'].shift(20)
    data_frame['momentum'] = data_frame['close'] - close_20

# Moving Average Covergence / Divergence

def macd(data_frame):
    
    alpha_12 = 2 / (12 + 1)
    alpha_26 = 2 / (26 + 1)
    
    EMA_12 = data_frame['close'].ewm(alpha=alpha_12).mean()
    EMA_26 = data_frame['close'].ewm(alpha=alpha_26).mean()
    
    data_frame['macd'] = EMA_12 - EMA_26
    data_frame['signal'] = data_frame['macd'].ewm(alpha=0.2).mean()
    data_frame['macd_hist'] = data_frame['macd'] - data_frame['signal']

# Stochastic RSI

def stoch_rsi(data_frame):
    min_price = data_frame['low'].rolling(window = 14).min()
    max_price = data_frame['high'].rolling(window = 14).max()

    
    ma_up = data_frame['close'] - min_price
    ma_down = max_price - min_price
    
    data_frame['stoch_rsi'] = ma_up / ma_down
    data_frame['stoch_rsi'] = 100 * data_frame['stoch_rsi']
    data_frame['stoch_rsi_sma'] = data_frame['stoch_rsi'].rolling(window = 3).mean() 



