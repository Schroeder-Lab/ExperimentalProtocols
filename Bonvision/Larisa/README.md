Information for reward experiments

# Bonsai files

1. Reward

Protocol for accommodating mouse to the rig and the sound of the valve

Delay 1: valve opening 
Delay 2: time between openings

![image](https://user-images.githubusercontent.com/82219339/184322305-86901b12-83dc-440f-9508-800b7c3abea8.png)

Saving Directory: where the output is stored

![image](https://user-images.githubusercontent.com/82219339/184322392-53e79e40-2abe-49dd-9f08-33fa6f2bc757.png)

Timer: How long the protocol runs for 

![image](https://user-images.githubusercontent.com/82219339/184322443-f4e308b1-a17d-46e4-90a5-7a168b073fe8.png)

2. OpenValveLong

MUST USE this file to get rid of air bubbles in the tubing and make sure the needle is filled with sucrose before the experiments start

Delay: How long the valve opens for, valve will close automatically at the end 

![image](https://user-images.githubusercontent.com/82219339/184322531-4433e060-3d79-4449-82be-1479399d4c68.png)

3. GratingsOutOfCsvReward

_IN GRATINGS ASYNC GROUP_

![image](https://user-images.githubusercontent.com/82219339/184323975-fc54e65d-bf45-4b0e-b626-c7cd901aa4ea.png)

RepeatCount: iterations of EACH stimulus eg with two stimuli if you input 10 it will total 20

CSV reader: input the correct csv file 

_IN GRATING PRES_

Delay 1: How many s into reward presentation is the reward delivered

Delay 2: How long the valve is open for 

![Picture1](https://user-images.githubusercontent.com/82219339/184323328-f0e48fad-7cfa-4ceb-9bce-f5fe465386aa.png)

In Python Source: can edit the ITIs (max nr of seconds - min nr of seconds) - it will generate a random number between those values 

![Picture3](https://user-images.githubusercontent.com/82219339/184323758-60288fc2-bd05-4090-a7dc-314d1dbe5d31.png)

Timer: How long the stimulus is presented for 

![image](https://user-images.githubusercontent.com/82219339/184323901-0d4512d6-a0ad-4670-80e6-8ecab456f6c6.png)


