#!/usr/bin/env python3

# This will be called before the test
def setup_function(fn):
    if fn == test1:
        print('Test1 setup Configuration')
    elif fn == testTwo:
        print('TestTwo setup Configuration')
    else:
        print('Something wacky going on')

# This will be called once the test is done
def teardown_function(fn):
    if fn == test1:
        print('Test1 shutdown Configuration')
    elif fn == testTwo:
        print('TestTwo shutdown Configuration')
    else:
        print('Something wacky going on')


def test1():
    print('!!test1!!!!!')
    assert True

def testTwo():
    print('This Is TEST TWO')
    assert True
