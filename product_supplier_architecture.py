class Supplier:
    def __init__(self, name):
        self.supplier_name = name


class Specification:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)


class Product:
    def __init__(self, pid, name, supplier):
        self.product_id = pid
        self.product_name = name
        self.supplier = supplier
        self.spec = None

    def add_specification(self):
        brand = input("Enter brand: ")
        price = input("Enter price: ")
        self.spec = Specification(brand, price)

    def display(self):
        print("\nProduct ID:", self.product_id)
        print("Product Name:", self.product_name)
        print("Supplier:", self.supplier.supplier_name)
        if self.spec:
            self.spec.display()


sname = input("Enter supplier name: ")
supplier = Supplier(sname)

n = int(input("Enter number of products: "))
products = []

for i in range(n):
    pid = int(input("Enter product id: "))
    pname = input("Enter product name: ")
    p = Product(pid, pname, supplier)
    p.add_specification()
    products.append(p)

for p in products:
    p.display()
