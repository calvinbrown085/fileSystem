#Program: Utilities.py
#Authors: Calvin Brown, Chad Gilmer
#Description: Provides utilities so our code base is cleaner
import struct

def bytesPerSector(fileName):
    return getInfo(fileName, 11, 2, 0)

def secPerClus(fileName):
    return getInfo(fileName, 13, 1, 0)

def rsvdSecCnt(fileName):
    return getInfo(fileName, 14, 2, 0)


def numFats(fileName):
    return getInfo(fileName, 16, 1, 0)

def fatsZ32(fileName):
    return getInfo(fileName, 36, 4, 0)

def numFats(fileName):
    return getInfo(fileName, 16, 1, 0)

def rootClus(fileName):
    firstDataSector = rsvdSecCnt(fileName) + (numFats(fileName) * fatsZ32(fileName)) + 0;
    N = getInfo(fileName, 44, 4, 0)
    firstSectorOfCluster = ((N - 2) * secPerClus(fileName)) + firstDataSector
    sizeOfCluster = firstSectorOfCluster * bytesPerSector(fileName)
    print(getInfo(fileName, sizeOfCluster, 11, 0))
    #print(getInfo(fileName,0, 11, sizeOfCluster))
    #thisFATSecNum = thisFatSecNum(fileName, N)
    #FATOffset = fatOffset(fileName, N)
    #print(hex(getInfo(fileName, thisFATSecNum,FATOffset)))

def thisFatSecNum(fileName, N):
    return int(rsvdSecCnt(fileName) + ((N * 4) / bytesPerSector(fileName)));

def fatOffset(fileName, N):
    return (N * 4) % bytesPerSector(fileName)

def getInfo(fileName, offset, size, whereToStart):
    newFile = open(str(fileName), "rb")
    newFile.seek(offset,whereToStart)
    byte = newFile.read(size)
    newFile.close()
    return int.from_bytes(byte, byteorder='little', signed=False)

def getByteString(number):
    byteString = struct.pack('>I', number)
    hexNumber = "0x"
    boolean = True
    for byte in byteString:
        newByte = hex(byte).replace("x","")
        hexNumber += newByte

    return hexNumber



def printInfo(fileName):
    print("BPB_BytesPerSec is {}, {}".format(getByteString(bytesPerSector(fileName)),bytesPerSector(fileName)))
    print("BPB_SecPerClus is {}, {}".format(getByteString(secPerClus(fileName)),secPerClus(fileName)))
    print("BPB_RsvdSecCnt is {}, {}".format(getByteString(rsvdSecCnt(fileName)),rsvdSecCnt(fileName)))
    print("BPB_NumFATs is {}, {}".format(getByteString(numFats(fileName)),numFats(fileName)))
    print("BPB_FATSz32 is {}, {}".format(getByteString(fatsZ32(fileName)),fatsZ32(fileName)))
    #print("BPB_RootClus is {}, {}".format(getByteString(rootClus(fileName)),rootClus(fileName)))
