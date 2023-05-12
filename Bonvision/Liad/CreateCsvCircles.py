# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 13:31:14 2021
@author: liad0
"""

import csv
import numpy as np

rangeX, rangeY, Dia, White = 0, 0, 0, 0

header = ["X", "Y", "Diameter", "White", "Presentation Time"]

filePath = "D:\Bonsai\VisualProtocols\csvCircleStationary.csv"

data = np.array([0, 0, 0, 0, 0]).T

# Parameters to change
gridSize = 5
xRange = np.arange(
    -150, -110, gridSize
)  # np.arange(-145,-90,5)#np.arange(-145,-45,10)
yRange = np.arange(5, 45, gridSize)  # np.arange(-41,41,5)#np.arange(-41,41,10)
diaRange = [0.5, 1, 2, 4, 8, 16, 32]  # [1,4,16,255]
blackWhiteRange = [0, 1] 
presentationT = 0.10

# Create Data

for d in diaRange:
    df = xRange[1] - xRange[0]
    # xRange_ = np.arange(xRange[0],xRange[-1],max(d,df))
    xRange_ = xRange
    for x in xRange_:
        df = yRange[1] - yRange[0]
        # yRange_ = np.arange(yRange[0],yRange[-1],max(d,df))
        yRange_ = yRange
        for y in yRange_:
            for w in blackWhiteRange:
                data = np.vstack((data, [x, y, d, w, presentationT]))
totalTime = (data.shape[0] * (presentationT)) / 60
print("Total Time is: " + str(totalTime) + " Minutes per Run")

data = data[1:, :]

with open(filePath, "w", encoding="UTF8", newline="") as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)
