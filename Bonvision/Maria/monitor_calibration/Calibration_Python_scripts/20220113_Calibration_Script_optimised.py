# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 09:09:37 2022 by Maria
Updated on Tue Jan 11 23:13:55 2022 by Andre
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import PIL

#support functions (should be placed in a separate file eventually)

#normalizing the array
def normalize_data(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))



def f(x):
    return interpolate.splev(x, tck)

def m(row):
    return np.mean(row)


#files location
filePath = "C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//Maria//monitor_calibration//output_files//beforeC//"

#files
files = ["Calibration_red1","Calibration_green1","Calibration_blue1"]


start = 4000
step = 2000
end = 22000
arrays = list()
fig, axs = plt.subplots(1, 1, figsize=(30, 9))
for item in files:
    temp = np.fromfile(filePath+item,dtype='float64')    
    temp = normalize_data(temp)
    axs.plot(temp)
    temp = np.reshape(temp[start:end:1], (-1,step))
    arrays.append(temp)

y_points= [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]



#make the loop give you the mean values for all two colours, then use the interpolation function
#after interpol. save the values in a variable and use these values to plot the colours, use plt.imshow

g = [m(arrays[1][0]),m(arrays[1][1]),m(arrays[1][2]),m(arrays[1][3]), m(arrays[1][4]), m(arrays[1][5]),m(arrays[1][6]),m(arrays[1][7]),m(arrays[1][8])]
b = [m(arrays[2][0]),m(arrays[2][1]),m(arrays[2][2]),m(arrays[2][3]), m(arrays[2][4]), m(arrays[2][5]),m(arrays[2][6]),m(arrays[2][7]),m(arrays[2][8])]



    
    
#interpolation    

tck = interpolate.splrep(g, y_points)

range_of_xvaluesg=[]

for x in np.arange(0,0.9,0.01):
    range_of_xvaluesg.append(f(x))
    
range_of_yvalues=[]
for y in np.arange(0,0.9,0.01):
    range_of_yvalues.append(y)

    
#trying to figur eout how to make imshow work
#first RGB values here
# first_value= (0, 0.03, 0.05)
# first= plt.imsave(fname='C://Users//maria//Documents//GitHub//Monitor_calibration//first', arr=first_value)

#trying out a different module for this

PIL.save('C://Users//maria//Documents//GitHub//Monitor_calibration//g')

#plt.imshow(0, 0.029395561187219303, 0.04714912534373198)

# plt.show()

#plotting all frames to check if they match our expectations
# fig, axs = plt.subplots(1, 3, figsize=(30, 9))
# axs[0].plot(arrays[0].T)
# axs[1].plot(arrays[1].T)
# axs[2].plot(arrays[2].T)


# fig, axs = plt.subplots(1, 3, figsize=(30, 9))
# axs[0].plot(np.mean(arrays[0],1),'o', color= "red")
# axs[1].plot(np.mean(arrays[1],1),'o', color="green")
# axs[2].plot(np.mean(arrays[2],1),'o', color= "blue")
