#!/usr/bin/env python3

class Checkout:
    def __init__(self):
        self.prices = {}
        self.total = 0

    def addItemPrice(self, itemName, price):
        self.prices[itemName] = price

    def addItem(self, itemName):
        self.total += self.prices[itemName]

    def calculateTotal(self):
        return self.total
