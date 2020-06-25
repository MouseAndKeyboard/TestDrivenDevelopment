#!/usr/bin/env python3

def readFromFile(fileName):
    f = open(fileName, "r")
    line = f.readline()
    return line
