# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:57:28 2018

@author: syeh3

Optimizes each PandasFrame stock data and finds the index of MACD Crossover for each
Dumps json into folder 'var_one'
"""

import json
import convertExceltoDataFrame
import macd_opt
import volume


convertExceltoDataFrame.convertExcelToDataFrame('historicalstockdata')
stocksDataListOutcome = convertExceltoDataFrame.stocksDataList
stockIndices = {}

for stock in stocksDataListOutcome:
    print(stock)
    stockData = stocksDataListOutcome[stock]
    macd_opt.macdHistorical(stockData)
    volume.volumeAveHistorical(stockData)
    stockIndices[stock] = macd_opt.findHistoricalMACDCrossovers(stockData)

filename = 'var_one'

with open(filename + '/indices.json', 'w') as outfile:
    json.dump(stockIndices, outfile)
    
with open(filename + '/indices.txt', 'w') as outfile:
    json.dump(stockIndices, outfile)
