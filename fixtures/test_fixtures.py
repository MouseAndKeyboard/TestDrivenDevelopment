#!/usr/bin/env python3

import pytest

@pytest.fixture(autouse=True)
def setup():
    print('SETTING UP STUFF')
def test1():
    print('executing test')
    assert True


def test2():
    print('doing the second test')
    assert True
