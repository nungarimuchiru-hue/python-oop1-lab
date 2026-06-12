#!/usr/bin/env python3

class Coffee:
    def __init__(self, size: str, price: float):
        valid_sizes = ["small", "medium", "large"]
        if size not in valid_sizes:
            raise ValueError("size must be Small, Medium, or Large\n ")
        
        self.size = size
        self._base_price = price
        self._tip_amount = 0.0
        
    @property
    def size(self):
        return self._size
    
    @property
    def price(self):
        return self._base_price + self._tip_amount
    
    def tip(self, amount: float = None):
        if amount is not None:
            self._tip_amount += amount
            return self._tip_amount