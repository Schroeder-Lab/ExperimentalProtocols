# Bonsai and Bonvision- User guide
## About and good to know
### What is Bonvision?
Bonvision is a community package which can be installed in Bonsai and allows creating diverse visual stimuli protocols
**Most important thing to remember: Bosai is asynchronous, unlike Python, Matlab etc**

**Further resources:**

There is a Bonvision [website](https://bonvision.github.io/pages/001_info/) which more or less describes what it does, how it works and the different nodes such as DrawQuad, DrawGratings etc (scroll down on the about page for a useful youtube tutorial video)


## Example workflow

**One important thing to bear in mind about Bonsai is the fact that it is *asynchronous* so the order in which the nodes are placed doesn't matter (*however* they do have to be connected to each other in a way that makes sense)**

![script annotated](https://github.com/Schroeder-Lab/ExperimentalProtocols/blob/main/Bonvision/Maria/Bonvision_guide_figures/script%20annotated%20all.PNG)

The original full script can be opened in GitHub Desktop and downloaded from [here](https://github.com/Schroeder-Lab/ExperimentalProtocols/blob/main/Bonvision/Liad/SingleCircleOverScreenOrtho.bonsai)

Once you have loaded this in Bonsai and pressed run, you will see random circles appearing in various places on a grey background on a pop up window.

Now let's see what the use of the general components of this Bonvision workflow is and after that we will delve into the sub-workflows embedded in this:
1. These are three nodes which are essential every time
	- **Create Window** generates a popup window in which the stimuli will be displayed (there are settings on the right of the GUI which can be adjusted, the most relevant probably being *DisplayDevice* which in the current 2P setup(24.11.2021) would be *Secondary*) (see below)

	![CreateWindow settings](https://github.com/Schroeder-Lab/ExperimentalProtocols/blob/main/Bonvision/Maria/Bonvision_guide_figures/Figure_2.png)

	- **Bonvision Resources** and **Load Resources** simply specifies that we will be using the package Bonvision and loads these resources 

2. This section is also needed in all types of workflows, however, it can be changed or simplefied
	- **RenderFrame** will always be needed. It creates a frame on top of which the stimulus types are shown
	- In this example, two types of stimuli are shown on the same frame and controlled through different parameters:
		-  **Orthographic View** shows stimuli in terms of the angles specified. This will be important for us because the mouse will be positioned at a specific angle relative to the monitor
		- **NormalizedView** normalizes the location of the stimuli between 0 and 1 to make it easier to specify the location regardless of the size of the window
		- there are two nodes connected to the two View nodes which are marked with an X, (**drawStim** and **Quad**). These are both **BehaviourSubject** nodes and their names were changed to something more specific and meaningful. The official definition of **BehaviourSubject**  is "Broadcasts the latest value of an observable sequence to all subscribed and future observers using a shared suject". This works together with **SubscribeSubject** (usually has an X and a star displayed in the node, official definition: "Generates a sequence of values by subscribing to a shared subject"). This is how multiple stimuli can be generated when paired with **SubscribeSubject** of the same name. An example of this is **Quad** in this section and the other **Quad** in section **4**. Note the different colours and the extra star displayed with the X for the later.
		- the **FrameEventLogger** node records every time the two stimuli have been displayed in this case (creates a CSV file and adds this data in it)
3. This part (**CreateRandom**) creates random numbers  which is important later on for randomising the sequence and location of the stimuli.
4. This section records an **AnalogInput** (from a photodiode in this case), then records when the input was added (**LogEvent**) to a binary file in this case (**MatrixWriter**), then records again when that file was written (the second **LogEvent**)
5. This draws a square in the specified location and colour and because it is connected to a **Subscribe Subject** called **Quad** which in turn is connected to the **BehaviourSubject** (**Quad**) it will display this on the window through its connection to **RenderFrame** from section **2**. The real purpose of this is to make sure the timing of the stimuli actually displayed on the monitor coresponds to the timing specified in the settings. This is because it will be important to match the stimuli to the 2P recording and since there could be a delay in the display of the stimuli for whatever reason (slow rendering by the computer etc), we have to know if there is a delay. Therefore, a small rectangle is shown in the right corner of the screen simultaneously with the other stimuli shown (hence the node format in section **2**.) and the photodiode is placed right on top of it to record the actual output. 
6. This is the collection of nodes which actually specifies the exact stimuli (in this case both rectangles and circles) and the timing of these stimuli. Let's see the purpose of each node:
	- the most important node here is probably **Concat**. This essentially takes the first command (to show the rectangle) and only displays the second command (to show the circles) once the first command has been executed
	- **Quad** is the **SubscribeSubject** which links to the **BehaviourSubject** we saw in section **2**.
	- the **TakeUntil** and the other node that connects to it, **Timer**, essentially control how long the stimulus will be shown. **TakeUntil** could also be controlled by something else such as pressing a key on a keyboard, a light flash or sound, it doesn't have to be time
	- finally when the squares are displayed, the program goes to the other sub-workflow (**Present Stimuli**) (see below)

	![present stimuli workflow](https://github.com/Schroeder-Lab/ExperimentalProtocols/blob/main/Bonvision/Maria/Bonvision_guide_figures/Present%20Stimuli%20Workflow.PNG)
--> this can be accessed bu double clicking on the node


