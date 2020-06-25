#!/usr/bin/env python3

import pytest
@pytest.fixture(scope="session", autouse=True)
def setupSession():
    print('setting up session')


@pytest.fixture(scope="session", autouse=True)
def setupModule():
    print('setting up the module')


@pytest.fixture(scope="session", autouse=True)
def setupFunction():
    print('setting up the function')

def test1():
    print('running first test')
    assert True

def test2():
    print('running second test')
    assert True
