class Behaviour(object):
    """Behaviour for all possible cases"""

import BinanceData as bd
import Calcs as cs
import Plots as pts

# Basic Candlestick Plot

def run_basic(data_frame):
    pts.vol_plot(data_frame).show()

# Simple Moving Average

def run_sma(data_frame):
    cs.SMA(data_frame, 20)
    cs.SMA(data_frame, 50)
    cs.SMA(data_frame, 100)
    pts.sma_plot(data_frame)

    current = data_frame['close'][499]
    sma_20 = data_frame['SMA_20'][499]
    sma_50 = data_frame['SMA_50'][499]
    sma_100 = data_frame['SMA_100'][499]

    print('Current price is ' + str(current) + ', SMA 20 is ' + str(sma_20) + ', SMA 50 is ' + str(sma_50) + ' and SMA 100 is ' + str(sma_100))

    if (current > sma_100):
        if (current > sma_20 > sma_50 > sma_100):
            print ('Current price is above SMA 100, SMA 50 and SMA 20. Looks like we are in strong uptrend.')
        else:
            print ('Current price is above SMA 100. Looks like we are in uptrend.')
    else:
        if (current < sma_20 < sma_50 < sma_100):
            print ('Current price is below SMA 100, SMA 50 and SMA 20. Looks like we are in strong downtrend.')
        else:
            print ('Current price is above SMA 100. Looks like we are in downtrend.')

# Exponential Moving Average

def run_ema(data_frame):
    cs.EMA(data_frame, 20)
    cs.EMA(data_frame, 50)
    cs.EMA(data_frame, 100)
    pts.ema_plot(data_frame)

    current = data_frame['close'][499]
    ema_20 = data_frame['EMA_20'][499]
    ema_50 = data_frame['EMA_50'][499]
    ema_100 = data_frame['EMA_100'][499]

    print('Current price is ' + str(current) + ', EMA 20 is ' + str(ema_20) + ', EMA 50 is ' + str(ema_50) + ' and EMA 100 is ' + str(ema_100))
    print()

    if current > ema_100:
        if current > ema_20 > ema_50 > ema_100:
            print ('Current price is above EMA 100, EMA 50 and EMA 20. Looks like we are in strong uptrend.')
        else:
            print ('Current price is above EMA 100. Looks like we are in uptrend.')
    else:
        if current < ema_20 < ema_50 < ema_100:
            print ('Current price is below EMA 100, EMA 50 and EMA 20. Looks like we are in strong downtrend.')
        else:
            print ('Current price is above EMA 100. Looks like we are in downtrend.')

# Relative Strength Index

def run_rsi(data_frame):
    cs.RSI(data_frame)
    pts.rsi_plot(data_frame).show()

    current = data_frame['close'][499]
    rsi = data_frame['rsi'][499]

    print('Current RSI is ' + rsi)
    print()

    if rsi > 70:
        if rsi > 80:
            print('RSI is above 80. The market is extremely overbought and we may expect trend reversal. It may be considered as a strong SELL signal.')
        else:
            print('RSI is above 70. The market is overbought and we may expect trend reversal. It may be considered as a SELL signal.')
    elif rsi < 30:
        if rsi < 20:
            print('RSI is below 20. The market is extremely oversold and we may expect trend reversal. It may be considered as a strong BUY signal.')
        else:
            print('RSI is below 30. The market is oversold and we may expect trend reversal. It may be considered as a BUY signal.')
    else:
        print('RSI is between 30 and 70. There is no clear signal from RSI.')

# Bollinger Bands

def run_boll(data_frame):
    cs.boll_bands(data_frame)
    pts.boll_plot(data_frame).show()

    current = data_frame['close'][499]
    high = data_frame['high'][499]
    low = data_frame['low'][499]
    boll_up = data_frame['close'][499]
    boll_down = data_frame['close'][499]

    if current > boll_up:
        print('Price is currently above Bollinger Bands. It may be considered as a strong SELL signal.')
    elif high > boll_up:
        print('Price reached top Bollinger Band in the last period. It may be considered as a SELL signal.')
    elif current < boll_up:
        print('Price is currently below Bollinger Bands. It may be taken as a strong BUY signal.')
    elif low < boll_down:
        print('Price reached bottom Bollinger Band in the last period. It may be considered as a BUY signal.')
    else:
        print('Price is currently between Bollinger Bands. No clear signals.')

# Momentum

def run_mom(data_frame):
    cs.momentum(data_frame)
    pts.momentum_plot(data_frame).show()

    current = data_frame['close'][499]
    momentum = data_frame['momentum'][499]

    print('Current price is ' + str(current) + ', momentum is ' + str(momentum))

    if (momentum > 0):
        print ('Momentum is currently positive. Seems like we are in an uptrend.')
    else:
        print ('Momentum is currently negative. Seems like we are in an downtrend.')

# Moving Average Convergence / Divergence

def run_macd(data_frame):
    cs.macd(data_frame)
    pts.macd_plot(data_frame).show()

    macd = data_frame['macd_hist'][499]

    if (macd > 0):
        print ('MACD histogram is currently positive. Seems like we are in an uptrend.')
    else:
        print ('MACD histogram is currently negative. Seems like we are in an downtrend.')


# Stochastic RSI

def run_stoch_rsi(data_frame):
    cs.stoch_rsi(data_frame)
    pts.stoch_rsi_plot(data_frame).show()

    current = data_frame['close'][499]
    stoch_rsi = data_frame['stoch_rsi'][499]

    print('Current stochastic RSI is ' + str(stoch_rsi))
    print()

    if stoch_rsi > 70:
        if stoch_rsi > 80:
            print('Stochastic RSI is above 80. The market is extremely overbought and we may expect trend reversal. It may be considered as a strong SELL signal.')
        else:
            print('Stochastic RSI is above 70. The market is overbought and we may expect trend reversal. It may be considered as a SELL signal.')
    elif stoch_rsi < 30:
        if stoch_rsi < 20:
            print('Stochastic RSI is below 20. The market is extremely oversold and we may expect trend reversal. It may be considered as a strong BUY signal.')
        else:
            print('Stochastic RSI is below 30. The market is oversold and we may expect trend reversal. It may be considered as a BUY signal.')
    else:
        print('Stochastic RSI is between 30 and 70. There is no clear signal from Stochastic RSI.')

# Summary
 
def run_summary(data_frame, symbol):
    cs.SMA(data_frame, 20)
    cs.SMA(data_frame, 50)
    cs.SMA(data_frame, 100)    
    cs.EMA(data_frame, 20)
    cs.EMA(data_frame, 50)
    cs.EMA(data_frame, 100)
    cs.boll_bands(data_frame)
    cs.RSI(data_frame)
    cs.macd(data_frame)
    cs.momentum(data_frame)
    cs.stoch_rsi(data_frame)

    print('Brief summary for ' + symbol + ':')
    current = data_frame['close'][499]
    sma_20 = data_frame['SMA_20'][499]
    sma_50 = data_frame['SMA_50'][499]
    sma_100 = data_frame['SMA_100'][499]
    ema_20 = data_frame['EMA_20'][499]
    ema_50 = data_frame['EMA_50'][499]
    ema_100 = data_frame['EMA_100'][499]
    rsi = data_frame['RSI'][499]
    high = data_frame['high'][499]
    low = data_frame['low'][499]
    boll_up = data_frame['close'][499]
    boll_down = data_frame['close'][499]
    momentum = data_frame['momentum'][499]
    macd = data_frame['macd_hist'][499]
    stoch_rsi = data_frame['stoch_rsi'][499]

    if (current > sma_100):
        if (current > sma_20 > sma_50 > sma_100):
            print ('Current price is above SMA 100, SMA 50 and SMA 20. Looks like we are in strong uptrend.')
        else:
            print ('Current price is above SMA 100. Looks like we are in uptrend.')
    else:
        if (current < sma_20 < sma_50 < sma_100):
            print ('Current price is below SMA 100, SMA 50 and SMA 20. Looks like we are in strong downtrend.')
        else:
            print ('Current price is above SMA 100. Looks like we are in downtrend.')

    if current > ema_100:
        if current > ema_20 > ema_50 > ema_100:
            print ('Current price is above EMA 100, EMA 50 and EMA 20. Looks like we are in strong uptrend.')
        else:
            print ('Current price is above EMA 100. Looks like we are in uptrend.')
    else:
        if current < ema_20 < ema_50 < ema_100:
            print ('Current price is below EMA 100, EMA 50 and EMA 20. Looks like we are in strong downtrend.')
        else:
            print ('Current price is above EMA 100. Looks like we are in downtrend.')

    if rsi > 70:
        if rsi > 80:
            print('RSI is above 80. The market is extremely overbought and we may expect trend reversal. It may be considered as a strong SELL signal.')
        else:
            print('RSI is above 70. The market is overbought and we may expect trend reversal. It may be considered as a SELL signal.')
    elif rsi < 30:
        if rsi < 20:
            print('RSI is below 20. The market is extremely oversold and we may expect trend reversal. It may be considered as a strong BUY signal.')
        else:
            print('RSI is below 30. The market is oversold and we may expect trend reversal. It may be considered as a BUY signal.')
    else:
        print('RSI is between 30 and 70. There is no clear signal from RSI.')

    if current > boll_up:
        print('Price is currently above Bollinger Bands. It may be considered as a strong SELL signal.')
    elif high > boll_up:
        print('Price reached top Bollinger Band in the last period. It may be considered as a SELL signal.')
    elif current < boll_up:
        print('Price is currently below Bollinger Bands. It may be taken as a strong BUY signal.')
    elif low < boll_down:
        print('Price reached bottom Bollinger Band in the last period. It may be considered as a BUY signal.')
    else:
        print('Price is currently between Bollinger Bands. No clear signals.')

    if (momentum > 0):
        print ('Momentum is currently positive. Seems like we are in an uptrend.')
    else:
        print ('Momentum is currently negative. Seems like we are in an downtrend.')

    if (macd > 0):
        print ('MACD histogram is currently positive. Seems like we are in an uptrend.')
    else:
        print ('MACD histogram is currently negative. Seems like we are in an downtrend.')

    if stoch_rsi > 70:
        if stoch_rsi > 80:
            print('Stochastic RSI is above 80. The market is extremely overbought and we may expect trend reversal. It may be considered as a strong SELL signal.')
        else:
            print('Stochastic RSI is above 70. The market is overbought and we may expect trend reversal. It may be considered as a SELL signal.')
    elif stoch_rsi < 30:
        if stoch_rsi < 20:
            print('Stochastic RSI is below 20. The market is extremely oversold and we may expect trend reversal. It may be considered as a strong BUY signal.')
        else:
            print('Stochastic RSI is below 30. The market is oversold and we may expect trend reversal. It may be considered as a BUY signal.')
    else:
        print('Stochastic RSI is between 30 and 70. There is no clear signal from Stochastic RSI.')