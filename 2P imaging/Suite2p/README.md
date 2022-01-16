# Cell detection criteria
In order to ensure a standardised approach to cell detection, these criteria should be adhered to when doing a manual curation of the ROIs detected by suite2p:
- ROIs which have a reasonable shape (and also look similar to the actual recording)
- fast responses
- neuropil traces and raw fluroescence activity should not be similar (as little correlation between traces as possible)
- as few slow responses as possible (beware of traces which only have slow responses, especially if they are present near a blood vessel)
- be especially careful with ROIs detected on/below or near blood vessels (dark areas)
- also look at the traces over time; if they decrease in amplitude a lot over time that is a bad sign!
- avoid noisy traces
- to be safe, it is best to remove the ROIs detected in dark areas 
- remove traces which have a "step-like" appearance to them

To keep in mind: during pre-processing slow responses are filtered out (over 1350 frames)
## Good examples:
![good](https://github.com/Schroeder-Lab/ExperimentalProtocols/blob/main/2P%20imaging/Suite2p/Examples%20of%20traces/good.PNG)
