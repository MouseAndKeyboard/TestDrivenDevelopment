#!/usr/bin/env python3
from checkout import Checkout

def test_canAddItemPrice():
    co = Checkout()
    co.addItemPrice("a", 1)
