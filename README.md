[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/kCrKdl4V)
# ExplorationActivity2


## 1. What package/library does this program demonstrate?
The package used to expand [sentenceReportGUI.py](https://github.com/CS2613-FA23/explorationactivity2-SubyDoo/blob/main/sentenceReportGUI.py) is Matplotlib. <br />

<img src="https://github.com/CS2613-FA23/explorationactivity2-SubyDoo/assets/93729876/5652b188-b19d-4bc7-a823-2475561d8640" width=80% height=80%>

 <br />
References: <br />
[image] https://matplotlib.org/3.1.1/api/pyplot_summary.html <br />
 <br />




## 2. How to run the programs
Make sure python 3 is installed to the machine<br />
Make sure the Matplotlib library is installed <br />
> python -m ensurepip
> python -m pip install --update matplotlib 

If Matplotlib is installed you can simply run
> python3 sentenceReportGUI.py <br />
 <br />




## 3. What purpose dose the programs serve

The sentenceReportGUI program is the Python PQ1 converted to use GUI instead of a textual interface using Tkinter. It shows a different way to interact with a user as opposed to the textual user interface. <br />

The program will take a string as an input thought the GUI and report some statistics such as the total number of alphabetic characters, total number words with repeated alphabetic characters, and total number of end-start letter matches between words. The history of these values will be tracked so they can be plotted (the focus of this demo).

There are a few buttons to interact with but the one of focus for this exploratory activity is the "**Download Sentence Report History Graph**" button which will graph the history of the statistical results into a png image using Matplotlib. 
> [!NOTE]
> Unfortunalty due to some library issues on the lab machines, <br />
> the graph could not be displayed directly in the GUI and so it is saved as an image

<br /> <br />
This program demonstrates: 
- creating multiple lines on a plot
- setting plot size
- setting plot title
- setting axis labels
- different styles for marking points
- ensuring all axis values are labeled
- saving graph as an image
<br />





## 4. Sample input/output

- sentenceReportGUI.py
  - run the program to get this initial state <br /> <img src="https://github.com/CS2613-FA23/explorationactivity2-SubyDoo/assets/93729876/2689cdbf-4f69-46c1-ae28-f2646e5573ef" width=80% height=80%> <br />
  - input some text into the textbox and click the "Get the sentence report" button, the labels will update with the statistics <br /> <img src="https://github.com/CS2613-FA23/explorationactivity2-SubyDoo/assets/93729876/ed57193f-c072-4300-a939-c1a9961b1db2" width=80% height=80%> <br />
  - keep typing new sentances and clicking the "Get the sentence report" button to get a report and add the data to the history
  - Once you want to get the history of the statistics, click the "Download Sentence Report History Graph" button, the graph should be downloaded in the same directory as the program <br />
  
- SentenceReportStatisticsHistory.png
  - Graph showing the report number in the horizontal axis VS the number of alphabetic characters, words with repeated alphabetic characters, end-start letter matches
  <img src="https://github.com/CS2613-FA23/explorationactivity2-SubyDoo/assets/93729876/876ae825-ab69-42a9-bccb-2219d99f20a5" width=100% height=100%> <br />
<br />

> [!NOTE]
> More Inputs/Outputs are in comments at the bottom of the program if you need help
