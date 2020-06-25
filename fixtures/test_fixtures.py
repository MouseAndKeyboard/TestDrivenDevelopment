#!/usr/bin/env python3

import pytest

@pytest.fixture()
def setup():
    print('SETTING UP STUFF')

def test1(setup):
    print('executing test')
    assert True

@pytest.mark.useFixtures("setup")
def test2():
    print('doing the second test')
    assert True
