
from lsInfo import *
from Utilities import *

def getFileList(fileName, N):
    newList = getSectorInfoForFiles(fileName, N)
    return newList

def getFileSize(fileName, fileToOpen, N):
    fileList = getFileList(fileToOpen, N)
    boolean = False
    getTup = ()
    for tup in fileList:
        if(fileName in tup[0]):
            boolean = True
            getTup = tup
    if(boolean == False):
        print("Error: directory does not exist")
        return None
    fileSize = getStatFileInfo(fileToOpen,28, 4, getTup[1])
    return endinanessOrder(fileSize)

def runToStat(fileName, fileToOpen, N):
    fileList = getFileList(fileToOpen, N)

    boolean = False
    getTup = ()
    for tup in fileList:
        if(fileName in tup[0]):
            boolean = True
            getTup = tup
    if(boolean == False):
        print("Error: file/directory does not exist")
        return None
    fileSize = getStatFileInfo(fileToOpen,28, 4, getTup[1])
    fileAttr = getStatFileInfo(fileToOpen, 11,1,getTup[1])
    nextClusterNumber = getStatFileInfo(fileToOpen,26,2,getTup[1])
    nextClusterNumber = getByteString(endinanessOrder(nextClusterNumber))
    prettyPrintStat(fileSize,endinanessOrder(fileAttr),nextClusterNumber)


def getStatFileInfo(fileName, offset, size, startCluster):
    newFile = openFile(fileName)
    newFile.seek(startCluster,0)
    newFile.seek(offset,1)
    byte = newFile.read(size)
    closeFile(newFile)
    return byte


def prettyPrintStat(fileSize, fileAttr, nextClusterNumber):
    print("File Size Is: {}".format(endinanessOrder(fileSize)))
    print("File Attributes: {}".format(determineFileAttr(fileAttr)))
    print("Next Cluster Number: {}".format(nextClusterNumber))

def determineFileAttr(fileAttr):
    if fileAttr == 1:
        return "ATTR_READ_ONLY"
    elif fileAttr == 2:
        return "ATTR_HIDDEN"
    elif fileAttr == 4:
        return "ATTR_SYSTEM"
    elif fileAttr == 8:
        return "ATTR_VOLUME_ID"
    elif fileAttr == 16:
        return "ATTR_DIRECTORY"
    elif fileAttr == 32:
        return "ATTR_ARCHIVE"
