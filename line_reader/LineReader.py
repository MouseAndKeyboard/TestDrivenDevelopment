#!/usr/bin/env python3
import os

def readFromFile(fileName):
    if not os.path.exists(fileName):
        raise Exception("Does not exist")
    f = open(fileName, "r")
    line = f.readline()
    return line
