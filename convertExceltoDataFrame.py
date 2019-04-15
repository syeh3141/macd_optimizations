# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 19:52:53 2018

@author: syeh3

Function for converting Excelt to Pandas DataFrame type
"""

import os
import pandas as pd
import time

stocksDataList = {}

def convertExcelToDataFrame(fileName):

    count = 0
    
    timeStart = time.time()
    
    print(timeStart)
    
    for stock in os.listdir(fileName):
        
        fullFileName = fileName + '/' + stock
        
        print(count)
        
        #pd.read_csv(fileName)
        #stocksDataList[stock[:len(stock)-4]] = pd.read_csv(fileName)
        
        stocksDataList[stock[:len(stock)-4]] = pd.io.parsers.read_csv(fullFileName)
        
        count += 1
        
    print(time.time() - timeStart)
        

