class Product:
    def __init__(self, name, code, price):
        self.name = name
        self.code = code
        self.price = price

    def __str__(self):
        return f"{self.name} (Code: {self.code}) - £{self.price:.2f}"

# Create a dictionary of products
products = {
    "A1": Product(name="Crisps", code="A1", price=0.75),
    "B2": Product(name="Chocolate Bar", code="B2", price=1.00),
    "C3": Product(name="Cola", code="C3", price=1.50),
}

# Function to handle user input
def select_product():
    product_code = input("Enter the product code: ").strip().upper()
    product = products.get(product_code)
    
    if product:
        print(f"You selected: {product}")
    else:
        print("Invalid product code. Please try again.")

# Example interaction
select_product()
