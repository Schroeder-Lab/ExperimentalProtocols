# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 16:25:38 2022

@author: maria
"""

import numpy as np
import matplotlib.pyplot as plt


y= [np.arange(0,1,0.00390625)]
x_points= [np.arange(0,1,0.00390625)]


arraygray= np.dstack((y,y,y))


plt.imshow(arraygray)
plt.axis('off')
plt.savefig(fname= 'C://Users//maria//Documents//GitHub//ExperimentalProtocols//Bonvision//Maria//monitor_calibration//ourLUTgray.png')
