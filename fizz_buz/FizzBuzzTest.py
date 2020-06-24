#!/usr/bin/env python3

import pytest

def fizzBuzz(value):
    if isMultiple(value, 3):
        return "Fizz"
    elif isMultiple(value, 5):
        return "Buzz"
    return str(value)
def isMultiple(value, mod):
    return value % mod == 0

def test_canAssertTrue():
    assert True
def checkFizzBuzz(value, expectedRet):
    retVal = fizzBuzz(value)
    assert retVal == expectedRet

def test_returnsWith1Passed():
    checkFizzBuzz(1, "1")

def test_returns2With2Passed():
    checkFizzBuzz(2, "2")

def test_returnsFizzWith3Passed():
    checkFizzBuzz(3, "Fizz")

def test_returnsBuzzWith5Passed():
    checkFizzBuzz(5, "Buzz")

def test_returnsFizzWith6Passed():
    checkFizzBuzz(6, "Fizz")

def test_returnsBuzzWith10Passed():
    checkFizzBuzz(10, "Buzz")

def test_returnsFizzBuzzWith15Passed():
    checkFizzBuzz(15, "FizzBuzz")
