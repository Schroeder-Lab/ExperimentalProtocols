# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 16:07:48 2021

@author: maria
"""

import numpy as np
import matplotlib.pyplot as plt

#loading file
#file_path= "C://Users//maria//Desktop//PhD//Code//Calibration_blue3"
file_path_b= "C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//Maria//monitor_calibration//output_files//beforeC//Calibration_blue1"
file_path_g= "C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//Maria//monitor_calibration//output_files//beforeC//Calibration_green1"

#formatting file into array
array_b= np.fromfile(file_path_b,dtype='float64')
array_g= np.fromfile(file_path_g,dtype='float64')

#normalizing the array
def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

norm_array_b=  NormalizeData(array_b)
norm_array_g=  NormalizeData(array_g)

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


#loading all frames into an array
b= np.array([frame2_b, frame3_b, frame4_b, frame5_b, frame6_b, frame7_b, frame8_b, frame9_b, frame10_b], dtype='float64')
g= np.array([frame2_g, frame3_g, frame4_g, frame5_g, frame6_g, frame7_g, frame8_g, frame9_g, frame10_g], dtype='float64')


#appending a list with the actual values for interpolation
#NOTE: x_points are actually the y values and y_points the x values, written like this here for easier plotting and interpolation
x_pointsb= []
x_pointsg= []
for x in b:
    x_pointsb.append(x)
    
for x in g:    
    x_pointsg.append(x)

#known y points from Bonsai script
y_points = [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

# #plotting inverse to check
# # creating graph space for two graphs
# graph, (plot1, plot2) = plt.subplots(1, 2)
 
# # plot1 graph for normal axes
# plot1.scatter(y_points, x_pointsb)
# plot1.set_title("Normal Plot")

# # plot2 graph for inverted axes
# plot2.scatter(x_pointsb, y_points)
# plot2.set_title("Inverted Plot")

#interpolation    
from scipy import interpolate



tckb = interpolate.splrep(x_pointsb, y_points)
tckg = interpolate.splrep(x_pointsg, y_points)
def f(x):
   
    return interpolate.splev(x, tckb)
#here can add any value and obtain our desired input value
range_of_xvaluesb= []
range_of_xvaluesg=[]
for x in np.arange(0,1,0.01):
    range_of_xvaluesb.append(f(x))
    
for x in np.arange(0,1,0.01):
    range_of_xvaluesg.append(f(x))
    
range_of_yvalues=[]
for y in np.arange(0,1,0.01):
    range_of_yvalues.append(y)

    
xy= np.stack((range_of_xvaluesb, range_of_xvaluesg))

plt.matshow(xy)

plt.show()
