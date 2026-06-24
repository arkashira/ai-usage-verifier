from .product import Product

class Portfolio:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if product.is_validated():
            self.products.append(product)

    def get_products(self):
        return self.products
