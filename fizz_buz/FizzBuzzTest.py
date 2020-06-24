#!/usr/bin/env python3

import pytest

def fizzBuzz(value):
    if value == 3:
        return "Fizz"
    elif value == 5:
        return "Buzz"
    return str(value)

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
