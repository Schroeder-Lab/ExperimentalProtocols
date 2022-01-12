# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 09:09:37 2022 by Maria
Updated on Tue Jan 11 23:13:55 2022 by Andre
"""

import numpy as np
import matplotlib.pyplot as plt


#support functions (should be placed in a separate file eventually)

#normalizing the array
def normalize_data(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

#files location
filePath = "C://Maria//output//"
#filePath = "data//"
#files
files = ["Calibration_red_no_red","Calibration_green0","Calibration_blue9"]

start = 4000
step = 2000
end = 22000

arrays = list()
for item in files:
    temp = np.fromfile(filePath+item,dtype='float64')
    temp = normalize_data(temp)
    temp = np.reshape(temp[start:end], (step,-1))
    arrays.append(temp)





#plotting all frames to check if they match our expectations
fig, axs = plt.subplots(1, 3, figsize=(30, 9))
axs[0].plot(arrays[0])
axs[1].plot(arrays[1])
axs[2].plot(arrays[2])

mean_red= np.mean(arrays[0,1,2])
