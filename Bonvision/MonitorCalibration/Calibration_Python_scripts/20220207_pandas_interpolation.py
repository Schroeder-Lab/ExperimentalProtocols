# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 16:30:14 2022

@author: maria
"""

import numpy as np
import pandas as pd

def f(x):
    return x.interpolate(method='spline', order=2)

b=pd.Series([0.303169,0.303871,0.302602,0.351127,0.450659,0.543382,0.646193, 0.748551,0.796879])
y=pd.Series([0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])

blue= b.interpolate(method='spline', order=2)

range_of_xvaluesg=[]
range_of_xvaluesb= []
range_of_xvaluesr=[]
for x in np.arange(0,0.9,0.003515625):
    range_of_xvaluesg.append(blue)


