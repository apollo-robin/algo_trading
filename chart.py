# -*- coding: utf-8 -*-
"""
Created on Mon May 24 00:38:17 2021

@author: robin
"""
#Importing required libraries
import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import ta

#Function to download the Stock Price Data
@st.cache(allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def load_stock_data(exchng,Ticker,period, interval):
    if exchng =='NSE':
        if Ticker == 'NIFTY 50':
            Ticker = '^NSEI'
        elif Ticker == 'NIFTY BANK':
            Ticker = '^NSEBANK'
        else:
            Ticker = Ticker + '.NS'
    if exchng == 'BSE':
        if Ticker == 'SENSEX':
            Ticker = '^BSESN'
        else:
            Ticker = Ticker + '.BO'
    Stock = yf.download(Ticker, period = period, interval = interval)
    if Stock.empty:
        st.error(Ticker +': '+yf.shared._ERRORS[Ticker])
        st.stop()      
    return Stock
    
#Function to download the Stock Price Data
@st.cache(allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def get_financial(exchng,Ticker):
    if Ticker == 'NIFTY 50' or Ticker == 'NIFTY BANK' or Ticker == 'SENSEX':
        st.info("Financials not available for Indices. Please select a company to get the financial data")
        st.stop()
    if exchng =='NSE':
        Ticker = Ticker + '.NS'
    else :
        Ticker = Ticker + '.BO'
    Stock = yf.Ticker(Ticker)
        
    return Stock

def draw_chart(exchng, Stock, chart_type, ticker, interval):
    if exchng =='NSE':
        plot_title = ticker+ ' . '+interval+' . NSE' 
    if exchng == 'BSE':
        plot_title = ticker+ ' . '+interval+' . BSE' 
        
    if chart_type == "Candlestick":
        candles = go.Candlestick(x=Stock.index, open=Stock.Open, high=Stock.High, low=Stock.Low, close=Stock.Close, increasing_line_color= 'rgb(38,166,154)', decreasing_line_color= 'rgb(239,83,80)', increasing_fillcolor= 'rgb(38,166,154)', decreasing_fillcolor= 'rgb(239,83,80)',line_width = 1,showlegend = False)
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(candles) 
        fig.update_layout(title=plot_title,height=600, xaxis_rangeslider_visible=False,  legend = dict(yanchor="top",y = -0.1,xanchor="left", x=0.01,orientation="h")) 
        
    else :
        line = go.Scatter(x=Stock.index, y=Stock.Close, line=dict(color='rgb(61,162,244)',width = 2), name = 'Close' )
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(line)
        fig.update_layout(title=plot_title,height=600,legend = dict(yanchor="top",y = -0.1,xanchor="left", x=0.01,orientation="h")) 
    
    return fig

def add_trace(fig, traces,widget1, widget2, widget3, Stock):
    
    
    if "Short Moving Average" in traces:
        SMA_source = widget1.selectbox("SMA Source",["Close","Open","High","Low"])
        SMA_window = widget2.number_input("SMA Window",value = 30, key = 1)
        Stock['SMA'] = Stock[SMA_source].rolling(window = SMA_window).mean()
        SMA = go.Scatter(x=Stock.index, y=Stock.SMA,  line=dict(color='rgb(61,162,244)',width = 1.2), name = 'SMA')
        fig.add_trace(SMA)

    if "Long Moving Average" in traces:
        LMA_source = widget1.selectbox("LMA Source",["Close","Open","High","Low"])
        LMA_window = widget2.number_input("LMA Window",value = 50, key = 2)
        Stock['LMA'] = Stock[LMA_source].rolling(window = LMA_window).mean()
        LMA = go.Scatter(x=Stock.index, y=Stock.LMA, line=dict(color='rgb(161, 224, 88)',width = 1.2), name = 'LMA')
        fig.add_trace(LMA)
            
    if "Exponential Moving Average" in traces:
        EMA_source = widget1.selectbox("EMA Source",["Close","Open","High","Low"])
        EMA_span = widget2.number_input("EMA Window",value = 13, key = 3)
        Stock['EMA'] = Stock[EMA_source].ewm(span= EMA_span, adjust= False).mean()
        EMA = go.Scatter(x=Stock.index, y=Stock.EMA,  line=dict(color='rgb(192, 109,237)',width = 1.2), name = 'EMA')
        fig.add_trace(EMA)
        
    if "MACD" in traces:
        MACD_source = widget1.selectbox("MACD Source",["Close","Open","High","Low"])
        MACD_short_span = widget2.number_input("MACD Short Window",value = 12,  key = 4)
        MACD_long_span = widget3.number_input("MACD Long Window",value = 26,  key = 5)
        # Calculate the Exponential Moving Average
        Stock['ShortEMA'] = Stock[MACD_source].ewm(span = MACD_short_span, adjust = False).mean()
        Stock['LongEMA'] = Stock[MACD_source].ewm(span = MACD_long_span, adjust = False).mean()
        #Calculate the MACD line 
        Stock['MACD'] = Stock['ShortEMA'] - Stock['LongEMA']
        MACD = go.Scatter(x=Stock.index, y=Stock.MACD, line=dict(color='rgb(27, 130, 9)',width = 1.2), name = 'MACD')
        fig.add_trace(MACD,secondary_y=True)
       

    if "MACD Signal" in traces:
        if not "MACD" in traces:
            MACD_source = widget1.selectbox("MACD Source",["Close","Open","High","Low"])
            MACD_short_span = widget2.number_input("MACD Short Window",value = 12,  key = 6)
            MACD_long_span = widget3.number_input("MACD Long Window",value = 26, key= 7 )
            
        MACD_signal_span = widget3.number_input("MACD Signal Smooth",value = 9, key = 8)
        # Calculate the Exponential Moving Average
        Stock['ShortEMA'] = Stock[MACD_source].ewm(span = MACD_short_span, adjust = False).mean()
        Stock['LongEMA'] = Stock[MACD_source].ewm(span = MACD_long_span, adjust = False).mean()
        # Calculate the MACD line 
        Stock['MACD'] = Stock['ShortEMA'] - Stock['LongEMA']
        Stock['MACD_Signal'] = Stock['MACD'].ewm(span= MACD_signal_span, adjust = False).mean()
        MACD_Signal = go.Scatter(x=Stock.index, y=Stock.MACD_Signal, line=dict(color='rgb(230, 69, 67)',width = 1.2), name = 'MACD Signal')
        fig.add_trace(MACD_Signal,secondary_y=True)
        
    if "RSI" in traces:
        RSI_source = widget1.selectbox("RSI Source",["Close","Open","High","Low"])
        RSI_period = widget2.number_input("RSI Period",value = 14, key = 9)
        Stock['RSI'] = ta.momentum.RSIIndicator(Stock[RSI_source], window = RSI_period).rsi()
        RSI = go.Scatter(x=Stock.index, y=Stock.RSI,  line=dict(color='rgb(163, 81, 240)',width = 1.2), name = 'RSI')
        fig.add_trace(RSI,secondary_y= True)
        fig.add_hrect(y0=33.33, y1=66.67,fillcolor='rgb(163, 81, 240)', opacity=0.2, secondary_y=True) 

def add_compare(fig,exchng,Ticker,period, interval):
    Stock = load_stock_data(exchng,Ticker,period, interval)
    Stock = (Stock.div(Stock.Close[0]) - 1).div(0.01)
    line = go.Scatter(x=Stock.index, y=Stock.Close, line=dict(width = 1.2), name = Ticker )
    fig.add_trace(line)
    
        
def buy_signal(Stock, fig , strategy):
    buy_trace = go.Scatter(x=Stock.index, y=Stock.BUY, mode ='markers', marker_symbol = 'triangle-up', marker_color = 'green', marker_size= 10, name = strategy+' BUY')
    fig.add_trace(buy_trace)
    
            
def sell_signal(Stock, fig, strategy):
    sell_trace = go.Scatter(x=Stock.index, y=Stock.SELL, mode ='markers', marker_symbol = 'triangle-down', marker_color = 'red', marker_size= 10, name = strategy+' SELL')
    fig.add_trace(sell_trace)   
    