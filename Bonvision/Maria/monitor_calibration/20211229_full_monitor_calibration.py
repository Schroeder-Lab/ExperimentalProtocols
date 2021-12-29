# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 08:50:55 2021

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