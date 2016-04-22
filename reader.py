#Program: reader.py
#Authors: Calvin Brown, Chad Gilmer
#Description: Reades a file in and does things on it like ls, stat, and info of the file
import sys
import os
import struct
from Utilities import *
from lsInfo import *
from statInfo import *
from info import *
from read import *
from changeDirectory import *

fileName = sys.argv[1]


#Loops until quit
directory = ""
newTup = ("",0)
while True:


    userInput = input("/"+directory+"] ")

    if userInput == "quit":
        print("Bye!")
        break
    elif userInput == "info":
        #This will give info of the file you passed in, in the arguments
        printInfo(fileName)
    elif "cd" in userInput:
        fileToStat = userInput.split()
        if(len(fileToStat) <= 1):
            print("Please enter cd <dir> to go to it")
        elif(len(fileToStat) > 1):
            fileToStat = fileToStat[1]
            newTup = changeDir(fileToStat,fileName, newTup[1])
            if(newTup == None):
                continue

            directory = newTup[0][0]

    elif "stat" in userInput:
        #This is the STAT function, This ~semi~ needs the ls function since the ls can get info about the first clustor of data, and then we can get info on that from finding those files in the ls module.
        fileToStat = userInput.split()
        if(len(fileToStat) <= 1):
            print("Please enter stat <filename> to get the statistics of it")
        elif(len(fileToStat) > 1):
            fileToStat = fileToStat[1]
            runToStat(fileToStat,fileName, newTup[1])
    elif userInput == "ls":
        doLs(fileName, newTup[1])
    elif "read" in userInput:
        inputList = userInput.split()
        readFile(inputList[1],inputList[2],inputList[3],fileName, newTup[1])
