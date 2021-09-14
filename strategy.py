# -*- coding: utf-8 -*-
"""
Created on Sat May 22 01:44:59 2021

@author: robin
"""
import pandas as pd
import numpy as np
import math 
import ta
import datetime
import streamlit as st

@st.cache(allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def ma44(data):
    data['44MA'] = data['Close'].rolling(window= 44).mean()
    sigBUY = []
    
    # Signal when to buy 
    for i in range (len(data)):
        if len(data)>3:
            if (data['44MA'][i] > (data['44MA'][i-1]+data['44MA'][i-2]+data['44MA'][i-3])/3 ) :
                if data['Open'][i] < data['Close'][i]:
                    if ( abs(data['44MA'][i] - data['Low'][i]) < 4 and data['44MA'][i] < data['Open'][i]):
                        sigBUY.append(data['Close'][i])
                    else:
                        sigBUY.append(np.nan)
                else:
                    sigBUY.append(np.nan)
            else:
                sigBUY.append(np.nan)
        else:
            if (data['44MA'][i] > data['44MA'][i-1]) :
                if data['Open'][i] < data['Close'][i]:
                    if ( abs(data['44MA'][i] - data['Low'][i]) < 4 and data['44MA'][i] < data['Open'][i]):
                        sigBUY.append(data['Close'][i])
                    else:
                        sigBUY.append(np.nan)
                else:
                    sigBUY.append(np.nan)
            else:
                sigBUY.append(np.nan)
            
            
    data['BUY'] = sigBUY
    Date = []
    BuyPrice=[]
    Quantity = []
    StopLoss =[]
    Target =[]
    Risk = 1000
    data = data.reset_index()
   
    #Calculate buying details
    for i in range(len(data)):
        if math.isnan(data['BUY'][i]):
            continue
        else:
            Date.append(data.iloc[:,0][i]+ datetime.timedelta(days=1))
            price = math.ceil(data['Close'][i])
            stoploss = min(data['Low'][i], data['Low'][i-1])
            diff = price - stoploss
            
            BuyPrice.append(price)
            StopLoss.append(stoploss)
            Quantity.append(math.floor(Risk / diff))
            Target.append(price + 2*diff)
    
    
    buy_df = pd.DataFrame({'Date':Date, 'Buy Price': BuyPrice,
                     'Stop Loss': StopLoss, 'Target': Target, 'Quantity': Quantity})

            
    return buy_df , sigBUY


@st.cache(allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def ma_crossover(data):
    sigPriceBuy = []
    sigPriceSell = []
    flag = -1 
    
    data['SMA30'] = data['Close'].rolling(window= 30).mean()
    data['SMA100'] = data['Close'].rolling(window= 100).mean()
    for i in range (len(data)):
        if data['SMA30'][i] > data['SMA100'][i]:
            if flag != 1:
                sigPriceBuy.append(data['Close'][i])
                sigPriceSell.append(np.nan)
                flag = 1
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        elif data['SMA30'][i] < data['SMA100'][i]:
            if flag != 0:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(data['Close'][i])
                flag = 0
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        else:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)
    
    data['BUY'] = sigPriceBuy
    data['SELL'] = sigPriceSell
    
    Date = []
    BuyPrice = []
    SellPrice = []

    
    data = data.reset_index()
    for i in range(len(data)):
        if math.isnan(data['SELL'][i]):
            if math.isnan(data['BUY'][i]):
                continue
            else:
                Date.append(data.iloc[:,0][i]+ datetime.timedelta(days=1))
                SellPrice.append(np.nan)
                BuyPrice.append(data['Close'][i])
        else:
            Date.append(data.iloc[:,0][i]+ datetime.timedelta(days=1))
            SellPrice.append(data['Close'][i])
            BuyPrice.append(np.nan)            
    
    
    buy_df = pd.DataFrame({'Date':Date, 'Buy Price': BuyPrice, 'Sell Price': SellPrice})
    return buy_df, sigPriceBuy, sigPriceSell
    

@st.cache(allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def macd_crossover(data):
    data['MACD'] = ta.trend.MACD(data['Close'],window_slow=26, window_fast=12, window_sign=9).macd()
    data['SIGNAL'] = ta.trend.MACD(data['Close'],window_slow=26, window_fast=12, window_sign=9).macd_signal()
    
    sigPriceBuy = []
    sigPriceSell = []
    flag = -1 
    
    for i in range (len(data)):
        if data['MACD'][i] > data['SIGNAL'][i]:
            if flag != 1:
                sigPriceBuy.append(data['Close'][i])
                sigPriceSell.append(np.nan)
                flag = 1
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        elif data['MACD'][i] < data['SIGNAL'][i]:
            if flag != 0:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(data['Close'][i])
                flag = 0
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        else:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)
    
    data['BUY'] = sigPriceBuy
    data['SELL'] = sigPriceSell
    
    Date = []
    BuyPrice = []
    SellPrice = []
   
    
    data = data.reset_index()
    for i in range(len(data)):
        if math.isnan(data['SELL'][i]):
            if math.isnan(data['BUY'][i]):
                continue
            else:
                Date.append(data.iloc[:,0][i]+ datetime.timedelta(days=1))
                SellPrice.append(np.nan)
                BuyPrice.append(data['Close'][i])
        else:
            Date.append(data.iloc[:,0][i]+ datetime.timedelta(days=1))
            SellPrice.append(data['Close'][i])
            BuyPrice.append(np.nan)            
    
    
    buy_df = pd.DataFrame({'Date':Date, 'Buy Price': BuyPrice, 'Sell Price': SellPrice})
    
       
    return buy_df, sigPriceBuy, sigPriceSell
    
    
    
    return

@st.cache(allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def rsi(data):
    data['RSI'] = ta.momentum.RSIIndicator(data['Close'], window = 14).rsi()
    sigPriceBuy = []
    sigPriceSell = []
    flag = -1 
    
    for i in range (len(data)):
        if data['RSI'][i] >= 33.33 and data['RSI'][i-1] < 33.33:
            if flag != 1:
                sigPriceBuy.append(data['Close'][i])
                sigPriceSell.append(np.nan)
                flag = 1
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        elif data['RSI'][i] <= 66.67 and data['RSI'][i-1] > 66.67:
            if flag != 0:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(data['Close'][i])
                flag = 0
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        else:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)
    
    data['BUY'] = sigPriceBuy
    data['SELL'] = sigPriceSell
    
    Date = []
    BuyPrice = []
    SellPrice = []
   
    
    data = data.reset_index()
    for i in range(len(data)):
        if math.isnan(data['SELL'][i]):
            if math.isnan(data['BUY'][i]):
                continue
            else:
                Date.append(data.iloc[:,0][i]+ datetime.timedelta(days=1))
                SellPrice.append(np.nan)
                BuyPrice.append(data['Close'][i])
        else:
            Date.append(data.iloc[:,0][i]+ datetime.timedelta(days=1))
            SellPrice.append(data['Close'][i])
            BuyPrice.append(np.nan)            
    
    
    buy_df = pd.DataFrame({'Date':Date, 'Buy Price': BuyPrice, 'Sell Price': SellPrice})
    
       
    return buy_df, sigPriceBuy, sigPriceSell
    