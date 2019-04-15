# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 17:50:29 2019

@author: syeh3
Prints out returns to the console of Spyder IDE
"""

from returns import returnsFromJson as rfj

def printReturns(folder):
    
    print("Control Returns")
    rfj(folder + "/control")
    
    print("\n")
    print("\n")
    
    print("Exit Early Returns")
    rfj(folder + "/exitreturnsone")
    
    print("\n")
    print("\n")
    
    print("3 Day Returns")
    rfj(folder + "/returns3")
    
    print("\n")
    print("\n")
    
    print("5 Day Returns")
    rfj(folder + "/returns5")
    
    print("\n")
    print("\n")
    
    print("10 Day Returns")
    rfj(folder + "/returns10")
    
    print("\n")
    print("\n")
    
    print("Threshold Failed Returns")
    rfj(folder + "/thresholdfailed")
