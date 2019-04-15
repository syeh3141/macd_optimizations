# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 15:30:19 2019

@author: syeh3
Methods needed for MACD calculations
Optimization constraints and finding the indices of MACD crossovers
"""

def macdHistorical(stock):
    """Creates necessary PandasFrame columns for each stock"""
    stock['EMA 26'] = stock['Close'].ewm(span = 26).mean()
    
    stock['EMA 12'] = stock['Close'].ewm(span = 12).mean()
    
    stock['MACD Line'] = stock['EMA 12'] - stock['EMA 26']
    
    stock['Signal Line'] = stock['MACD Line'].ewm(span = 9).mean()
    
    stock['MACD Signal Difference'] = stock['MACD Line'] - stock['Signal Line']




def optimizationConstraintsMACDTwoDayCheck(stock, index):
    """Optimize for MACD"""
    
    if stock['MACD Signal Difference'][index] < 0 and stock['Close'][index] >= 10 and stock['Volume SMA'][index] >= 10000:
        if stock['MACD Signal Difference'][index + 1] > 0:
            if stock['Volume'][index + 1] > 0.85*stock['Volume SMA'][index + 1] and stock['Volume'][index] > 0.85*stock['Volume SMA'][index]:
                #changed to 0.75 multiplier
                return True
            

def findHistoricalMACDCrossovers(stock):
    """Returns the indices where MACD Crossovers occur in historical data"""
    
    index = 1 
    listOfIndices = []
    while index < len(stock['Close']) - 10:
        if optimizationConstraintsMACDTwoDayCheck(stock, index):
            listOfIndices.append(index + 1)
        index += 1
    return listOfIndices
