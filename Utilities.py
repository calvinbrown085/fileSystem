import struct

def bytesPerSector(fileName):
    return getInfo(fileName, 11, 2)

def secPerClus(fileName):
    return getInfo(fileName, 13, 1)

def rsvdSecCnt(fileName):
    return getInfo(fileName, 14, 2)

def numFats(fileName):
    return getInfo(fileName, 16, 1)

def fatsZ32(fileName):
    return getInfo(fileName, 36, 4)

def getInfo(fileName, offset, size):
    newFile = open(str(fileName), "rb")
    newFile.seek(offset,0)
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
