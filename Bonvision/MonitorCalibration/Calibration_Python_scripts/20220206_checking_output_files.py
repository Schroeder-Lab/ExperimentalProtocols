# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 12:24:06 2022

@author: maria
"""
import numpy as np
import matplotlib.pyplot as plt

file_path_b= "C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//MonitorCalibration//output_files//20220428//Calibration_blue1"
file_path_g= "C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//MonitorCalibration//output_files//20220428//Calibration_green1"
# file_path_r= "C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//MonitorCalibration//output_files//20220428//Calibration_red1"

array_b= np.fromfile(file_path_b,dtype='float64')
array_g= np.fromfile(file_path_g,dtype='float64')
# array_r= np.fromfile(file_path_r,dtype='float64')

fig, axs= plt.subplots(2,sharex=True, sharey=True)
axs.plot(array_b, color="blue") 
axs.plot(array_g, color="green") 
# plt.plot(array_r, color="red")
# plt.imsave(fname= "C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//MonitorCalibration//Figures//20220428.png")