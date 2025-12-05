from repositories import ProductRepository
# Pastikan DebitCardPayment di-import
from services import CartService, IPaymentProcessor, CashPayment, DebitCardPayment
from models import Product

class PosApp:
    def __init__(self, product_repo: ProductRepository, cart_service: CartService, payment_processor: IPaymentProcessor):
        self.repo = product_repo
        self.cart_service = cart_service
        self.payment_processor = payment_processor

    def show_products(self):
        print("\n--- KATALOG PRODUK ---")
        for p in self.repo.get_all():
            print(f"[{p.id}] {p.name:<25} Rp {p.price:,.0f}")

    def add_to_cart(self):
        try:
            p_id = int(input("Pilih ID Produk : "))
            qty = int(input("Jumlah Beli     : "))
            product = self.repo.find_by_id(p_id)
            if product:
                self.cart_service.add_product(product, qty)
            else:
                print("Error: Produk tidak ditemukan.")
        except ValueError:
            print("Error: Masukkan angka saja.")

    def checkout(self):
        total = self.cart_service.calculate_total()
        if total == 0:
            print("Keranjang masih kosong.")
            return
        
        print(f"\nTotal Tagihan: Rp {total:,.0f}")
        confirm = input("Lanjut Bayar (y/n)? ")
        if confirm.lower() == 'y':
            # Ini akan memanggil DebitCardPayment yang keren tadi
            if self.payment_processor.process_payment(total):
                print(">>> STRUK TRANSAKSI DICETAK <<<")
                self.cart_service.clear_cart()
        else:
            print("Pembayaran dibatalkan.")

    def run(self):
        while True:
            # Header Menu Dibuat Beda
            print("\n" + "#"*40)
            print("   MODUL 13: CHALLENGE DEBIT SYSTEM   ")
            print("#"*40)
            print("1. Lihat Katalog")
            print("2. Tambah Barang")
            print("3. Bayar (Debit)")
            print("4. Keluar")
            
            choice = input("Pilih Menu (1-4): ")
            if choice == '1': self.show_products()
            elif choice == '2': self.add_to_cart()
            elif choice == '3': self.checkout()
            elif choice == '4': break

if __name__ == "__main__":
    repo = ProductRepository()
    cart_svc = CartService()
    
    # --- WIRING TUGAS MANDIRI ---
    # Menggunakan DebitCardPayment agar outputnya kotak-kotak (EDC)
    payment_method = DebitCardPayment() 
    
    app = PosApp(repo, cart_svc, payment_method)
    app.run()