from src.axentx_product.portfolio import Portfolio
from src.axentx_product.product import Product

def test_portfolio_add_product():
    portfolio = Portfolio()
    product = Product("Test Product", 10, 100)
    portfolio.add_product(product)
    assert len(portfolio.get_products()) == 1

def test_portfolio_add_invalid_product():
    portfolio = Portfolio()
    product = Product("Test Product", 0, 100)
    portfolio.add_product(product)
    assert len(portfolio.get_products()) == 0
