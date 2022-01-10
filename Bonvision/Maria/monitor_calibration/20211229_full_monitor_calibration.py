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
file_path_bGC= "C://MyPrograms//Bonvision//output//afterGC//Calibration_blue0"
file_path_gGC= "C://MyPrograms//Bonvision//output//afterGC//Calibration_green0"
file_path_rGC= "C://MyPrograms//Bonvision//output//afterGC//Calibration_red0"

file_path_b= "C://MyPrograms//Bonvision//output//Calibration_blue9"
file_path_g= "C://MyPrograms//Bonvision//output//Calibration_green0"
file_path_r= "C://MyPrograms//Bonvision//output//Calibration_red0"
#formatting file into array
array_b= np.fromfile(file_path_b,dtype='float64')
array_g= np.fromfile(file_path_g,dtype='float64')
array_r= np.fromfile(file_path_r,dtype='float64')

array_bGC= np.fromfile(file_path_bGC,dtype='float64')
array_gGC= np.fromfile(file_path_gGC,dtype='float64')
array_rGC= np.fromfile(file_path_rGC,dtype='float64'

#normalizing the array
def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

norm_array_b=  NormalizeData(array_b)
norm_array_g=  NormalizeData(array_g)
norm_array_r=  NormalizeData(array_r)

# norm_array_bGC=  NormalizeData(array_bGC)
# norm_array_gGC=  NormalizeData(array_gGC)
# norm_array_rGC=  NormalizeData(array_rGC)

norm_red=pd.DataFrame(norm_array_r, dtype='float64')
norm_green= pd.DataFrame(norm_array_g, dtype='float64')
norm_blue=pd.DataFrame(norm_array_b, dtype='float64')

norm_redGC=pd.DataFrame(norm_array_rGC, dtype='float64')
norm_greenGC= pd.DataFrame(norm_array_gGC, dtype='float64')
norm_blueGC=pd.DataFrame(norm_array_bGC, dtype='float64')


plt.plot(norm_red)
plt.plot(norm_green)
plt.plot(norm_blue)

plt.scatter(norm_redGC)
plt.scatter(norm_greenGC)
plt.scatter(norm_blueGC)

norm_red.to_csv('C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//Maria//monitor_calibration//normalised_red.csv')
norm_green.to_csv('C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//Maria//monitor_calibration//normalised_green.csv')
norm_blue.to_csv('C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//Maria//monitor_calibration//normalised_blue.csv')

# average_red=[]

# for i in norm_red:
#     average_red.append
    
    


#for i in norm_red:
    