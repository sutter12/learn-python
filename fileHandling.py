# Author: Alexander Sutter
# Date: 2/11/2022
# Latest Revision: 4/20/2022
# fileHandling.py

def createFile(fileName="defaultFile.txt"):
    try:
        return open(fileName)
    except:
        print("error opening file")

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