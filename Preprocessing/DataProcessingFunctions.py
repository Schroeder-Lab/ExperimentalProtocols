# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 09:26:53 2022

@author: Liad J. Baruchin
"""

def GetMetadataChannels(niDaqFilePath, numChannels = 7):
    """
    

    Parameters
    ----------
    niDaqFilePath : string
        the path of the nidaq file.
    numChannels : int, optional
        Number of channels in the file. The default is 7.

    Returns
    -------
    niDaq : matrix
        the matrix of the niDaq signals [time X channels]

    """
    niDaq = np.fromfile(niDaqFile, dtype= np.float64)
    niDaq = np.reshape(niDaq,(int(len(niDaq)/7),7))
    return niDaq

def AssignFrameTime(frameClock,th = 0.5,plot=False):
    """
    The function assigns a time in ms to a frame time.
    
    Parameters:
    frameClock: the signal from the nidaq of the frame clock
    th : the threshold for the tick peaks, default : 3, which seems to work 
    plot: plot to inspect, default = False
    
    returns frameTimes (ms)
    """
    #Frame times
    # pkTimes,_ = sp.signal.find_peaks(-frameClock,threshold=th)
    # pkTimes = np.where(frameClock<th)[0]
    # fdif = np.diff(pkTimes)
    # longFrame = np.where(fdif==1)[0]
    # pkTimes = np.delete(pkTimes,longFrame)
    # recordingTimes = np.arange(0,len(frameClock),0.001)
    # frameTimes = recordingTimes[pkTimes]
    
    # threshold = 0.5
    pkTimes = np.where(np.diff(frameClock > th, prepend=False))[0]    
    # pkTimes = np.where(np.diff(np.array(frameClock > 0).astype(int),prepend=False)>0)[0]
       
    
    if (plot):
        f,ax = plt.subplots(1)
        ax.plot(frameClock)
        ax.plot(pkTimes,np.ones(len(pkTimes))*np.min(frameClock),'r*')
        ax.set_xlabel('time (ms)')
        ax.set_ylabel('Amplitude (V)')
        
        
    return pkTimes

def DetectPhotodiodeChangesComplicated(photodiode,plot=False,lowPass=30,kernel = 101,fs=1000, waitTime=5000):
    """
    The function detects photodiode changes, even with a noisy
    photodiode signal. It uses a hidden markov chain model for that.
    Might be a slight overkill, but worth it for accuracy. 
    requrires the hmmlearn package.
    
    Parameters: 
    photodiode: the signal from the nidaq of the photodiode    
    lowPass: the low pass signal for the photodiode signal, default: 30,
    kernel: the kernel for median filtering, default = 101.
    fs: the frequency of acquisiton, default = 1000
    plot: plot to inspect, default = False   
    waitTime: the delay time until protocol start, default = 5000
    
    returns: st,et (ms) (if acq is 1000 Hz)
    """    
    
    b,a = sp.signal.butter(1, lowPass, btype='low', fs=fs)
    sigFilt = sp.signal.filtfilt(b,a,photodiode)
    sigFilt = sp.signal.medfilt(sigFilt,kernel)
    # sigFilt[:waitTime] = 0
    # remodel = hmm.GaussianHMM(n_components=2, covariance_type="full", n_iter=1000)
    remodel = hmm.GaussianHMM(n_components=2,n_iter=1000)
    remodel.fit(sigFilt.reshape(-1,1))
    filt = remodel.predict(sigFilt.reshape(-1,1))
    medOne = np.median(photodiode[filt==1])
    medZero = np.median(photodiode[filt==0])
    if (medZero>medOne):
        filt = np.abs(filt-1)

    threshold = 0.5
    crossings = np.where(np.diff(filt > threshold, prepend=False))[0]    
    crossings = np.delete(crossings,np.where(crossings<waitTime)[0])     
    
    
    # stateDiff = np.diff(filt)
    # st = np.where(stateDiff == 1)[0]
    # et = np.where(stateDiff == -1)[0]-1
    
    # #Correct possible problems for end of recording
    # if (len(st)>len(et)):
    #     et = np.hstack((et,[len(sigFilt)]))
    # elif (len(st)<len(et)):
    #     st = np.hstack(([waitTime],st))
    # if (et[0]<st[0]):
    #     st = np.hstack(([waitTime],st))
    # if ((st[-1]-et[-1])>0):
    #     et = np.hstack((et,[len(sigFilt)]))
    
    
    
    if (plot):
        f,ax = plt.subplots(1,1,sharex=True)
        ax.plot(photodiode,label='photodiode raw')
        ax.plot(sigFilt,label = 'photodiode filtered')
        ax.plot(filt*np.max(photodiode),label='state')
        ax.plot(crossings,np.ones(len(crossings))*np.mean(sigFilt),'k*')         
        ax.legend(loc = 'upper right')
        ax.set_xlabel('time (ms)')
        ax.set_ylabel('Amplitude (V)')
    
    
    
    
    
    
    return crossings

def DetectPhotodiodeChanges(photodiode,plot=False,lowPass=30,kernel = 101,fs=1000, waitTime=5000):
    """
    The function detects photodiode changes using a 'Schmitt Trigger', that is, by
    detecting the signal going up at an earlier point than the signal going down,
    the signal is filtered and smootehd to prevent nosiy bursts distorting the detection.W
    
    Parameters: 
    photodiode: the signal from the nidaq of the photodiode    
    lowPass: the low pass signal for the photodiode signal, default: 30,
    kernel: the kernel for median filtering, default = 101.
    fs: the frequency of acquisiton, default = 1000
    plot: plot to inspect, default = False   
    waitTime: the delay time until protocol start, default = 5000
    
    returns: st,et (ms) (if acq is 1000 Hz)
    """    
    
    b,a = sp.signal.butter(1, lowPass, btype='low', fs=fs)
    # sigFilt = photodiode
    sigFilt = sp.signal.filtfilt(b,a,photodiode)
    sigFilt = sp.signal.medfilt(sigFilt,kernel)
   
  
    maxSig = np.max(sigFilt)
    minSig = np.min(sigFilt)
    thresholdU = (maxSig-minSig)*0.2
    thresholdD = (maxSig-minSig)*0.8
    threshold =  (maxSig-minSig)*0.5
    
    # find thesehold crossings
    crossingsU = np.where(np.diff(np.array(sigFilt > thresholdU).astype(int),prepend=False)>0)[0]
    crossingsD = np.where(np.diff(np.array(sigFilt > thresholdD).astype(int),prepend=False)<0)[0]
    # crossingsU = np.delete(crossingsU,np.where(crossingsU<waitTime)[0])     
    # crossingsD = np.delete(crossingsD,np.where(crossingsD<waitTime)[0])   
    crossings = np.sort(np.unique(np.hstack((crossingsU,crossingsD))))
  
    
    if (plot):
        f,ax = plt.subplots(1,1,sharex=True)
        ax.plot(photodiode,label='photodiode raw')
        ax.plot(sigFilt,label = 'photodiode filtered')        
        ax.plot(crossings,np.ones(len(crossings))*threshold,'g*')  
        ax.hlines([thresholdU],0,len(photodiode),'k')
        ax.hlines([thresholdD],0,len(photodiode),'k')
        # ax.plot(st,np.ones(len(crossingsD))*threshold,'r*')  
        ax.legend()
        ax.set_xlabel('time (ms)')
        ax.set_ylabel('Amplitude (V)')
    
    
    
    
    
    return crossings

def DetectWheelMove(moveA,moveB,rev_res = 1024, total_track = 598.47,plot=False):
    """
    The function detects the wheel movement. 
    At the moment uses only moveA.    
    
    Parameters: 
    moveA,moveB: the first and second channel of the rotary encoder
    rev_res: the rotary encoder resoution, default =1024
    total_track: the total length of the track, default = 598.47 (mm)
    kernel: the kernel for median filtering, default = 101.
    
    plot: plot to inspect, default = False   
    
    returns: distance
    """
    
    
    # make sure all is between 1 and 0
    moveA /= np.max(moveA)
    moveA -= np.min(moveA)
    moveB /= np.max(moveB)
    moveB -= np.min(moveB)
    
    # detect A move
    ADiff = np.diff(moveA)
    Ast = np.where(ADiff >0.5)[0]
    Aet = np.where(ADiff <-0.5)[0]
    
    # detect B move
    BDiff = np.diff(moveB)
    Bst = np.where(BDiff >0.5)[0]
    Bet = np.where(BDiff <-0.5)[0]
    
    #Correct possible problems for end of recording
    if (len(Ast)>len(Aet)):
        Aet = np.hstack((Aet,[len(moveA)]))
    elif (len(Ast)<len(Aet)):
        Ast = np.hstack(([0],Ast))   
    
    
    dist_per_move = total_track/rev_res
    
    # Make into distance
    track = np.zeros(len(moveA))
    track[Ast] = dist_per_move
    
    distance = np.cumsum(track)
        
    if (plot):
        f,ax = plt.subplots(3,1,sharex=True)
        ax[0].plot(moveA)
        # ax.plot(np.abs(ADiff))
        ax[0].plot(Ast,np.ones(len(Ast)),'k*')
        ax[0].plot(Aet,np.ones(len(Aet)),'r*')
        ax[0].set_xlabel('time (ms)')
        ax[0].set_ylabel('Amplitude (V)')
        
        ax[1].plot(distance)
        ax[1].set_xlabel('time (ms)')
        ax[1].set_ylabel('distance (mm)')
        
        ax[2].plot(track)
        ax[2].set_xlabel('time (ms)')
        ax[2].set_ylabel('Move')
    
    # movFirst = Amoves>Bmoves
    
    return distance
  
def GetSparseNoise(filePath, size=(20,25)):
    """
    Pulls the sparse noise from the directory
    
    Parameters: 
    filePath: The full file path for the sparse noise file
    size: a tuple for the size of the screen. default = (20,25)         
    
    returns: an array of size [frames X size[0] X size[1]]
    """
    sparse = np.fromfile(filePath, dtype= np.dtype('b'))
    sparse = np.reshape(sparse,(int(len(sparse)/(size[0]*size[1])),size[0],size[1]))
    # sparse = np.reshape(sparse,(size[0],size[1],int(len(sparse)/(size[0]*size[1]))))
    return sparse

def GetLogEntry(filePath,entryString):
    """
    

    Parameters
    ----------
    filePath : str
        the path of the log file.
    entryString : the string of the entry to look for

    Returns
    -------
    StimProperties : list of dictionaries
        the list has all the extracted stimuli, each a dictionary with the props and their values.

    """
    
    

    StimProperties  = []
    
    with open(filePath, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            a = []
            for p in range(len(props)):
                # m = re.findall(props[p]+'=(\d*)', row[np.min([len(row)-1,p])])
                m = re.findall(entryString, row[np.min([len(row)-1,p])])
                if (len(m)>0):
                    a.append(m[0])            
            if (len(a)>0):
                stimProps = {}
                for p in range(len(props)):
                    stimProps[props[p]] = a[p]
                StimProperties.append(stimProps)
    return StimProperties

def GetStimulusInfo(filePath,props):
    """
    

    Parameters
    ----------
    filePath : str
        the path of the log file.
    props : array-like
        the names of the properties to extract.

    Returns
    -------
    StimProperties : list of dictionaries
        the list has all the extracted stimuli, each a dictionary with the props and their values.

    """
    
    

    StimProperties  = []
    
    with open(filePath, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            a = []
            for p in range(len(props)):
                # m = re.findall(props[p]+'=(\d*)', row[np.min([len(row)-1,p])])
                m = re.findall(props[p]+'=([a-zA-Z0-9_.-]*)', row[np.min([len(row)-1,p])])
                if (len(m)>0):
                    a.append(m[0])            
            if (len(a)>0):
                stimProps = {}
                for p in range(len(props)):
                    stimProps[props[p]] = a[p]
                StimProperties.append(stimProps)
    return StimProperties

def DeriveDfSignal(F,N,fr,ws = 180):
    None
    F0 = sp.scipy.ndimage.percentile_filter(F,8,size=(1,180*fr))
    N0 = sp.scipy.ndimage.percentile_filter(N,8,size=(1,180*fr))   
    Ff = F-F0
    Nf = N-N0
    #### Implement alpha factor finding Fc = F-alpha*N with what was found above
    None