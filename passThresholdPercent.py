# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 18:05:09 2019

@author: syeh3
"""

def passThresholdPercent(stockData, index, days, threshold):
    
    count = 0
    
    while count <= days:

        absoluteDifference = (stockData['Low'][index + count] - stockData['Open'][index])
        if absoluteDifference/stockData['Open'][index]*100 < threshold:
            return False
    
        count += 1
    
    return True