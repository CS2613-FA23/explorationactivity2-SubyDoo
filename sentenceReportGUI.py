
#This program is Python PQ1 converted to use GUI instead of a textual interface
#to run just type "python3 sentenceReportGUI.py"
import tkinter as tk
import matplotlib.pyplot as plt

#function for the sentence report button action
def sentence_report():

    alphaCount = 0
    repeatCount = 0
    endStartCount = 0
    
    #gets the string from the entry widget
    inputString = input_Entry.get()

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
exit_button = tk.Button(buttonFrame, text="Clear Text", bg="#69b2bf", command=clear)
exit_button.grid(sticky="w", row=0, column=1)


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