# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 16:07:48 2021

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
frame2_b= np.mean(norm_array_b[4001:6000])
frame3_b= np.mean(norm_array_b[6001:8000])
frame4_b=np.mean(norm_array_b[8001:10000])
frame5_b= np.mean(norm_array_b[10001:12000])
frame6_b= np.mean(norm_array_b[12001:14000])
frame7_b= np.mean(norm_array_b[14001:16000])
frame8_b= np.mean(norm_array_b[16001:18000])
frame9_b= np.mean(norm_array_b[18001:20000])
frame10_b= np.mean(norm_array_b[20001:22000])

#green
frame2_g= np.mean(norm_array_g[4001:6000])
frame3_g= np.mean(norm_array_g[6001:8000])
frame4_g=np.mean(norm_array_g[8001:10000])
frame5_g= np.mean(norm_array_g[10001:12000])
frame6_g= np.mean(norm_array_g[12001:14000])
frame7_g= np.mean(norm_array_g[14001:16000])
frame8_g= np.mean(norm_array_g[16001:18000])
frame9_g= np.mean(norm_array_g[18001:20000])
frame10_g= np.mean(norm_array_g[20001:22000])

#red
frame2_r= np.mean(norm_array_r[4001:6000])
frame3_r= np.mean(norm_array_r[6001:8000])
frame4_r=np.mean(norm_array_r[8001:10000])
frame5_r= np.mean(norm_array_r[10001:12000])
frame6_r= np.mean(norm_array_r[12001:14000])
frame7_r= np.mean(norm_array_r[14001:16000])
frame8_r= np.mean(norm_array_r[16001:18000])
frame9_r= np.mean(norm_array_r[18001:20000])
frame10_r= np.mean(norm_array_r[20001:22000])

#loading all frames into an array
b= np.array([frame2_b, frame3_b, frame4_b, frame5_b, frame6_b, frame7_b, frame8_b, frame9_b, frame10_b], dtype='float64')
g= np.array([frame2_g, frame3_g, frame4_g, frame5_g, frame6_g, frame7_g, frame8_g, frame9_g, frame10_g], dtype='float64')
r= np.array([frame2_r, frame3_r, frame4_r, frame5_r, frame6_r, frame7_r, frame8_r, frame9_r, frame10_r], dtype='float64')

#potting all frames to check if they match our expectations
plt.plot(r)
plt.plot(g)
plt.plot(b)

#obtaining the mean for all frames across all colours
frame2_mean= (frame2_r + frame2_g + frame2_b)/3
frame3_mean= (frame3_r + frame3_g + frame3_b)/3
frame4_mean= (frame4_r + frame4_g + frame4_b)/3
frame5_mean= (frame5_r + frame5_g + frame5_b)/3
frame6_mean= (frame6_r + frame6_g + frame6_b)/3
frame7_mean= (frame7_r + frame7_g + frame7_b)/3
frame8_mean= (frame8_r + frame8_g + frame8_b)/3
frame9_mean= (frame9_r + frame9_g + frame9_b)/3
frame10_mean= (frame10_r + frame10_g + frame10_b)/3

#adding all values into a list
RGB_mean= [frame2_mean, frame3_mean, frame4_mean, frame5_mean, frame6_mean, frame7_mean, frame8_mean, frame9_mean, frame10_mean]

#appending a list with the actual values for interpolation
#NOTE: x_points are actually the y values and y_points the x values, written like this here for easier plotting and interpolation
x_points= []
for x in RGB_mean:
    x_points.append(x)

#known y points from Bonsai script
y_points = [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

#plotting inverse to check
# creating graph space for two graphs
graph, (plot1, plot2) = plt.subplots(1, 2)
 
# plot1 graph for normal axes
plot1.scatter(y_points, x_points)
plot1.set_title("Normal Plot")

# plot2 graph for inverted axes
plot2.scatter(x_points, y_points)
plot2.set_title("Inverted Plot")

#interpolation    
from scipy import interpolate



tck = interpolate.splrep(x_points, y_points)

def f(x):
   
    return interpolate.splev(x, tck)
#here can add any value and obtain our desired input value
print(f(1))

