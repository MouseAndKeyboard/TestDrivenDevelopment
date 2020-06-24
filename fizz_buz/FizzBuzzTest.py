#!/usr/bin/env python3

import pytest

def fizzBuzz(value):
    return "1"

def test_canAssertTrue():
    assert True

def test_returnsWith1Passed():
    retVal = fizzBuzz(1)
    assert retVal == "1"

def test_returns2With2Passed():
    retVal = fizzBuzz(2)
    assert retVal == "2"
