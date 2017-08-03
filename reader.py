# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 21:30:51 2017

@author: davecrob
"""
from yahoo_finance import Share

apple = Share('AAPL')
print(apple.get_price())