# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 08:09:10 2022

@author: chris
"""

def dividend(a):
    stock_name = "SPY" #stock name
    investment_amount = a #investment amount in dollars 
    dividend_rate = 1.50 #yearly dividend rate 
    market_price = 400.38 #current markeyprice of stock 
    return print (stock_name, investment_amount * dividend_rate / market_price )
dividend(5000) #74.9288176232579
dividend(7000) #104.90034467256106
dividend(10000) #149.8576352465158
