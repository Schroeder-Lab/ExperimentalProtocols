# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:37:38 2022

@author: maria
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#support functions (should be placed in a separate file eventually)

#normalizing the array
def normalize_data(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))


#files location
filePath = "C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//MonitorCalibration//output_files//20220301//"

#files
files = ["Calibration_red_grayLUT","Calibration_green_grayLUT","Calibration_blue_grayLUT"]
#files = ["Calibration_red1","Calibration_green1","Calibration_blue1"]

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
# fig, axs = plt.subplots(1, 3, figsize=(30, 9))
# axs[0].plot(arrays[0].T)
# axs[1].plot(arrays[1].T)
# axs[2].plot(arrays[2].T)


# fig, axs = plt.subplots(1, 3, figsize=(30, 9))
# axs[0].plot(np.mean(arrays[0],1),'o', color= "red")
# axs[1].plot(np.mean(arrays[1],1),'o', color="green")
# axs[2].plot(np.mean(arrays[2],1),'o', color= "blue")

blue= np.mean(arrays[2],1)
x= np.array([0,1,2,3,4,5,6,7,8]).reshape((-1,1))

model = LinearRegression().fit(x, blue)
r_sq = model.score(x, blue)
print('coefficient of determination:', r_sq)
