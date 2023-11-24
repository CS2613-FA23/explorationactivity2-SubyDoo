

 <br />

## 1. What package/library was selected?
The package selected is Matplotlib. <br />

<img src="https://github.com/CS2613-FA23/explorationactivity2-SubyDoo/assets/93729876/5652b188-b19d-4bc7-a823-2475561d8640" width=80% height=80%>

 <br />
 



## 2. What is the package/library and functionality?

- What purpose does it serve

Matplotlib is a widely used open-source data visualization and plotting library for python [1]. It is a python alternative to MATLAB and provides static, animated, and interactive visualizations including scatter plots, bar charts, histograms, error charts, pie charts, box plots, line graphs, etc. [2][3]. It provides the foundation to many popular data analysis/visualization libraries such as Pandas and Seaborn [3].
 <br />


 <br />
References: <br />
[1] https://www.testgorilla.com/blog/matplotlib-in-python/  <br />
[2] https://matplotlib.org/  <br />
[3] https://www.scaler.com/topics/matplotlib/matplotlib-in-python/ <br />
[image] https://matplotlib.org/3.1.1/api/pyplot_summary.html <br />

 <br /><br />

- How do you use it

Get a data set, choose a graph to best represent the data and plot it.
 <br /> 
 <br />

<img src="https://github.com/CS2613-FA23/explorationactivity2-SubyDoo/assets/93729876/876ae825-ab69-42a9-bccb-2219d99f20a5" width=90% height=90%> <br />
Description: image of the graph referenced. For full see code [sentenceReportGUI.py](https://github.com/CS2613-FA23/explorationactivity2-SubyDoo/blob/main/sentenceReportGUI.py)


In order to use Matplotlib you need to import it.
```
import matplotlib.pyplot as plt
```
 <br />

We need to get data that we want to plot. In this case we are plotting the history of string statistics and so we need to know how many reports were done and the stats for each report.
```
totalSentenceCount = 0
alphaCountHistory = []
repeatCountHistory = []
endStartCountHistory = []
```
 <br />

After each report data will be added to the lists
```
totalSentenceCount = totalSentenceCount + 1

... CODE TO GET STATS FOR STRING

alphaCountHistory.append(alphaCount)
repeatCountHistory.append(repeatCount)
endStartCountHistory.append(endStartCount)
```
<br />

Here we are using NumPy to create an array from 1 to the # of reports generated to represent the horiszontal values in the graph
```
xValue = np.arange(1, totalSentenceCount+1)
```
<br />

We will set the size of the graph to 1500 x 1000 pixels
```
plt.figure(figsize=(15, 10))
```
<br />

**For any of the text based methods you can also send parameters to change the appearance of such as font size and position in any of the functions.*\*

Here we set the title of the graph.
```
plt.title("History of Sentence Statistics")
```
<br />

We set the x axis label. 
```
plt.xlabel("Sentence report #")
```
<br />

We will create a plot of x vs y with multiple lines, we add the optional marker parameter so that points are marked in the style specified <br />
(o = circle, x = x, D = diamond, there are many more styles) <br /><br />
An optional label is also specified to describe each of the lines. Different colors are given to each of the lines by default
```
plt.plot(xValue, alphaCountHistory, marker='o', label = "Total number of alphabetic characters")
plt.plot(xValue, repeatCountHistory, marker='x', label = "Total number of words with repeated alphabetic characters")
plt.plot(xValue, endStartCountHistory, marker='D', label = "Total number of end-start letter matches")
```
<br />

Here we will display the legend to display the line titles. By default it will go the best position to avoid lines but you can also specifiy its placement by coordinates or position.
```
plt.legend()
```
<br />

This 
```
new_list = range(math.floor(min(xValue)), math.ceil(max(xValue))+1)
plt.xticks(new_list)
```
<br />

Here we will save the graph as image, we had to do this instead of displaying it directly in GUI becuase of some library import issues on the lab machine
```
plt.savefig("SentenceReportStatisticsHistory.png")
```
<br />


 
 <br />






 
## 3. When was it created?
Matplotlib was created by John D. Hunter in 2002 during his post-doctoral study in neurobiology [1]. 

References: <br />
[1] https://www.scaler.com/topics/matplotlib/matplotlib-in-python/ <br />
 
 <br />








 
## 4. Why did you select this package/library
I selected this library because I have seen a few videos on the data science field that seemed interesting and Matplotlib is an important part of the data science tech stack. Learning this library can be useful in my programming with data creation and representation which I can translate to use in other classes/projects. 

 <br />







## 5. How did learning the package/library influence your learning of the language?
Learning this package and incorporating it into my exploratory 1 program helped me learn how to integrate other visualization libraries into a python GUI (even though it was not demonstrated due to lab machine issues). I also learned an extremely basic form of data logging/accounting and visualization in python. 

 <br />






 
## 6. How was your overall experience with the package/library?
- **When would you recommend this package/library to someone?**  <br />
I would recommend this library to someone who has some interest in the data science field as matplotlib is a popular library for this field. I would also recommend this to anyone in any field that requires data representation such as biology, chemistry, physics, and accounting who also wants an application associated with it due to how easy python is to learn. I would possibly recommend another library called Seaborn which is built on top of Matplotlib as it is simpler to use. If an interactive graph editor is sought where less coding skills are needed such as in excel, the Pylustrator library can be used with Matplotlib. <br /><br />
Demo of Pylustrator: https://www.youtube.com/watch?v=xXPI4LLrNuM  

- **Would you continue using this package/library? Why or why not?**  <br />
I would continue to use this library with the Pandas library for data analysis, machine learning and as a replacement for excel. It will take some time to get used to editing and creating graphs through code rather than an interactive interface but the greater functionality for advanced data analysis with Pandas and representation with Matplotlib would be interesting to further explore.


 <br />

 
