# Monitor calibration

## This page explains how to perform monitor calibration for the monitors we use to show visual stimuli to the experimental animals.

### Why calibrating the monitor?

### Part 1: Monitor calibration test

- Before we can calibrate the monitor we first need to determine what the current colour correction is
- for this we need to measure what the monitor displays using a photodiode
- this is present in the current setup (December 2021)
- There is a Bonvision script for this available from [here](https://github.com/Schroeder-Lab/ExperimentalProtocols/blob/main/Bonvision/Maria/monitor_calibration/calibration_scripts_bonsai/GammaCalibration_Test.bonsai)
- However, it gives an error when we try to run it which couldn't be solved, therefore [three custom scripts](https://github.com/Schroeder-Lab/ExperimentalProtocols/tree/main/Bonvision/Maria/monitor_calibration/calibration_scripts_bonsai) (one for each colour) were written to obtain the [output](https://github.com/Schroeder-Lab/ExperimentalProtocols/tree/main/Bonvision/Maria/monitor_calibration/output_files) from the photodiode (the photodiode records the voltage).
- These scripts should already be available on the local computer in the 2P room.
- This output (in the form of a binary file) is then fed into a [custom python script](https://github.com/Schroeder-Lab/ExperimentalProtocols/blob/main/Bonvision/Maria/monitor_calibration/Calibration_Python_scripts/20220113_Calibration_Script_optimised.py) which feeds the data into an array and gives a graph with the normalised output from all 3 colours at 9 data points

![Nvidia](https://github.com/Schroeder-Lab/ExperimentalProtocols/blob/main/Bonvision/Maria/monitor_calibration/Figures/Nvidia%20control%20panel%20gamma%20adjustment.PNG)
- go to adjust colour settings--> change gamma (value of 2.6 gives a linear output)
- use the Python script to check how the graph compares to the previous one, before calibration

### Part 2: Monitor calibration: Two options
#### Step 1: Using the Nvidia control panel to adjust settings as good as possible
This is how the plot looks like before and after correction (with changing Nvidia settings only, however) **to note: we removed the red from the monitor because it interferes with the 2P laser, so the red is not relevant anymore**:

![corrected_output](https://github.com/Schroeder-Lab/ExperimentalProtocols/blob/main/Bonvision/Maria/monitor_calibration/Figures/before%20and%20after%20Calibration.PNG)

#### Step 2: Using Bonvision
- the output after Nvidia correction is then fed into the code available here [add finished code] then interpolates this data to obtain a range of values which are used to create a lookup table (LUT) (image format)
- this LUT is fed into the **gamma correction** node in Bonsai. This node should be added to all our scripts to allow for gamma correction


### Calibration test every month
- In order to ensure the values stay the same and we perform the right correction, a calibration test should be run once every month and compared to the previous values in this [script](https://github.com/Schroeder-Lab/ExperimentalProtocols/blob/main/Bonvision/Maria/monitor_calibration/comparing_old_and_new_output_values.py)
