# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 15:34:01 2022

@author: maria
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

#loading file
#file_path= "C://Users//maria//Desktop//PhD//Code//Calibration_blue3"
file_path_b= "C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//Maria//monitor_calibration//output_files//beforeC//Calibration_blue1"
file_path_g= "C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//Maria//monitor_calibration//output_files//beforeC//Calibration_green1"
#file_path_r= "C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//Maria//monitor_calibration//output_files//beforeC//Calibration_red1"


#formatting file into array
array_b= np.fromfile(file_path_b,dtype='float64')
array_g= np.fromfile(file_path_g,dtype='float64')
#array_r= np.fromfile(file_path_r,dtype='float64')

#normalizing the array
def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

def f(x):
    return interpolate.splev(x, tck)

def f2(x):
    return interpolate.splev(x, tck2)

# def f3(x):
#     return interpolate.splev(x, tck3)

norm_array_b=  NormalizeData(array_b)
norm_array_g=  NormalizeData(array_g)
#norm_array_r=  NormalizeData(array_r)

#getting the values per frame which contained different shadings of the respective colours
#there are steps of 2000 because the sample rate was 1000 and each frame was shown for 2s
#first 4000 steps removed due to a max saturation frame which would appear at the start for some unexplainable reason (tried to remove it in Bonsai script but didn't work)


# #red
# frame2_r= np.mean(norm_array_r[4000:5999])
# frame3_r= np.mean(norm_array_r[6000:7999])
# frame4_r=np.mean(norm_array_r[8000:9999])
# frame5_r= np.mean(norm_array_r[10000:11999])
# frame6_r= np.mean(norm_array_r[12000:13999])
# frame7_r= np.mean(norm_array_r[14000:16999])
# frame8_r= np.mean(norm_array_r[16000:17999])
# frame9_r= np.mean(norm_array_r[18000:19999])
# frame10_r= np.mean(norm_array_r[20000:21999])


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


#loading all frames into an array
b= np.array([frame2_b, frame3_b, frame4_b, frame5_b, frame6_b, frame7_b, frame8_b, frame9_b, frame10_b], dtype='float64')
g= np.array([frame2_g, frame3_g, frame4_g, frame5_g, frame6_g, frame7_g, frame8_g, frame9_g, frame10_g], dtype='float64')
#r= np.array([frame2_r, frame3_r, frame4_r, frame5_r, frame6_r, frame7_r, frame8_r, frame9_r, frame10_r], dtype='float64')

y_points= [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

tck = interpolate.splrep(g, y_points)
tck2= interpolate.splrep(b, y_points)
#tck3= interpolate.splrep(r, y_points)



range_of_xvaluesg=[]
range_of_xvaluesb= []
range_of_xvaluesr=[]
for x in np.arange(0,0.9,0.003515625):
    range_of_xvaluesg.append(f(x))
    
for x in np.arange(0,0.9,0.003515625):
    range_of_xvaluesb.append(f2(x))

# for x in np.arange(0,0.9,0.003515625):
#     range_of_xvaluesr.append(f3(x))

    
range_of_yvalues=[]
for y in np.arange(0,0.9,0.003515625):
    range_of_yvalues.append(y)
    

    
arrayg= np.array(range_of_xvaluesg)
arrayb= np.array(range_of_xvaluesb)
#arrayr= np.array(range_of_xvaluesr)

zeros=np.zeros((1,256,1))


arrayrgb= np.dstack((zeros, arrayg, arrayb))




plt.imshow(arrayrgb)
plt.axis('off')
plt.imsave('C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//Maria//monitor_calibration//LUTs//ourLUTrgb.jpg', arrayrgb)

#plt.save(fname= 'C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//Maria//monitor_calibration//ourLUTrgb.png')


