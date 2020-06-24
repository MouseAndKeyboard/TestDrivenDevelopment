#!/usr/bin/env python3

import pytest

def fizzBuzz(value):
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
