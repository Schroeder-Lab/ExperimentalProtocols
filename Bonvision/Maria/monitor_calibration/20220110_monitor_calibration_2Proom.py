# # -*- coding: utf-8 -*-
# """
# Created on Wed Dec 29 08:50:55 2021

# @author: maria
# """

# import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#loading file
#file_path= "C://Users//maria//Desktop//PhD//Code//Calibration_blue3"
file_path_b= "C://Maria//output//no_red//Calibration_blue"
file_path_g= "C://Maria//output//no_red//Calibration_green"
file_path_r= "C://Maria//output//no_red//Calibration_red"
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

norm_red=pd.DataFrame(norm_array_r, dtype='float64')
norm_green= pd.DataFrame(norm_array_g, dtype='float64')
norm_blue=pd.DataFrame(norm_array_b, dtype='float64')

plt.plot(norm_red,color="red")
plt.plot(norm_green, color= "green")
plt.plot(norm_blue, color= "blue")

# norm_red.to_csv('C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//Maria//monitor_calibration//normalised_red.csv')
# norm_green.to_csv('C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//Maria//monitor_calibration//normalised_green.csv')
# norm_blue.to_csv('C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//Maria//monitor_calibration//normalised_blue.csv')


    
    


#for i in norm_red:
    