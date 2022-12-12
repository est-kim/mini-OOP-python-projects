class CashRegister:

    TAX_RATE = 0.05

    def __init__(self, cashier):
        self.products = {}
        self.cashier = cashier
        self.subtotal = 0

    def add_product(self, new_product, quantity=1):
        self.products[new_product["name"]] = {
            "price" : new_product["price"],
            "quantity" : quantity
        }
        self.subtotal += new_product["price"] * quantity

    def update_price(self, product, new_price):
        self.products[product]["price"] = new_price

    def find_subtotal(self):
        print(f"Subtotal: {self.subtotal}")

    def show_products(self):
        print(self.products)

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

#creating an instance
my_cash_register = CashRegister("Esther")

#creating products
product1 = {"name": "Hot Cheetos", "price": 4.99}
product2 = {"name": "Kombucha", "price": 3.99}
product3 = {"name": "Bread", "price": 6.49}
product4 = {"name": "Salad", "price": 5.49}

#adding products
my_cash_register.add_product(product1, 2)
my_cash_register.add_product(product2, 4)
my_cash_register.add_product(product3)
my_cash_register.add_product(product4)

my_cash_register.show_products()

#removing product
my_cash_register.remove_product("Salad")
my_cash_register.show_products()

#updating product price
my_cash_register.update_price("Hot Cheetos", 5.39)
my_cash_register.show_products()

#print subtotal, taxes, and total
my_cash_register.find_subtotal()
my_cash_register.print_taxes()
my_cash_register.print_total()

#clearing register
my_cash_register.clear_purchase()
my_cash_register.show_products()
