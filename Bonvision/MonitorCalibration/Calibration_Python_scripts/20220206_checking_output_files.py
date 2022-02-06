# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 12:24:06 2022

@author: maria
"""
import numpy as np
import matplotlib.pyplot as plt

file_path_b= "C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//MonitorCalibration//output_files//different_brightness//Calibration_blue1"
file_path_g= "C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//MonitorCalibration//output_files//different_brightness//Calibration_green1"
file_path_r= "C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//MonitorCalibration//output_files//different_brightness//Calibration_red1"

array_b= np.fromfile(file_path_b,dtype='float64')
array_g= np.fromfile(file_path_g,dtype='float64')
array_r= np.fromfile(file_path_r,dtype='float64')

plt.plot(array_b, color="blue") 
plt.plot(array_g, color="green") 
plt.plot(array_r, color="red")