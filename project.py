class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


class Bill:
    def __init__(self, tax_rate=0.18):  # 18% GST
        self.products = []
        self.tax_rate = tax_rate

    def add_product(self, product):
        self.products.append(product)

    def calculate_subtotal(self):
        return sum(product.total_price() for product in self.products)

    def calculate_tax(self):
        return self.calculate_subtotal() * self.tax_rate

    def calculate_total(self):
        return self.calculate_subtotal() + self.calculate_tax()

    def display_bill(self):
        print("\n" + "=" * 50)
        print("               FINAL BILL")
        print("=" * 50)
        print(f"{'Product':<15}{'Price':<10}{'Qty':<10}{'Amount':<10}")
        print("-" * 50)

        for product in self.products:
            print(f"{product.name:<15}{product.price:<10}{product.quantity:<10}{product.total_price():<10}")

        print("-" * 50)
        print(f"{'Subtotal':<35}{self.calculate_subtotal():.2f}")
        print(f"{'Tax (18%)':<35}{self.calculate_tax():.2f}")
        print(f"{'Grand Total':<35}{self.calculate_total():.2f}")
        print("=" * 50)


# Main Program
bill = Bill()

n = int(input("Enter number of products: "))

for i in range(n):
    print(f"\nProduct {i+1}")
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    product = Product(name, price, quantity)
    bill.add_product(product)

bill.display_bill()