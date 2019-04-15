# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 15:32:32 2019

@author: syeh3
"""

import macd_opt
import volume
import convertExceltoDataFrame
import returns
import json
from passThresholdPercent import passThresholdPercent as ptp


filename = 'var_three'

convertExceltoDataFrame.convertExcelToDataFrame('historicalstockdata')

stocksDataListOutcome = convertExceltoDataFrame.stocksDataList

with open(filename + '/indices.json') as infile:
    listOfIndices = json.load(infile)

stockReturnsThresholdFailed = {}
stockReturnsExit = {}
stockReturns3 = {}
stockReturns5 = {}
stockReturns10 = {}
stockControlReturns = {}
stockReturnsandDate = {}
stockAngles = {}

threshold = -5

for stock in stocksDataListOutcome:
    print(stock)
    stockData = stocksDataListOutcome[stock]
    macd_opt.macdHistorical(stockData)
    volume.volumeAveHistorical(stockData)
    
    stockReturnsThresholdFailed[stock] = []
    stockReturnsExit[stock] = []
    
    stockReturns3[stock] = []
    stockReturns5[stock] = []
    stockReturns10[stock] = []
    stockReturnsandDate[stock] = []
    stockAngles[stock] = []
    stockControlReturns[stock] = []
    for index in listOfIndices[stock]: 
        if ptp(stockData,index,0,threshold):
            if stockData['MACD Signal Difference'][index + 1] > stockData['MACD Signal Difference'][index]:
                try:
                    if ptp(stockData,index, 3,threshold): 
                        stockReturns3[stock].append(returns.returnsClosetoClose(stockData, index, 3))
                        if ptp(stockData,index, 5,threshold): 
                            stockReturns5[stock].append(returns.returnsClosetoClose(stockData, index, 5))
                            if ptp(stockData,index, 10,threshold): 
                                stockReturns10[stock].append(returns.returnsClosetoClose(stockData, index, 10))
                    else:
                        stockReturnsThresholdFailed[stock].append(threshold)
                        stockReturnsandDate[stock].append([stockData['Date'][index], returns.returnsClosetoClose(stockData, index, 5)])
                except:
                    continue
            else:
               try:
                   stockReturnsExit[stock].append(returns.returnsClosetoClose(stockData, index, 1))
               except:
                    continue
        else:
            #stockReturnsThresholdFailed[stock].append([stockData['Date'][index], threshold])
            stockReturnsThresholdFailed[stock].append(threshold)
            
        stockControlReturns[stock].append(returns.returnsOfFiveDaysClosetoClose(stockData, index))
  
with open(filename + '/thresholdfailed.json', 'w') as outfile:
    json.dump(stockReturnsThresholdFailed, outfile)
    
with open(filename + '/thresholdfailed.txt', 'w') as outfile:
    json.dump(stockReturnsThresholdFailed, outfile)

      
with open(filename + '/returns3.json', 'w') as outfile:
    json.dump(stockReturns3, outfile)
    
with open(filename + '/returns3.txt', 'w') as outfile:
    json.dump(stockReturns3, outfile)
            
with open(filename + '/returns5.json', 'w') as outfile:
    json.dump(stockReturns5, outfile)
    
with open(filename + '/returns5.txt', 'w') as outfile:
    json.dump(stockReturns5, outfile)
    
with open(filename + '/returns10.json', 'w') as outfile:
    json.dump(stockReturns10, outfile)
    
with open(filename + '/returns10.txt', 'w') as outfile:
    json.dump(stockReturns10, outfile)
    
with open(filename + '/returnsandDateMACDSlope.json', 'w') as outfile:
    json.dump(stockReturnsandDate, outfile)
    
with open(filename + '/returnsandDateMACDSlope.txt', 'w') as outfile:
    json.dump(stockReturnsandDate, outfile)
    
with open(filename + '/control.json', 'w') as outfile:
    json.dump(stockControlReturns, outfile)
    
with open(filename + '/control.txt', 'w') as outfile:
    json.dump(stockControlReturns, outfile)
    
with open(filename + '/exitreturnsone.json', 'w') as outfile:
    json.dump(stockReturnsExit, outfile)
    
with open(filename + '/exitreturnsone.txt', 'w') as outfile:
    json.dump(stockReturnsExit, outfile)
    