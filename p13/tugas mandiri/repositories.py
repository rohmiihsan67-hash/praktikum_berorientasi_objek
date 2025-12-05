from typing import List, Optional
from models import Product

class ProductRepository:
    def __init__(self):
        self._products = [
            Product(1, "Laptop Gaming", 15000000),
            Product(2, "Mouse Wireless", 150000),
            Product(3, "Mechanical Keyboard", 500000),
            Product(4, "Monitor 24 inch", 2000000),
            Product(5, "USB Hub", 100000)
        ]

    def get_all(self) -> List[Product]:
        return self._products

    def find_by_id(self, product_id: int) -> Optional[Product]:
        for p in self._products:
            if p.id == product_id:
                return p
        return None