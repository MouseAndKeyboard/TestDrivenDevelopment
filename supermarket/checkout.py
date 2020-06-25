#!/usr/bin/env python3

class Checkout:

    class Discount:
        def __init__(self, nbrItems, price):
            self.nbrItems = nbrItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def addItemPrice(self, itemName, price):
        self.prices[itemName] = price

    def addItem(self, itemName):
        if itemName in self.items:
            self.items[itemName] += 1
        else:
            self.items[itemName] = 1

    def calculateTotal(self):
        total = 0
        for item, count in self.items.items():
            if item in self.discounts:
                discount = self.discounts[item]
                if count >= discount.nbrItems:
                    nbrOfDiscounts = count / discount.nbrItems
                    total += nbrOfDiscounts * discount.price
                    remaining = count % discount.nbrItems
                    total += remaining * self.prices[item]
                else:
                    total += self.prices[item] * count
            else:
                total += self.prices[item] * count
        return total

    def addDiscount(self, item, nbrItems, price):
        discount = self.Discount(nbrItems, price)
        self.discounts[item] = discount
