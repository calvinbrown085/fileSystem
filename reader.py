import sys
import os
import struct
from Utilities import *


fileName = sys.argv[1]


#find the little endian to host equivalent for python
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
        fileToStat = userInput.split()
        if(len(fileToStat) <= 1):
            print("Please enter stat <filename> to get the statistics of it")
        elif(len(fileToStat) > 1):
            fileToStat = fileToStat[1]
            fileObject = open(fileToStat, "r")
            fileSize = getFileSize(fileObject)
            fileObject.close()
            print("Size of the file is: " + str(fileSize))
    elif userInput == "ls":
        print("ls")
