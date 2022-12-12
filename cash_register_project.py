class CashRegister:

    TAX_RATE = 0.05

    def __init__(self, cashier):
        self.products = {}
        self.cashier = cashier
        self.subtotal = 0

    @property
    def products(self):
        return self.products

    def add_product(self, new_product, quantity=1):
        if isinstance(new_product, str):
            self.products[new_product["name"]] = {
                "price" : new_product["price"],
                "quantity" : quantity
            }
            self.subtotal += new_product["price"] * quantity
        else:
            print("Please provide a valid product.")

    def update_price(self, product, new_price):
        if isinstance(self.products[product]["price"], float):
            self.products[product]["price"] = new_price
        else:
            print("Please provide a valid price.")

    def find_subtotal(self):
        print(f"Subtotal: {self.subtotal}")

    def show_products(self):
        print(sorted(self.products))

    def remove_product(self, product):
        del self.products[product]

    def find_taxes(self):
        return round(self.subtotal * CashRegister.TAX_RATE, 2)

    def print_taxes(self):
        print(f"Taxes: {self.find_taxes()}")

    def find_total(self):
        return round(self.subtotal + self.find_taxes(), 2)

    def print_total(self):
        print(f"Total: {self.find_total()}")

    def clear_purchase(self):
        self.products.clear()
