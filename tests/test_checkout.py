import pytest

from pages.AddProductsInAmazon import AddProductsInAmazon
from pages.ProceedToCheckout import ProceedToCheckout
from tests.test_add_product_to_cart import TestAddProductToCart

@pytest.mark.reg
class TestCheckout:
    def test_checkout(self,init_driver):
        
        add_prod=AddProductsInAmazon(init_driver)
        add_prod.add_products_feature20()

        checkout=ProceedToCheckout(init_driver)
        checkout.proceed_to_checkout("7207962483","Vijay@8500","123456781234","Anegondi Vijay","value","06","2031")
        print("done---------------")
