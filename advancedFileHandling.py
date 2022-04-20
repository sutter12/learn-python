# Author: Alexander Sutter
# Date: 4/20/2022
# Latest Revision: 4/20/2022
# advancedFileHandling.py

import os

def createFile(fileName="defaultFile.txt"):
    try:
        return open(fileName)
    except:
        print("error opening file")

def deleteFile(fileName):
    if existsFile(fileName):
        os.remove(fileName)
    else:
        print("Failed to remove file")

def existsFile(fileName):
    if os.path.exists(fileName):
        return True
    else:
        return False

def read(fileName):
    file = open(fileName, 'r')
    data = file.read()
    return data

def write(fileName, data, openType):
    file = open(fileName, openType)
    file.write(data)
    file.close()

def main():
    fileName = "defaultFile.txt"

    createFile(fileName)

    write(fileName, "Hello World!", 'w')

    print(read(fileName))

    write(fileName, "Hello World 2!", 'a')

    print(read(fileName))

main()