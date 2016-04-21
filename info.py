from Utilities import *


def bytesPerSector(fileName):
    return getInfo(fileName, 11, 2, 0)

def secPerClus(fileName):
    return getInfo(fileName, 13, 1, 0)

def rsvdSecCnt(fileName):
    return getInfo(fileName, 14, 2, 0)

def rootEntCnt(fileName):
    return getInfo(fileName,17,2,0)

def numFats(fileName):
    return getInfo(fileName, 16, 1, 0)

def fatsZ32(fileName):
    return getInfo(fileName, 36, 4, 0)

def numFats(fileName):
    return getInfo(fileName, 16, 1, 0)

def getInfo(fileName, offset, size, whereToStart):
    newFile = openFile(fileName)
    newFile.seek(offset,whereToStart)
    byte = newFile.read(size)
    closeFile(newFile)
    return endinanessOrder(byte)

def printInfo(fileName):
    print("BPB_BytesPerSec is {}, {}".format(getByteString(bytesPerSector(fileName)),bytesPerSector(fileName)))
    print("BPB_SecPerClus is {}, {}".format(getByteString(secPerClus(fileName)),secPerClus(fileName)))
    print("BPB_RsvdSecCnt is {}, {}".format(getByteString(rsvdSecCnt(fileName)),rsvdSecCnt(fileName)))
    print("BPB_NumFATs is {}, {}".format(getByteString(numFats(fileName)),numFats(fileName)))
    print("BPB_FATSz32 is {}, {}".format(getByteString(fatsZ32(fileName)),fatsZ32(fileName)))
    #print("BPB_RootClus is {}, {}".format(getByteString(rootClus(fileName)),rootClus(fileName)))
