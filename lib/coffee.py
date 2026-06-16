#!/usr/bin/env python3

class Coffee:
    def __init__(self, size: str, price: float):
        # The test expects a printed string, not a raised ValueError
        if size not in ["Small", "Medium", "Large"]:
            print("size must be Small, Medium, or Large")
            
        self.size = size
        self.price = float(price)

    # Set default amount to 1.0 because the test calls tip() with no arguments
    def tip(self, amount: float = 1.0):
        print("This coffee is great, here’s a tip!")
        self.price += float(amount)