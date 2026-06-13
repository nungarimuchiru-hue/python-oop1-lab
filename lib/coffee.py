#!/usr/bin/env python3

class Coffee:
    def __init__(self, size: str, price: float):
        # 1. Validate the size exactly as required by the test
        if size not in ["Small", "Medium", "Large"]:
            raise ValueError("size must be Small, Medium, or Large")
            
        self.size = size
        self.price = float(price)

    def tip(self, amount: float):
        # 2. Print the exact expected string (including the curly apostrophe)
        print("This coffee is great, here’s a tip!")
        
        # 3. Add the tip amount to update the object's price attribute
        self.price += float(amount)
