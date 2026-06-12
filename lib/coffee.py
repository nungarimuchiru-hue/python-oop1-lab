#!/usr/bin/env python3

class Coffee:
    def __init__(self, size: str, price: float, tip:float = 0.0):
        valid_sizes = ['small', 'medium', 'large']
        if size.lower() not in valid_sizes:
            raise ValueError("Invalid size")
        
        self.size = size
        self._base_price = price
        self.tip = tip
        

        @property
        def name(self):
            return self._base_price + self.tip
        
        def add_tip(self,amount: float):
            self.tip += amount