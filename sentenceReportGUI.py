
#This program is Python PQ1 converted to use GUI instead of a textual interface, Now has a plotting feature
#to run just type "python3 sentenceReportGUI.py"

import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import math

import matplotlib.ticker as ticker

# Need to import this to use plt.plot because of UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
# but there issue importing this on lab machine so cannot display graph directly in GUI
# Gettubg this error ImportError: cannot import name 'ImageTk' from 'PIL'
# import matplotlib
# matplotlib.use("TkAgg")
# from matplotlib.figure import Figure 
# from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
  

totalSentenceCount = 0
sentenceLengthHistory = []
alphaCountHistory = []
repeatCountHistory = []
endStartCountHistory = []


#function for the sentence report button action
def sentence_report():

    global totalSentenceCount
    global sentenceLengthHistory
    global alphaCountHistory
    global repeatCountHistory
    global endStartCountHistory

    totalSentenceCount = totalSentenceCount + 1

    alphaCount = 0
    repeatCount = 0
    endStartCount = 0
    
    #gets the string from the entry widget
    inputString = input_Entry.get()
    sentenceLengthHistory.append(len(inputString))

    #splits string into a list of words
    splitString = inputString.split()
    cleanStringList = []

    #add clean string to a new list
    for index, string in enumerate(splitString):
        cString = clean_token(string)
        cleanStringList.append(cString)

    listLength = len(cleanStringList)

    for index, string in enumerate(cleanStringList):
        #if cleaned string is not empty check for repeated characters and end start
        if string != "":
            alphaCount = alphaCount + len(string)

            isRepeated = repeat_letter(string)
            if isRepeated == True:
                repeatCount += 1

            #if not the last string in the list check the next string's starting character
            if index != listLength-1:
                if cleanStringList[index + 1] != "":
                    isEndStart = end_start(string, cleanStringList[index + 1])
                    if isEndStart == True:
                        endStartCount += 1

    
    alphaCountHistory.append(alphaCount)
    repeatCountHistory.append(repeatCount)
    endStartCountHistory.append(endStartCount)

    #updates the label widgets with the new statistics
    character_Number_Label.config(text="Total number of alphabetic characters: " + str(alphaCount))
    word_letter_Repeat_Label.config(text="Total number of words with repeated alphabetic characters: " + str(repeatCount))
    end_Start_Label.config(text="Total number of end-start letter matches: " + str(endStartCount))


#function that takes a string and returns the string with all non alphabet characters removed and in lower case
def clean_token(s):
    str1 = ""
    for char in s:
        if char.isalpha() == True:
            str1 = str1 + char.lower()

    return str1

#returns true if the string has a repeated character
def repeat_letter(s):
    for char in s:
        if s.count(char) > 1:
            return True
    
    return False

#returns true if the last character of the first string is the same as the first character of the second string
def end_start(s1, s2):
    lastChar = s1[-1]
    firstChar = s2[0]

    if lastChar == firstChar:
        return True
    return False

#function for the exit button action
def exit():
    root.destroy()

#function for the clear button action
def clear():
    input_Entry.delete(0, "end")

def generate_graph():

    global totalSentenceCount
    global sentenceLengthHistory
    global alphaCountHistory
    global repeatCountHistory
    global endStartCountHistory

    #xValue = range(1, totalSentenceCount)
    xValue = np.arange(1, totalSentenceCount+1)

    print(str(totalSentenceCount))
    print(xValue)
    print(str(alphaCountHistory))



    # fig, ax = plt.subplots()
    # for axis in [ax.xaxis, ax.yaxis]:
    #     axis.set_major_locator(ticker.MaxNLocator(integer=True))



    # 1500 x 1000 pixels in size
    plt.figure(figsize=(15, 10))

    plt.title("History of Sentence Statistics")
    plt.xlabel("Sentence report #")
    plt.plot(xValue, alphaCountHistory, marker='o', label = "Total number of alphabetic characters")
    plt.plot(xValue, repeatCountHistory, marker='x', label = "Total number of words with repeated alphabetic characters")
    plt.plot(xValue, endStartCountHistory, marker='D', label = "Total number of end-start letter matches")
    
    # default will go the best position to avoid lines, can also specifiy by cords or position
    plt.legend()

    # sets the x labels of the plot as integers
    new_list = range(math.floor(min(xValue)), math.ceil(max(xValue))+1)
    plt.xticks(new_list)

    #plt.ylim(ymin=0.0)
    #plt.locator_params(axis='y', nbins=10) 
    

    #plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(2))
    #plt.locator_params(axis='y', nbins=10)


    #this works by saving as image
    plt.savefig("SentenceReportStatisticsHistory.png")


root = tk.Tk()

#sets the title for the window
root.title("Sentence Report")

#creating a frame for the first row so that the label and entry and next to each other
inputFrame = tk.Frame(root)

#anchor is the direction of the text alignment
label1 = tk.Label(inputFrame, text="Input a sentence for statistics:", justify="left", anchor="w")
#adding a padding of 10px so that the widget is not at the very edge of the window
label1.grid(sticky="w", row=0, column=0, padx=10)

#entry to get text to procees for statistics
input_Entry = tk.Entry(inputFrame, width=50)
input_Entry.grid(sticky="w", row=0, column=1, padx=10)

#adding frame to the root grid
inputFrame.grid(row=0, column=0)

#labels for the statistics
character_Number_Label = tk.Label(root, text="Total number of alphabetic characters: ")
character_Number_Label.grid(sticky="w", row=1, column=0, padx=10)

word_letter_Repeat_Label = tk.Label(root, text="Total number of words with repeated alphabetic characters: ")
word_letter_Repeat_Label.grid(sticky="w", row=2, column=0, padx=10)

end_Start_Label = tk.Label(root, text="Total number of end-start letter matches: ")
end_Start_Label.grid(sticky="w", row=3, column=0, padx=10)

#creating a frame so that the sentece report and clear buttons are next to each other 
buttonFrame = tk.Frame(root)

#creating the button for getting the sentence report
sentence_report_button = tk.Button(buttonFrame, text="Get the sentence report", bg="#bdeb9b", command=sentence_report)
sentence_report_button.grid(sticky="w", row=0, column=0, padx=10)

#creating the button to clear the text in the entry widget
clear_button = tk.Button(buttonFrame, text="Clear Text", bg="#69b2bf", command=clear)
clear_button.grid(sticky="w", row=0, column=1)

#creating the button to clear the text in the entry widget
graph_button = tk.Button(buttonFrame, text="Generate Graph", bg="#f542ec", command=generate_graph)
graph_button.grid(sticky="w", row=0, column=2, padx=10)


#adding button frame to root grid
buttonFrame.grid(sticky="w", row=4, column=0)

#adding the exit button to the root grid
exit_button = tk.Button(root, text="exit", bg="#cc6e6c", command=exit)
exit_button.grid(sticky="e", row=4, column=1)

#tkinter is always looping to check changing values such as mouse positon
root.mainloop()

####Test Cases####
#This is a sentence. (15, 1, 0)
#I order a Total of 21 Fiddleheads. :)) I thought they were exquisite. (50, 6. 2)
#So cool like so cool like very ye cool like (34, 3, 4)
#LoooL Like Everything good dog (26, 3, 4)
#LoO (3, 1, 0)
#Lo!O (3, 1, 0)
#!!!! Hi !!!! !!!! I !!!!! See (6, 1, 0)
#!!!! Hi!!!!!!!! I !!!!! See (6, 1, 1)