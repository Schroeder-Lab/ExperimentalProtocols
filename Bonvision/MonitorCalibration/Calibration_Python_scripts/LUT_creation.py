# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 16:30:14 2022

@author: maria
"""

"""
This script creates the LUT which needs to be plugged into the Gamma calibration node in Bonsai
"""

import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from scipy import interpolate

# def f(x):
#    return x.interpolate(method='spline', order=2)

#blue

#x=np.array([0.303169,0.303871,0.302602,0.351127,0.450659,0.543382,0.646193, 0.748551,0.796879])
x=np.linspace(0, 1, num=9, endpoint=True)
yb=np.array([0.303169,0.303871,0.302602,0.351127,0.450659,0.543382,0.646193, 0.748551,0.796879])
yg=np.array([0.138527,0.148473,0.232025,0.32446,0.425474,0.551284,0.617042,0.712612,0.7606])
yr= np.array([0.477334,0.47928,0.476698,0.478122,0.478116,0.4784,0.477776,0.478171,0.478511])

# fb = interp1d(x, yb, kind='cubic')
# fg= interp1d(x, yg, kind='cubic')
# fr=interp1d(x, yr, kind='cubic')

fb = interpolate.InterpolatedUnivariateSpline(x, yb)
fg= interpolate.InterpolatedUnivariateSpline(x, yg)
fr=interpolate.InterpolatedUnivariateSpline(x, yr)


xnew = np.linspace(0, 1, num=256, endpoint=True)



# plt.plot(x, yb, 'o', xnew, fb(xnew), '--')
# plt.legend(['data', 'cubic'], loc='best')
# plt.show()

ipb=fb(xnew)
ipg= fg(xnew)
ipr=fr(xnew)

# plt.plot(ipb, color="blue")
# plt.plot(ipg, color="green")
# plt.plot(ipr, color="red")

arrayrgb= np.dstack((ipr, ipg, ipb))
plt.imshow(arrayrgb)
plt.axis('off')
#plt.imsave('C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//MonitorCalibration//LUTs//ourLUTrgb20220208b.jpg', arrayrgb)

# blue= b.interpolate(method='spline', order=2)

# range_of_xvaluesg=[]
# range_of_xvaluesb= []
# range_of_xvaluesr=[]
# for x in np.arange(0,0.9,0.003515625):
#     range_of_xvaluesg.append(blue)


