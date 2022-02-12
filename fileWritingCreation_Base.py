# Author: Alexander Sutter
# Date: 2/11/2022
# fileReadingWriting_Base.py

def openLogFile(fileName="fileReadingWriting_Base_Default.txt"):
    try:
        return open(fileName, "a")
    except:
        print("error opening file")

def writeLog(logItem):
    logFile = openLogFile("fileReadingWriting_Base_Default.txt")
    logFile.write(logItem + "\n")
    logFile.close()

def log(logItem):
    # print("log item: " +str(logItem))
    writeLog("log item: " +str(logItem))

def logError(logItem):
    # print("Error: " +str(logItem))
    writeLog("Error: " +str(logItem))

log("Hello World")