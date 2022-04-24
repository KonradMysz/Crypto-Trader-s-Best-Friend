class Plots(object):
    """Show plots with indicators"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Simple Candlestick plot

def candle_plot(data_frame):
    figure_1 = go.Candlestick(x=data_frame['open_time'], 
                                            open=data_frame['open'], 
                                            high=data_frame['high'], 
                                            low=data_frame['low'], 
                                            close=data_frame['close'])
    return figure_1

# Candlestick plot with volume barplot

def vol_plot(data_frame):
    figure = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03, 
                           subplot_titles=('Candles', 'Volume'), row_width=[0.2, 0.7])
    figure_1 = candle_plot(data_frame)
    figure_2 = go.Bar(x = data_frame['open_time'], 
                     y=data_frame['volume'], 
                     showlegend=False)
    figure.add_trace(figure_1, row=1, col=1)
    figure.add_trace(figure_2, row=2, col=1)
    figure.update(layout_xaxis_rangeslider_visible=False)
    return figure

# Simple Moving Average

def trace(data_frame, col_name):
    new_trace = go.Scatter(x=data_frame['open_time'], y=data_frame[col_name], mode='lines', name=col_name)
    return new_trace

def sma_plot(data_frame):
    fig_sma = vol_plot(data_frame)
    sma_list = ['SMA_20', 'SMA_50', 'SMA_100']
    for col_name in sma_list:
        fig_sma.add_trace(trace(data_frame, col_name))

    fig_sma.update_layout(title='Simple Moving Averages')

    return fig_sma

# Exponential Moving Average

def ema_plot(data_frame):
    fig_ema = vol_plot(data_frame)
    ema_list = ['EMA_20', 'EMA_50', 'EMA_100']
    for col_name in ema_list:
        fig_ema.add_trace(trace(data_frame, col_name))

    fig_ema.update_layout(title='Exponential Moving Averages')

    return fig_ema

# Relative Strength Index

def rsi_plot(data_frame):
    figure = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03, 
                           subplot_titles=('Candles', 'RSI'), row_width=[0.2, 0.7])
    figure_1 = candle_plot(data_frame)
    figure_2 = go.Scatter(x = data_frame['open_time'], 
                     y=data_frame['RSI'], 
                     showlegend=False)
    figure.add_trace(figure_1, row=1, col=1)
    figure.add_trace(figure_2, row=2, col=1)
    figure.update(layout_xaxis_rangeslider_visible=False)
    figure.update_layout(title='Relative Strength Index')
    return figure

# Bollinger Bands

def boll_plot(data_frame):
    fig_boll = vol_plot(data_frame)
    boll_list = ['SMA_20', 'boll_up', 'boll_down']
    for col_name in boll_list:
        fig_boll.add_trace(trace(data, col_name))

    fig_boll.update_layout(title='Bollinger Bands')
    return fig_boll

# Momentum

def momentum_plot(data_frame):
    figure = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03, 
                           subplot_titles=('Candles', 'Momentum'), row_width=[0.2, 0.7])
    figure_1 = candle_plot(data_frame)
    figure_2 = go.Scatter(x = data_frame['open_time'], 
                     y=data_frame['momentum'], 
                     showlegend=False)
    figure.add_trace(figure_1, row=1, col=1)
    figure.add_trace(figure_2, row=2, col=1)
    figure.update(layout_xaxis_rangeslider_visible=False)
    return figure

# Moving Average Convergence / Divergence

def macd_plot(data_frame):
    figure = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.03, 
                           subplot_titles=('Candles', 'MACD'), row_width=[0.1, 0.1, 0.7])
    figure_1 = candle_plot(data_frame)
    figure_2 = go.Scatter(x = data_frame['open_time'], 
                     y=data_frame['macd'], 
                     showlegend=False)
    figure_3 = go.Scatter(x = data_frame['open_time'], 
                     y=data_frame['signal'], 
                     showlegend=False)
    figure_4 = go.Bar(x = data_frame['open_time'], 
                     y=data_frame['macd_hist'], 
                     showlegend=False)
    figure.add_trace(figure_1, row=1, col=1)
    figure.add_trace(figure_2, row=2, col=1)
    figure.add_trace(figure_3, row=2, col=1)
    figure.add_trace(figure_4, row=3, col=1)
    figure.update(layout_xaxis_rangeslider_visible=False)
    figure.update_layout(title='Moving Average Convergence / Divergence')
    return figure

# Stochastic RSI

def stoch_rsi_plot(data_frame):
    figure = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03, 
                           subplot_titles=('Candles', 'Stoch RSI'), row_width=[0.2, 0.7])
    figure_1 = candle_plot(data_frame)
    figure_2 = go.Scatter(x = data_frame['open_time'], 
                     y=data_frame['stoch_rsi'], 
                     showlegend=False)
    figure_3 = go.Scatter(x = data_frame['open_time'], 
                     y=data_frame['stoch_rsi_sma'], 
                     showlegend=False)
    figure.add_trace(figure_1, row=1, col=1)
    figure.add_trace(figure_2, row=2, col=1)
    figure.add_trace(figure_3, row=2, col=1)
    figure.update(layout_xaxis_rangeslider_visible=False)
    figure.update_layout(title='Stochastic RSI')
    return figure