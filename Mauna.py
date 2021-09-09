#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 18:07:48 2021

@author: nate_mac
"""

import numpy as np
from matplotlib import pyplot as plt 
from datetime import datetime
import pandas as pd
CO2_ppm_MaunaLoa = np.load("Mauna_CO2.npy")

#print(CO2_ppm_MaunaLoa)

#dates = pd.date_range(start="1981-01-01",periods=230,freq='14D')



y = CO2_ppm_MaunaLoa
x = np.arange(0, 3214, 14)







#plt.plot(dates,y,'.') 
plt.plot(x,y,'.')
m, b = np.polyfit(x, y, 1)

slope = m * 365
plt.plot(x, m*x + b)
#plt.savefig("plot.png")

print(slope)

plt.title("CO2 parts/million, rate of") 
plt.xlabel("Days") 
plt.ylabel("CO2 Concentration") 

plt.show()

