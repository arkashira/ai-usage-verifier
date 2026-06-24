from src.axentx_product.product import Product

def test_product_validation():
    product = Product("Test Product", 10, 100)
    assert product.is_validated()

def test_product_invalid_demand():
    product = Product("Test Product", 0, 100)
    assert not product.is_validated()

def test_product_invalid_willingness_to_pay():
    product = Product("Test Product", 10, 0)
    assert not product.is_validated()
