# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 18:05:09 2019

@author: syeh3

"""

def passThresholdPercent(stockData, index, days, threshold):
    """Returns True if absolute difference between start index and each day
    up to number of total days is greater than or equal to threshold returns
    Returns False otherwise"""
    count = 0
    
    while count <= days:

        absoluteDifference = (stockData['Low'][index + count] - stockData['Open'][index])
        if absoluteDifference/stockData['Open'][index]*100 < threshold:
            return False
    
        count += 1
    
    return True
