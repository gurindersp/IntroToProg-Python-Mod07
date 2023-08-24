*Gurinder Pabla*  
*Aug. 23, 2023*  
*Assignment 07*  
*Foundations of Programming: Python*
*[https://github.com/gurindersp/IntroToProg-Python-Mod07](https://github.com/gurindersp/IntroToProg-Python-Mod07)*

# Pickling and Structured Error Handling

## Introduction
In this module, we return to working with text files, but with a more efficient method of using functions, as well as learning how to prepare in advance for potential errors that a user can create. A twist that we have added to the text files is having the data saved and loaded be obscure text rather than normal text. This was done via the pickling method. The other topic we covered was getting accustomed to using the Try-Except scenario to try and predict errors that can arise when a user is interacting with our code. This way, we can provide a better description of what is causing the error, leading to a more user-friendly error message being displayed. In the end, our understanding of the material was tested via the task of creating a script that demonstrates how pickling and structured error handling work.

## Pickling and Try-Except Block
There are times when it is more appropriate to have text saved in a binary format rather than the usual plain text format. Python allows you to do so by using the Pickling method. In other words, “The Python pickle module is another way to serialize and deserialize objects in Python…it’s also faster and it works with many more Python types right out of the box, including your custom-defined objects.” ([https://realpython.com/python-pickle-module/](https://realpython.com/python-pickle-module/), 2023) (External Site). It is important to know that although the content is not human-readable, it does not mean that the information is encrypted. In addition, to utilize the functions for pickling, you must first import the pickle code from another code file into your own script. Another topic we touched upon was practicing structured error handling, specifically with the Try-Except method. By doing so, we can predict errors that can occur and proactively create error messages that are easy to understand and allow for simple troubleshooting on the user’s end.

## Module 7 Script Assignment
The task for this week diverged from the recent assignments in that a template script was no longer provided that required to be edited. This was a script from scratch that would need to demonstrate pickling and the try-except method being utilized correctly. I did so by creating two functions that would make use of the pickling operators and those functions would then be called after receiving inputs from a user. The custom functions defined can be seen in Figure 1. A challenging aspect of this script was the fact the pickle.load() only accounted for one row of data. As such a while loop needed to be constructed to capture all rows of data within the file. Within the presentation section where we take in the inputs from the user, I used the try-except method to ensure that the input for the “priority” would only have numbers in it. If it didn’t, a simple error message will be displayed instructing only numbers to be used in that specific input. Figures 2-6 reveal the outputs on PyCharm and Terminal, including the display of the error message.

## Summary
At the end of this module, we have gone through and enforced topics that we have been exposed to before, such as working with text files, and are able to expand on them by using programming experience that we did not have before. As such, we are now capable of saving data into a file with obscure text via Python Pickling. In addition, we learned more about error messages by practicing with the Try-Except method, and that will serve us well in the future for instances where our script will be commonly interacting with users. By learning structured error handling, we are setting foundations for more clean and efficient coding in the future.  

![Figure 1](https://github.com/gurindersp/IntroToProg-Python-Mod07/blob/main/docs/Picture1.png "Figure 1")
#### *Figure 1: Custom Defined Functions*             

![Figure 2](https://github.com/gurindersp/IntroToProg-Python-Mod07/blob/main/docs/Picture2.png "Figure 2")
#### *Figure 2: Script on PyCharm*  

![Figure 3](https://github.com/gurindersp/IntroToProg-Python-Mod07/blob/main/docs/Picture3.png "Figure 3")
#### *Figure 3: Script on PyCharm*  

![Figure 4](https://github.com/gurindersp/IntroToProg-Python-Mod07/blob/main/docs/Picture4.png "Figure 4")
#### *Figure 4: Script on PyCharm*  

![Figure 5](https://github.com/gurindersp/IntroToProg-Python-Mod07/blob/main/docs/Picture5.png "Figure 5")
#### *Figure 5: Text file on PyCharm*  

![Figure 6](https://github.com/gurindersp/IntroToProg-Python-Mod07/blob/main/docs/Picture6.png "Figure 6")
#### *Figure 6: Script on Terminal*  








