#Program: reader.py
#Authors: Calvin Brown, Chad Gilmer
#Description: Reades a file in and does things on it like ls, stat, and info of the file
import sys
import os
import struct
from Utilities import *


fileName = sys.argv[1]


#Loops until quit
while True:
    userInput = input("/] ")
    if userInput == "quit":
        print("Bye!")
        break
    elif userInput == "info":
        printInfo(fileName)
    elif userInput == "cd":
        print("change directory")
    elif "stat" in userInput:
        #This is the STAT function, This ~semi~ needs the ls function since the ls can get info about the first clustor of data, and then we can get info on that from finding those files in the ls module.
        fileToStat = userInput.split()
        if(len(fileToStat) <= 1):
            print("Please enter stat <filename> to get the statistics of it")
        elif(len(fileToStat) > 1):
            fileToStat = fileToStat[1]
            fileObject = open(fileToStat, "r")
            fileObject.close()
    elif userInput == "ls":
        #As of right now this gets the root cluster, I need it to seek to that piece and then read info yet, I haven't figured out how to do that
        rootClus(fileName)
