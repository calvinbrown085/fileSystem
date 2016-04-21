
from statInfo import *


def readFile(fileName, offset, size,image):

    fileList = getFileList(image)
    print(fileList)
    boolean = False
    getTup = ()
    for tup in fileList:
        if(fileName in tup[0]):
            boolean = True
            getTup = tup
    if(boolean == False):
        print("Error: file/directory does not exist")
        return None

    DIR_FstClusLO = endinanessOrder(getFileInfo(image, 26,2,getTup[1]))
    DIR_FstClusHI = endinanessOrder(getFileInfo(image, 20,2,getTup[1]))

    clusterNumber = int(str(DIR_FstClusHI)+str(DIR_FstClusLO))
    N = clusterNumber
    rootDirSectors = int(((rootEntCnt(image) * 32) + (bytesPerSector(image) - 1)) / bytesPerSector(image))
    firstDataSector = rsvdSecCnt(image) + (numFats(image) * fatsZ32(image)) + rootDirSectors
    firstSectorOfCluster = ((N - 2) * secPerClus(image)) + firstDataSector * 512
    
    print(firstSectorOfCluster)
    print(getStrFromFile(image,0,15, firstSectorOfCluster))




def getStrFromFile(fileName, offset, size, startCluster):
    newFile = openFile(fileName)
    newFile.seek(startCluster,0)
    newFile.seek(offset,1)
    byte = newFile.read(size)
    closeFile(newFile)
    return byte



def getFileInfo(fileName, offset, size, startCluster):
    newFile = openFile(fileName)
    newFile.seek(startCluster,0)
    newFile.seek(offset,1)
    byte = newFile.read(size)
    closeFile(newFile)
    return byte
