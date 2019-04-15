# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 19:05:18 2018

@author: syeh3
Methods to compute volume
"""

def volumeAve(stock):
    """Creates column in Pandas DataFrame for Volume"""
    stock['Volume SMA'] = stock['volume'].rolling(50).mean()
    
def volumeAveHistorical(stock):
    """Creates column in Pandas DataFrame for Volume"""
    stock['Volume SMA'] = stock['Volume'].rolling(50).mean()
