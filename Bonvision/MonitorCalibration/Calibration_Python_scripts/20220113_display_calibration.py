# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 16:27:12 2022

@author: maria
"""

import numpy as np
import matplotlib.pyplot as plt


#support functions (should be placed in a separate file eventually)

#normalizing the array
def normalize_data(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))


#files location
filePath = "C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//MonitorCalibration//output_files//20220301//"

#files
files = ["Calibration_red_ourLUT","Calibration_green_ourLUT","Calibration_blue_ourLUT"]
#files = ["Calibration_blue1"]


    
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



#plotting all frames to check if they match our expectations
fig, axs = plt.subplots(1, 3, figsize=(30, 9))
axs[0].plot(arrays[0].T)
axs[1].plot(arrays[1].T)
axs[2].plot(arrays[2].T)


fig, axs = plt.subplots(1, 3, figsize=(30, 9))
axs[0].plot(np.mean(arrays[0],1),'o', color= "red")
axs[1].plot(np.mean(arrays[1],1),'o', color="green")
axs[2].plot(np.mean(arrays[2],1),'o', color= "blue")

    

