#!/usr/bin/env python3
import pytest
from checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout

def test_canCalculateTotal(checkout):
    checkout.addItemPrice("a", 1)
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1
