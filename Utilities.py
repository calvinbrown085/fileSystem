#Program: Utilities.py
#Authors: Calvin Brown, Chad Gilmer
#Description: Provides utilities so our code base is cleaner
import struct


def getByteString(number):
    byteString = struct.pack('>I', number)
    hexNumber = "0x"
    for byte in byteString:
        newByte = hex(byte).replace("x","")
        hexNumber += newByte

    return hexNumber


def openFile(fileName):
    newFile = open(str(fileName), "rb")
    return newFile

def closeFile(fileObject):
    fileObject.close()


def endinanessOrder(byte):
    return int.from_bytes(byte, byteorder='little', signed=False)


def makeFileTuple(stringToClean,startCluster):
    stringToClean = stringToClean.replace("TRASHE~1", "")
    stringToClean = stringToClean.replace("\n", " ")
    newString = ""
    cleanedString = ""
    newList = []
    tupList = []
    if(stringToClean.isupper()):
        newString += stringToClean
    newString = newString.replace(" ", "")
    newString = newString.replace("\n", "")
    newString = newString.replace("~1TRA", "")
    newString = newString.replace("TXT", ".TXT")
    for char in newString:
        cleanedString += char
    splitList = cleanedString.split()

    return (splitList,startCluster)

def cleanLsUp(stringToClean):
    stringToClean = stringToClean.replace("TRASHE~1", "")
    stringToClean = stringToClean.replace("CHUCKLES", "")
    stringToClean = stringToClean.replace("\n", " ")
    newString = ""
    cleanedString = ""
    newList = []
    if(stringToClean.isupper()):
        newString += stringToClean
    newString = newString.replace(" ", "")
    newString = newString.replace("\n", "")
    newString = newString.replace("~1TRA", "")
    newString = newString.replace("TXT", ".TXT")
    for char in newString:
        cleanedString += char
    splitList = cleanedString.split()
    for item in splitList:
        print(item)
