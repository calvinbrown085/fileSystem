from statInfo import *
from Utilities import *

def changeDir(fileName,fileImage, N):
    fileList = getFileList(fileImage, N)
    getTup = ()
    boolean = False
    for tup in fileList:
        if(fileName in tup[0]):
            boolean = True
            getTup = tup
    if(boolean == False):
        print("Error: directory does not exist")
        return ("",N)
    fileAttr = getStatFileInfo(fileImage, 11,1,getTup[1])
    if(determineFileAttr(endinanessOrder(fileAttr)) != "ATTR_DIRECTORY"):
        print(fileName, "is not a directory")
        return ("",N)
    DIR_FstClusLO = endinanessOrder(getFileInfo(fileImage, 26,2,getTup[1]))
    DIR_FstClusHI = endinanessOrder(getFileInfo(fileImage, 20,2,getTup[1]))

    clusterNumber = int(str(DIR_FstClusHI)+str(DIR_FstClusLO))
    N = clusterNumber
    #doLs(fileImage, N)
    return (getTup[0], N)



def getFileInfo(fileName, offset, size, startCluster):
    newFile = openFile(fileName)
    newFile.seek(startCluster,0)
    newFile.seek(offset,1)
    byte = newFile.read(size)
    closeFile(newFile)
    return byte
