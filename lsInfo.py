
from Utilities import *
from info import *

def thisFatSecNum(fileName, N):
    return int(rsvdSecCnt(fileName) + ((N * 4) / bytesPerSector(fileName)))

def fatOffset(fileName, N):
    return (N * 4) % bytesPerSector(fileName)

def dirName(fileName):
    return getLsInfo(fileName,0,11,2050)



def getLsInfo(fileName,offset,size,rootClus):
    newFile = openFile(fileName)
    newFile.seek(rootClus,0)
    newFile.seek(offset,1)
    byte = newFile.read(size)
    closeFile(newFile)
    return byte


def rootClus(fileName):
    firstDataSector = rsvdSecCnt(fileName) + (numFats(fileName) * fatsZ32(fileName)) + 0;
    N = getInfo(fileName, 44, 4, 0)

    firstSectorOfCluster = ((N - 2) * secPerClus(fileName)) + firstDataSector

    clusterAddress = firstSectorOfCluster * bytesPerSector(fileName)
    #print(getLsInfo(fileName,0,11,clusterAddress))
    printFileNames(fileName)
    #print(getInfo(fileName,0, 11, sizeOfCluster))
    #thisFATSecNum = thisFatSecNum(fileName, N)
    #FATOffset = fatOffset(fileName, N)
    #print(hex(getInfo(fileName, thisFATSecNum,FATOffset)))

def getSectorInfoForFiles(fileName):
    firstDataSector = rsvdSecCnt(fileName) + (numFats(fileName) * fatsZ32(fileName)) + 0;
    N = getInfo(fileName, 44, 4, 0)
    firstSectorOfCluster = ((N - 2) * secPerClus(fileName)) + firstDataSector
    clusterAddress = firstSectorOfCluster * bytesPerSector(fileName)
    newStr = ""
    DIR_NAME = b""
    newList = []
    newTup = ()
    while b"\xe5" not in DIR_NAME:
        DIR_NAME = getLsInfo(fileName,0,11,clusterAddress)
        FILE_SIZE = endinanessOrder(getLsInfo(fileName,28,4, clusterAddress))

        for byte in DIR_NAME:
            newStr += chr(byte)
        newTup = makeFileTuple(newStr,clusterAddress)
        newStr = ""
        clusterAddress+=32
        newList.append(newTup)

    return newList


def doLs(fileName):
    firstDataSector = rsvdSecCnt(fileName) + (numFats(fileName) * fatsZ32(fileName)) + 0;
    N = getInfo(fileName, 44, 4, 0)
    firstSectorOfCluster = ((N - 2) * secPerClus(fileName)) + firstDataSector
    clusterAddress = firstSectorOfCluster * bytesPerSector(fileName)
    newStr = ""
    DIR_NAME = b""
    newList = []
    while b"\xe5" not in DIR_NAME:
        DIR_NAME = getLsInfo(fileName,0,11,clusterAddress)
        FILE_SIZE = endinanessOrder(getLsInfo(fileName,28,4, clusterAddress))

        for byte in DIR_NAME:
            newStr += chr(byte)
        newList = cleanLsUp(newStr)
        newStr = ""
        clusterAddress+=32

    getSectorInfoForFiles(fileName)
    return newList
