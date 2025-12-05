from abc import ABC, abstractmethod
from typing import List
from models import Product, CartItem

class IPaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class CashPayment(IPaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        # Output polos (versi C)
        print(f"Processing Cash Payment: Rp {amount:,.0f}")
        return True

class DebitCardPayment(IPaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        # Simulasi Tampilan Layar EDC
        print("\n" + "="*40)
        print("       ELECTRONIC PAYMENT (EDC)       ")
        print("="*40)
        print(f" [+] AMOUNT       : Rp {amount:,.0f}")
        print(" [+] CARD STATUS  : INSERTED (CHIP)")
        print(" [+] VERIFYING... : PIN MATCHED ****")
        print(" [+] CONNECTING...: BANK SERVER [OK]")
        print(" [+] TRANSACTION  : APPROVED (00)")
        print("="*40 + "\n")
        return True

class CartService:
    def __init__(self):
        self.cart_items: List[CartItem] = []

    def add_product(self, product: Product, quantity: int):
        for item in self.cart_items:
            if item.product.id == product.id:
                item.quantity += quantity
                print(f"[CART] Quantity updated: {product.name} (+{quantity})")
                return
        self.cart_items.append(CartItem(product, quantity))
        print(f"[CART] Added: {product.name} ({quantity} pcs)")

    def get_all_items(self) -> List[CartItem]:
        return self.cart_items

    def calculate_total(self) -> float:
        return sum(item.subtotal for item in self.cart_items)

    def clear_cart(self):
        self.cart_items = []
        print("[CART] Keranjang telah dikosongkan.")