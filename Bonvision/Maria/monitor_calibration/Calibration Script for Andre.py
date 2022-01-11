# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 09:09:37 2022

@author: maria
"""

import numpy as np
import matplotlib.pyplot as plt

#loading file
#file_path= "C://Users//maria//Desktop//PhD//Code//Calibration_blue3"
file_path_b= "C://MyPrograms//Bonvision//output//Calibration_blue9"
file_path_g= "C://MyPrograms//Bonvision//output//Calibration_green0"
file_path_r= "C://MyPrograms//Bonvision//output//Calibration_red0"
#formatting file into array
array_b= np.fromfile(file_path_b,dtype='float64')
array_g= np.fromfile(file_path_g,dtype='float64')
array_r= np.fromfile(file_path_r,dtype='float64')

#normalizing the array
def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

norm_array_b=  NormalizeData(array_b)
norm_array_g=  NormalizeData(array_g)
norm_array_r=  NormalizeData(array_r)

#getting the values per frame which contained different shadings of the respective colours
#there are steps of 2000 because the sample rate was 1000 and each frame was shown for 2s
#first 4000 steps removed due to a max saturation frame which would appear at the start for some unexplainable reason (tried to remove it in Bonsai script but didn't work)
#blue
frame2_b= np.mean(norm_array_b[4000:5999])
frame3_b= np.mean(norm_array_b[6000:7999])
frame4_b=np.mean(norm_array_b[8000:9999])
frame5_b= np.mean(norm_array_b[10000:11999])
frame6_b= np.mean(norm_array_b[12000:13999])
frame7_b= np.mean(norm_array_b[14000:15999])
frame8_b= np.mean(norm_array_b[16000:17999])
frame9_b= np.mean(norm_array_b[18000:19999])
frame10_b= np.mean(norm_array_b[20000:21999])

#green
frame2_g= np.mean(norm_array_g[4000:5999])
frame3_g= np.mean(norm_array_g[6000:7999])
frame4_g=np.mean(norm_array_g[8000:9999])
frame5_g= np.mean(norm_array_g[10000:11999])
frame6_g= np.mean(norm_array_g[12000:13999])
frame7_g= np.mean(norm_array_g[14000:16999])
frame8_g= np.mean(norm_array_g[16000:17999])
frame9_g= np.mean(norm_array_g[18000:19999])
frame10_g= np.mean(norm_array_g[20000:21999])

#red
frame2_r= np.mean(norm_array_r[4000:5999])
frame3_r= np.mean(norm_array_r[6000:5999])
frame4_r=np.mean(norm_array_r[8000:9999])
frame5_r= np.mean(norm_array_r[10000:11999])
frame6_r= np.mean(norm_array_r[12000:13999])
frame7_r= np.mean(norm_array_r[14000:15999])
frame8_r= np.mean(norm_array_r[16000:17999])
frame9_r= np.mean(norm_array_r[18000:19999])
frame10_r= np.mean(norm_array_r[20000:21999])

#loading all frames into an array
b= np.array([frame2_b, frame3_b, frame4_b, frame5_b, frame6_b, frame7_b, frame8_b, frame9_b, frame10_b], dtype='float64')
g= np.array([frame2_g, frame3_g, frame4_g, frame5_g, frame6_g, frame7_g, frame8_g, frame9_g, frame10_g], dtype='float64')
r= np.array([frame2_r, frame3_r, frame4_r, frame5_r, frame6_r, frame7_r, frame8_r, frame9_r, frame10_r], dtype='float64')

#potting all frames to check if they match our expectations
plt.plot(r)
plt.plot(g)
plt.plot(b)